import socket
import requests
import subprocess
import os

# ========== USER INPUT ==========
target_domain = input("Enter domain name (leave blank if not needed): ").strip()
target_ip = input("Enter target IP (leave blank to resolve from domain): ").strip()

if not target_ip and target_domain:
    try:
        target_ip = socket.gethostbyname(target_domain)
    except socket.gaierror:
        print("[!] Failed to resolve domain to IP. Exiting.")
        exit()

# ========== DNS LOOKUP ==========
def dns_lookup(domain):
    print("[+] Performing DNS Lookup...")
    try:
        result = socket.gethostbyname_ex(domain)
        print("\tHost IPs:", result[2])
    except socket.gaierror:
        print("\tDNS Lookup Failed")

# ========== WHOIS QUERY ==========
def whois_lookup(domain):
    print("[+] Performing WHOIS Lookup...")
    try:
        result = subprocess.check_output(["whois", domain]).decode()
        print("\tWHOIS result saved to whois.txt")
        with open("whois.txt", "w") as f:
            f.write(result)
    except Exception as e:
        print("\tWHOIS Lookup Failed:", e)

# ========== PORT SCAN ==========
def port_scan(ip):
    print("[+] Scanning top 100 ports...")
    open_ports = []
    for port in range(1, 102):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                print(f"\tPort {port} open")
                open_ports.append(port)
    if not open_ports:
        print("\tNo open ports found")

# ========== HTTP HEADER CHECK ==========
def http_headers(domain):
    print("[+] Checking HTTP Headers...")
    try:
        r = requests.get(f"http://{domain}")
        for header, value in r.headers.items():
            print(f"\t{header}: {value}")
    except:
        print("\tHTTP request failed")

# ========== RUN ==========
print(f"[+] Starting Recon for {target_domain or target_ip}\n")
if target_domain:
    dns_lookup(target_domain)
    whois_lookup(target_domain)
    http_headers(target_domain)
if target_ip:
    port_scan(target_ip)
print("\n[+] Recon Complete. Report saved as whois.txt if WHOIS was performed.")

