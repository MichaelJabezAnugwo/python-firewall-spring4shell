Incident Postmortem: Malware Attack Leading to NBN Outage
Summary
- Incident Start Time: 2022-03-20T03:16:34Z
- Incident End Time: 2022-03-20T05:16:34Z
- Detection Time: 2022-03-20T03:16:34Z
- Root Cause Fixed Time: 2022-03-20T05:16:34Z
- Participants: Telstra Security Operations, NBN Team, Networks Team
- Status: Resolved
- Severity: 1 – Critical

Impact
- Significant impairment and downtime of NBN services across the network.
- Remote code execution was successfully performed on NBN service infrastructure.
- Critical disruption to customer connectivity and service availability.

Detection
- Initial detection occurred via firewall logs that flagged abnormal HTTP activity.
- Simultaneously, customer complaints about degraded service performance escalated the issue.
- These indicators prompted immediate investigation by Telstra Security Operations.

Root Cause
- The attacker exploited the Spring4Shell zero-day vulnerability (CVE-2022-22965).
- At 03:16:34Z, malicious HTTP POST requests were sent to nbn.external.network targeting the path /tomcatwar.jsp.
- Payloads included exploit code that leveraged class.module.classLoader to achieve remote code execution.
- Firewall alerts and customer reports confirmed the attack vector and its success.

Resolution
- 03:16–03:46Z:
Telstra Security Operations triaged the firewall alerts and escalated the incident to the NBN team.
- 03:46–04:16Z:
Security analysts conducted forensic analysis of the firewall logs, identifying consistent patterns in the malicious requests.
- 04:16–05:16Z:
The Networks team developed and deployed a Python-based firewall rule to block requests matching the Spring4Shell payload signature, referencing the public PoC.
- Once deployed, the firewall rule successfully mitigated the attack, restoring service functionality. A full forensic investigation was initiated post-resolution.

Action Items
- ✅ Deploy and maintain the custom firewall rule to block Spring4Shell-style payloads.
- 🔄 Collaborate with threat intelligence teams to identify and track similar exploit patterns.
- 🔐 Enhance monitoring of externally exposed frameworks and services.
- 📚 Document response playbooks for zero-day exploit scenarios
