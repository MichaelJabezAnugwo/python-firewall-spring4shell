# python-firewall-spring4shell

A defensive Python-based scripting simulation of a web application firewall that detects and blocks Spring4Shell-style exploits.
=======
```markdown

This project simulates a basic firewall using Python’s built-in HTTP server. It is designed to detect and block malicious HTTP POST requests that attempt to exploit the Spring4Shell vulnerability (CVE-2022-22965). The simulation demonstrates how defensive scripting can be used to mitigate real-world web application threats.

---

Project Structure

| File               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `firewall_server.py` | Core firewall logic that inspects and filters incoming HTTP POST requests |
| `test_requests.py`   | Script to simulate both malicious and clean HTTP requests for testing     |
| `README.md`          | Project documentation                                                     |

---

How to Run the Simulation

1. Prerequisites
- Python 3.x installed
- `requests` library installed:
  ```bash
  pip install requests
  ```

### 2. Start the Firewall Server
```bash
python firewall_server.py
```
You should see:
```
Firewall server running on port 8000...
```

### 3. Run the Test Script
In a separate terminal:
```bash
python test_requests.py
```

---

## What the Firewall Blocks

The firewall inspects:
- **Request Path**: Blocks `/tomcatwar.jsp`
- **Request Headers**: Blocks if headers contain:
  - `suffix=%>//`
  - `c1=Runtime`
  - `c2=<%`
  - `Content-Type: application/x-www-form-urlencoded`
- **Request Body**: Blocks if it contains keys like:
  - `class.module.classLoader.resources.context.parent.pipeline.first.pattern`

Blocked requests return:
```
403 Forbidden
```

Clean requests return:
```
200 OK
```

---

## What I Learned

- How to simulate a firewall using Python’s `http.server` module
- How to inspect and filter HTTP requests based on headers, paths, and payloads
- How to test security logic using automated scripts
- How Spring4Shell works and how to mitigate it

---

## Use Case

This project is ideal for:
- Cybersecurity students learning about web application firewalls (WAFs)
- Developers exploring Python for security automation
- Demonstrating defensive scripting in InfoSec interviews or portfolios

---

## 👨‍💻 Author

**Michael Jabez Anugwo**  
Cybersecurity Enthusiast | Penetration Tester | Security Explorer

---

## License

This project is for educational purposes only.
