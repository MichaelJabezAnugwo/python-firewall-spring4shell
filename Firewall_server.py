from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class FirewallHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Block based on suspicious request path
        if self.path == "/tomcatwar.jsp":
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Blocked: Suspicious path")
            return

        # 2. Read and decode the request body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        # 3. Parse the body into key-value pairs
        parsed_data = urllib.parse.parse_qs(post_data)

        # 4. Check for malicious parameter keys
        for key in parsed_data:
            if "class.module.classLoader" in key:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Blocked: Malicious parameter key")
                return

        # 5. Check for malicious header values
        suspicious_headers = {
            "suffix": "%>//",
            "c1": "Runtime",
            "c2": "<%",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        for header, bad_value in suspicious_headers.items():
            if header in self.headers and bad_value in self.headers[header]:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Blocked: Suspicious header detected")
                return

        # 6. If nothing suspicious, allow the request
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Request allowed")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FirewallHandler)
    print("Firewall server running on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
