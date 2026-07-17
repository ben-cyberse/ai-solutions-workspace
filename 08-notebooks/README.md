# 📓 Cybersecurity Lab Notebook Series

**Author:** Bency (Benjamin Adjei)  
**Program:** M.S. in Cybersecurity — University of Maryland, Baltimore County (UMBC)  
**Certifications:** CISA · CISM · AWS Security Specialty · CompTIA CySA+ · CompTIA AI+

---

## Overview

A complete hands-on cybersecurity lab series built in Python/Jupyter covering network security, threat detection, incident response, cloud security, GRC, and AI security. Each notebook is self-contained with simulated data, working code, and real-world tool references.

---

## Notebook Index

| # | Notebook | Topic | Key Tools |
|---|----------|-------|-----------|
| 06 | [`06_packet_analysis.ipynb`](06_packet_analysis.ipynb) | Packet Inspection & Analysis | Scapy, PCAP |
| 07 | [`07_log_analysis_siem.ipynb`](07_log_analysis_siem.ipynb) | Log Parsing & SIEM Correlation | Python `re`, Splunk SPL, Sentinel KQL |
| 08 | [`08_security_automation.ipynb`](08_security_automation.ipynb) | Python Security Automation | `hashlib`, `secrets`, `socket` |
| 09 | [`09_network_recon_scanning.ipynb`](09_network_recon_scanning.ipynb) | Network Recon & Port Scanning | `socket`, `concurrent.futures`, Nmap |
| 10 | [`10_vulnerability_assessment_cve.ipynb`](10_vulnerability_assessment_cve.ipynb) | Vulnerability Assessment & CVE Analysis | NIST NVD API, CVSS v3 |
| 11 | [`11_incident_response_forensics.ipynb`](11_incident_response_forensics.ipynb) | Incident Response & Digital Forensics | MITRE ATT&CK, Chain of Custody |
| 12 | [`12_cloud_security_aws.ipynb`](12_cloud_security_aws.ipynb) | Cloud Security & AWS | boto3, IAM, CloudTrail, CIS Benchmark |
| 13 | [`13_grc_governance_risk_compliance.ipynb`](13_grc_governance_risk_compliance.ipynb) | GRC: Governance, Risk & Compliance | NIST CSF 2.0, ISO 27001, PCI-DSS |
| 14 | [`14_ai_security.ipynb`](14_ai_security.ipynb) | AI Security: Threats & Defences | OWASP LLM Top 10, Prompt Injection, ART |
| 15 | [`15_ai_governance.ipynb`](15_ai_governance.ipynb) | AI Governance & Responsible AI | NIST AI RMF, EU AI Act, Fairlearn, SHAP |
| 16 | [`16_ai_evaluation.ipynb`](16_ai_evaluation.ipynb) | AI Evaluation: Metrics & Benchmarking | BLEU, ROUGE, Rubric scoring, Hallucination detection |
| 17 | [`17_ai_safety_trust.ipynb`](17_ai_safety_trust.ipynb) | AI Safety & Trust | Red-teaming, NIST AI 100-1, Calibration, Alignment |

---

## Skills Demonstrated

- **Network Security** — Packet analysis, port scanning, DNS enumeration, traffic anomaly detection
- **Threat Detection** — Log parsing, SIEM correlation rules, IOC extraction, MITRE ATT&CK mapping
- **Security Automation** — Python scripting for FIM, password policy, log monitoring, audit reporting
- **Vulnerability Management** — CVE querying, CVSS scoring, service-to-CVE mapping, remediation SLAs
- **Incident Response** — Triage automation, timeline reconstruction, chain of custody, IR reports
- **Cloud Security** — AWS IAM auditing, S3 security, CloudTrail threat detection, CIS benchmarking
- **GRC** — Risk registers, NIST CSF gap analysis, multi-framework control crosswalks
- **AI Security** — Adversarial ML detection, prompt injection scanning, output safety filtering
- **AI Governance** — EU AI Act classification, bias/fairness metrics, NIST AI RMF self-assessment
- **AI Evaluation** — Rubric-based response scoring, BLEU/ROUGE metrics, hallucination detection, model benchmarking
- **AI Safety & Trust** — Red-teaming, confidence calibration, value consistency testing, NIST AI 100-1 trustworthiness

---

## How to Run

```bash
pip install jupyter scapy requests boto3
jupyter notebook
```

Each notebook uses simulated data by default — no live network access or cloud credentials required to explore the concepts.

---

## Related Folders

- [`../04-cybersecurity/`](../04-cybersecurity/) — Cybersecurity labs and scripts
- [`../05-projects/`](../05-projects/) — Portfolio projects (network scanner, log parser, etc.)
- [`../06-docs/`](../06-docs/) — Cheatsheets and notes

---

*Part of the [ai-solutions-workspace](https://github.com/ben-cyberse/ai-solutions-workspace) portfolio.*
