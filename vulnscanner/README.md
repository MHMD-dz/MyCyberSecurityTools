# Practice Vulnerability Scanner

A small Python practice project for learning the basics of TCP port scanning, service banner grabbing, and simple string matching. It is made for experimentation in a lab you own or have permission to test.

> **Practice project:** This is an educational exercise, not a reliable vulnerability scanner. I know it will not work very well in real-world environments. Its results can be incomplete or misleading, and it should not be used to make security decisions.

## What it does

The project has two Python files:

- `portscanner.py` defines `PortScanner`. It accepts an IP address or hostname, resolves hostnames to IPv4, and attempts TCP connections to a hard-coded list of common ports. For ports that accept a connection, it tries to read up to 1024 bytes and records the port and banner.
- `vulnScanner.py` is the interactive entry point. It asks for a target and a text file, runs the port scan, then reports a banner when a non-empty line from the file appears inside it.
- `vuln.txt` is an example list of banner strings to match. The entries are examples, not a complete or authoritative vulnerability database.

The script reports matching text as `VULNERABLE`, but a text match alone does not establish that a service is vulnerable. It does not verify software versions or configurations against advisories.

## Requirements

- Python 3
- The [`IPy`] package, used to validate IP addresses

Install the dependency with:

```sh
python -m pip install IPy
```

## Run

From the project directory:

```sh
python vulnScanner.py
```

At the prompts, enter a host or IP address and the path to a banner-signature text file. For example:

```text
[+] Enter the target IP: 192.0.2.10
[+] Enter the file directory to match the banners with: vuln.txt
```

Use a system you own or have explicit authorization to scan. The scanner makes network connection attempts against the target's listed ports.

## Limitations

- The port list is fixed and covers only selected TCP ports; it does not scan every port or UDP services.
- Each connection attempt has a one-second timeout, and scanning is sequential, so results depend on network conditions and can take time.
- Banner grabbing is minimal. Many services do not send a banner until they receive a protocol-specific request, and some banners may be empty or truncated.
- The matching is basic substring comparison. It can miss vulnerabilities, produce false positives, and does not account for patched builds, backported fixes, configuration, or context.
- The scanner does not provide comprehensive error handling, structured output, or safe production-grade scanning controls.
- `PortScanner` stores `banners` and `open_ports` as class attributes, so results can be shared between instances in the same Python process.

Treat output as a learning aid only. Confirm any finding with appropriate, current tools and manual verification before drawing conclusions.
