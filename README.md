# 🕵️ Auto Recon & Footprinting Tool

This Python script automates basic recon and footprinting tasks such as DNS lookups, WHOIS queries, HTTP header analysis, and basic TCP port scanning.

---

## 🔧 Features

- DNS resolution (A record lookup)
- WHOIS data extraction
- HTTP header analysis
- Top 100 TCP port scan
- User-prompted input (domain and/or IP)

---

## 🛠️ Requirements

- Python 3.x
- Internet connection (for WHOIS and HTTP lookups)
- Required tools:
  - `whois` command-line tool
  - Python packages: `requests`

To install missing packages:
```bash
sudo apt install whois -y
pip install requests
