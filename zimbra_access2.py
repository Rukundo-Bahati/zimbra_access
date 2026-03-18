import hmac
import hashlib
import time
import sys

def generate_zimbra_link(account, host, key, expires=0):
    """
    Generate Zimbra pre-authentication URL
    """
    timestamp = int(time.time() * 1000)
    by = "name"
    
    # Prepare data string
    data = f"{account}|{by}|{expires}|{timestamp}"
    
    # Generate HMAC-SHA1 signature
    token = hmac.new(
        key.encode('utf-8'),
        data.encode('utf-8'),
        hashlib.sha1
    ).hexdigest()
    
    # Construct URL
    url = f"https://{host}/service/preauth?account={account}&by={by}&timestamp={timestamp}&expires={expires}&preauth={token}"
    return url, timestamp

def print_banner():
    """Print a nice banner"""
    print("=" * 70)
    print("     ZIMBRA PRE-AUTH URL GENERATOR (Authorized Use Only)")
    print("=" * 70)
    print()

def get_user_input():
    """Step-by-step user input collection"""
    
    print("Please provide the following information:\n")
    
    # Step 1: Get authentication key
    print("[Step 1/4] Authentication Key")
    print("-" * 40)
    print("NOTE: This is the pre-shared key for Zimbra pre-auth")
    key = input("Enter the pre-authentication key: ").strip()
    while not key:
        print("❌ Key cannot be empty!")
        key = input("Enter the pre-authentication key: ").strip()
    print("✅ Key accepted\n")
    
    # Step 2: Get target email
    print("[Step 2/4] Target Email Address")
    print("-" * 40)
    print("Example: user@domain.com")
    account = input("Enter the email address: ").strip()
    while not account or '@' not in account:
        if not account:
            print("❌ Email cannot be empty!")
        elif '@' not in account:
            print("❌ Invalid email format (must contain @)")
        account = input("Enter the email address: ").strip()
    print(f"✅ Email accepted: {account}\n")
    
    # Step 3: Get mail host
    print("[Step 3/4] Zimbra Mail Host")
    print("-" * 40)
    print("Example: mail.domain.com")
    default_host = "mail.fic.gov.rw"
    host_input = input(f"Enter mail host [default: {default_host}]: ").strip()
    host = host_input if host_input else default_host
    print(f"✅ Host set to: {host}\n")
    
    # Step 4: Get expiration (optional)
    print("[Step 4/4] Link Expiration (Optional)")
    print("-" * 40)
    print("Enter expiration time in seconds (0 = no expiration)")
    print("Common values: 900 (15 min), 3600 (1 hour), 0 (none)")
    expires_input = input("Enter expiration [default: 0]: ").strip()
    
    try:
        expires = int(expires_input) if expires_input else 0
    except ValueError:
        print("⚠️  Invalid number, using default: 0")
        expires = 0
    
    if expires > 0:
        print(f"✅ Link will expire after {expires} seconds ({expires/60:.1f} minutes)")
    else:
        print("✅ No expiration set (valid until timestamp becomes stale)")
    
    return key, account, host, expires

def confirm_details(key, account, host, expires):
    """Show summary and confirm"""
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Authentication Key: {'*' * 8}{key[-8:] if len(key) > 8 else '****'}")
    print(f"Target Email:       {account}")
    print(f"Mail Host:          {host}")
    print(f"Expiration:         {expires} seconds" + (" (no expiry)" if expires == 0 else f" ({expires/60:.1f} minutes)"))
    print("=" * 70)
    
    confirm = input("\nGenerate URL with these details? (yes/no): ").strip().lower()
    return confirm in ['yes', 'y', 'ye', 'yeah', 'yep']

def main():
    print_banner()
    
    # Collect information step by step
    key, account, host, expires = get_user_input()
    
    # Confirm before generating
    if not confirm_details(key, account, host, expires):
        print("\n❌ Generation cancelled by user.")
        sys.exit(0)
    
    # Generate the link
    print("\n⏳ Generating secure link...")
    try:
        link, timestamp = generate_zimbra_link(account, host, key, expires)
        
        # Display results
        print("\n" + "=" * 70)
        print("✅ SUCCESS! Pre-Auth URL Generated")
        print("=" * 70)
        print("\n📧 TARGET:", account)
        print("🔗 URL:")
        print("-" * 70)
        print(link)
        print("-" * 70)
        print("\n📋 LINK DETAILS:")
        print(f"   • Generated at: {time.ctime(timestamp/1000)}")
        print(f"   • Timestamp: {timestamp}")
        print(f"   • Expires: {'Never' if expires == 0 else f'in {expires} seconds'}")
        print(f"   • One-time use: Yes")
        print("\n⚠️  IMPORTANT NOTES:")
        print("   • This link is for authorized testing only")
        print("   • Keep this key and link secure")
        print("   • The link may expire based on server configuration")
        print("=" * 70)
        
        # Option to copy to clipboard (if pyperclip is available)
        try:
            import pyperclip
            pyperclip.copy(link)
            print("\n📋 Link copied to clipboard!")
        except ImportError:
            print("\n📋 Tip: Install 'pyperclip' for auto-copy: pip install pyperclip")
            
    except Exception as e:
        print(f"\n❌ Error generating link: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Security warning
    print("\n🔐 AUTHORIZED USE ONLY - This tool should only be used with explicit permission")
    proceed = input("Do you have authorization to use this tool? (yes/no): ").strip().lower()
    
    if proceed in ['yes', 'y']:
        main()
    else:
        print("\n❌ This tool requires proper authorization. Exiting.")
        sys.exit(0)
