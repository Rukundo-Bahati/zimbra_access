# Zimbra Pre-Auth URL Generator

A secure, interactive tool for generating Zimbra Collaboration Suite pre-authentication URLs for authorized testing and administrative purposes.

---

## Table of Contents

* Overview
* Features
* Prerequisites
* Installation
* Usage
* Interactive Walkthrough
* Security Considerations
* Troubleshooting
* Technical Details
* Legal Notice
* Contributing
* Support
* Version History

---

## Overview

This tool generates pre-authentication URLs for Zimbra mail servers, allowing authorized users to create single-use, time-limited access links. It implements Zimbra's pre-authentication mechanism using HMAC-SHA1 signatures.

---

## Features

* Interactive step-by-step wizard for guided input
* Input validation for email format and required fields
* Secure key handling with masked display
* Optional clipboard integration
* Custom expiration control for generated links
* Detailed output with metadata
* Built-in authorization confirmation

---

## Prerequisites

* Python 3.6 or higher
* No external dependencies required (standard library only)
* Optional: `pyperclip` for clipboard functionality

---

## Installation

### Download the Script

```bash
wget https://path-to-script/zimbra_access2.py
# or
curl -O https://path-to-script/zimbra_access2.py
```

### Make Executable (Linux/Mac)

```bash
chmod +x zimbra_access2.py
```

### Optional: Install Clipboard Support

```bash
pip install pyperclip
```

---

## Usage

### Run the Script

```bash
python3 zimbra_access2.py
```

### Workflow

The script guides you through four steps:

1. Enter authentication key
2. Enter target email
3. Enter mail host (default provided)
4. Set expiration time (optional)

---

## Interactive Walkthrough

### Step 1: Authentication Key

* Enter the pre-shared key configured on your Zimbra server
* This field is required
* The key is masked for security

### Step 2: Target Email

* Enter a valid email address (e.g., [user@company.com](mailto:user@company.com))
* Must include "@" and domain

### Step 3: Mail Host

* Enter the Zimbra server hostname
* Example: mail.yourcompany.com
* Default value may be provided

### Step 4: Expiration (Optional)

Set link expiration in seconds:

* 900 (15 minutes, recommended)
* 3600 (1 hour)
* 0 (no expiration — use cautiously)

### Confirmation

Before generation, review:

* Masked authentication key
* Target email
* Mail host
* Expiration duration

---

## Security Considerations

### Important Notes

* Use only with proper authorization
* Never share or expose authentication keys
* Treat generated URLs as sensitive data

### Best Practices

* Use short expiration times (15–30 minutes)
* Transmit links securely (encrypted channels)
* Avoid logging or storing links in plaintext
* Rotate pre-authentication keys regularly
* Monitor usage in server logs
* Apply IP restrictions where possible

---

## Troubleshooting

### Common Issues

| Issue                | Solution                          |
| -------------------- | --------------------------------- |
| Key cannot be empty  | Provide a valid key               |
| Invalid email format | Ensure email includes @domain     |
| Link not working     | Verify host, key, and system time |
| Module not found     | Install pyperclip                 |

### Error Messages

* "Key cannot be empty" — authentication key required
* "Invalid email format" — incorrect email structure
* "Error generating link" — check inputs and connectivity

---

## Technical Details

### URL Structure

```
https://{host}/service/preauth?account={email}&by=name&timestamp={ms}&expires={seconds}&preauth={token}
```

### Components

* `account`: target email
* `by`: authentication method (name)
* `timestamp`: current time in milliseconds
* `expires`: validity duration in seconds
* `preauth`: HMAC-SHA1 signature

### Signature Generation

```python
data = f"{account}|name|{expires}|{timestamp}"
token = hmac.new(key.encode(), data.encode(), hashlib.sha1).hexdigest()
```

---

## Legal Notice

This software is intended for authorized security testing and administrative use only.

Users must:

1. Obtain explicit permission before use
2. Follow applicable laws and regulations
3. Respect privacy and data protection standards
4. Operate within approved scope
5. Report vulnerabilities responsibly

The developers assume no liability for misuse.

---

## Contributing

Contributions are welcome. Please ensure:

* Code follows PEP 8 standards
* Security features remain intact
* Documentation is updated
* Changes are tested

---

## Support

* Review the troubleshooting section
* Consult official Zimbra documentation
* Contact your system administrator

---

## Version History

* v2.0 — Interactive wizard, enhanced security, clipboard support
* v1.0 — Basic command-line URL generation

---

Use this tool responsibly and ethically.
