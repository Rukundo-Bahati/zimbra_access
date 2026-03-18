Zimbra Pre-Auth URL Generator


A secure, interactive tool for generating Zimbra Collaboration Suite pre-authentication URLs for authorized testing and administrative purposes.

📋 Table of Contents
Overview

Features

Prerequisites

Installation

Usage

Interactive Walkthrough

Security Considerations

Troubleshooting

Legal Notice

🔍 Overview
This tool generates pre-authentication URLs for Zimbra mail servers, allowing authorized users to create single-use, time-limited access links. It implements Zimbra's preauth authentication mechanism using HMAC-SHA1 signatures.

✨ Features
Interactive Step-by-Step Wizard - Guided input collection

Input Validation - Ensures correct email format and required fields

Secure Key Handling - Masks sensitive keys in confirmation screen

Clipboard Integration - Auto-copy generated URLs (optional)

Expiration Control - Set custom link expiration times

Comprehensive Output - Detailed link information and metadata

Authorization Confirmation - Built-in security acknowledgment

📦 Prerequisites
Python 3.6 or higher

No external dependencies required (standard library only)

Optional: pyperclip for clipboard functionality

🚀 Installation
Clone or download the script:

bash
wget https://path-to-script/zimbra_access2.py
# or
curl -O https://path-to-script/zimbra_access2.py
Make it executable (Linux/Mac):

bash
chmod +x zimbra_access2.py
Optional: Install clipboard support:

bash
pip install pyperclip
💻 Usage
Basic Execution
bash
python3 zimbra_access2.py
Command Flow
The script guides you through four simple steps:

Authentication Key - Enter your pre-shared key

Target Email - Specify the email address

Mail Host - Set the Zimbra server (with default)

Expiration - Configure link lifetime (optional)

Example Session
bash
$ python3 zimbra_access2.py

🔐 AUTHORIZED USE ONLY - This tool should only be used with explicit permission
Do you have authorization to use this tool? (yes/no): yes

==========================================
     ZIMBRA PRE-AUTH URL GENERATOR
==========================================

[Step 1/4] Authentication Key
----------------------------------------
Enter the pre-authentication key: ********************************

[Step 2/4] Target Email Address
----------------------------------------
Enter the email address: admin@example.com
📝 Interactive Walkthrough
Step 1: Authentication Key
Enter the pre-shared key configured in your Zimbra server

This is sensitive - it will be masked in the confirmation screen

Cannot be empty

Step 2: Target Email
Enter the full email address of the target user

Must include @ domain

Example: user@company.com

Step 3: Mail Host
Enter the Zimbra server hostname

Default: mail.fic.gov.rw (configurable)

Example: mail.yourcompany.com

Step 4: Expiration (Optional)
Set link expiration in seconds

Common values:

900 - 15 minutes (recommended)

3600 - 1 hour

0 - No expiration (use cautiously)

Confirmation
Review your settings before generation:

Authentication Key: ********f7 (last 8 chars shown)

Target Email: user@example.com

Mail Host: mail.example.com

Expiration: 900 seconds (15.0 minutes)

🔒 Security Considerations
⚠️ Important Security Notes
Authorization Required - This tool is for authorized use only

Key Protection - Never share or commit the authentication key

Link Security - Generated URLs are sensitive and should be:

Transmitted securely (encrypted channels)

Used immediately

Not logged or stored in plaintext

Expiration - Always set appropriate expiration times

Audit Trail - Maintain logs of generated links for compliance

Best Practices
Use short expiration times (15-30 minutes)

Regenerate pre-auth keys periodically

Monitor pre-auth usage in Zimbra logs

Implement IP restrictions where possible

🛠️ Troubleshooting
Common Issues
Issue	Solution
"Key cannot be empty"	Enter a valid pre-shared key
"Invalid email format"	Ensure email contains @ symbol
Link not working	Check hostname, key validity, timestamp sync
"Module not found"	Install pyperclip: pip install pyperclip
Error Messages
"Key cannot be empty!" - Authentication key is required

"Invalid email format" - Email must include domain (user@domain.com)

"Error generating link" - Check network connectivity and parameters

📄 Technical Details
URL Structure
text
https://{host}/service/preauth?account={email}&by=name&timestamp={ms}&expires={seconds}&preauth={token}
Components
account: Target email address

by: Authentication method ("name")

timestamp: Current time in milliseconds

expires: Link validity period (seconds)

preauth: HMAC-SHA1 signature

Signature Generation
python
data = f"{account}|name|{expires}|{timestamp}"
token = hmac.new(key.encode(), data.encode(), hashlib.sha1).hexdigest()
⚖️ Legal Notice
text
THIS SOFTWARE IS PROVIDED FOR AUTHORIZED SECURITY TESTING AND 
ADMINISTRATIVE PURPOSES ONLY.

Unauthorized access to computer systems is illegal and unethical. 
Users of this tool must:

1. Obtain explicit written permission before testing
2. Comply with all applicable laws and regulations
3. Respect privacy and data protection requirements
4. Use only within the scope of authorization
5. Report any discovered vulnerabilities responsibly

The developers assume no liability for misuse of this tool.
🤝 Contributing
Contributions are welcome! Please ensure:

Code follows PEP 8 guidelines

Security features remain intact

Documentation is updated

Changes are tested

📧 Support
For issues or questions:

Check Troubleshooting section

Review Zimbra documentation

Contact your system administrator

📚 Version History
v2.0 - Interactive wizard, enhanced security, clipboard support

v1.0 - Basic command-line URL generation

Remember: With great power comes great responsibility. Use this tool ethically and legally.
