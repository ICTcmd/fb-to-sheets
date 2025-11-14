"""
Setup verification script
Run this to test if your configuration is correct before starting the webhook server.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_environment_variables():
    """Test if all required environment variables are set."""
    print("🔍 Checking environment variables...")
    
    required_vars = {
        'FB_VERIFY_TOKEN': 'Facebook webhook verification token',
        'GOOGLE_SHEET_ID': 'Google Sheet ID',
    }
    
    optional_vars = {
        'GOOGLE_SHEET_NAME': 'Google Sheet name (default: Messages)',
        'GOOGLE_CREDENTIALS_FILE': 'Google credentials file path (default: credentials.json)',
        'EXCEL_EXPORT_ENABLED': 'Excel export enabled (optional)',
        'EXCEL_FILENAME': 'Excel filename (optional)',
    }
    
    missing = []
    for var, description in required_vars.items():
        value = os.environ.get(var)
        if not value or value.startswith('your_') or value == '':
            print(f"  ❌ {var}: NOT SET - {description}")
            missing.append(var)
        else:
            print(f"  ✅ {var}: Set")
    
    for var, description in optional_vars.items():
        value = os.environ.get(var)
        if value and not value.startswith('your_'):
            print(f"  ✅ {var}: {value}")
        else:
            print(f"  ⚠️  {var}: Using default - {description}")
    
    return len(missing) == 0

def test_google_credentials():
    """Test if Google credentials file exists and is valid."""
    print("\n🔍 Checking Google credentials...")
    
    creds_file = os.environ.get('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
    
    if not os.path.exists(creds_file):
        print(f"  ❌ Credentials file not found: {creds_file}")
        print("     Please download your service account credentials and save as credentials.json")
        return False
    
    print(f"  ✅ Credentials file found: {creds_file}")
    
    # Try to load credentials
    try:
        from google.oauth2.service_account import Credentials
        import gspread
        
        SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file"
        ]
        
        creds = Credentials.from_service_account_file(creds_file, scopes=SCOPE)
        client = gspread.authorize(creds)
        
        # Try to access the sheet
        sheet_id = os.environ.get('GOOGLE_SHEET_ID', '')
        if sheet_id and not sheet_id.startswith('your_'):
            try:
                spreadsheet = client.open_by_key(sheet_id)
                print(f"  ✅ Google Sheet access: SUCCESS")
                print(f"     Sheet title: {spreadsheet.title}")
                return True
            except Exception as e:
                print(f"  ⚠️  Google Sheet access: FAILED")
                print(f"     Error: {str(e)}")
                print(f"     Make sure the sheet ID is correct and the service account has access")
                return False
        else:
            print(f"  ⚠️  Google Sheet ID not set - cannot test sheet access")
            print(f"  ✅ Google credentials are valid")
            return True
            
    except Exception as e:
        print(f"  ❌ Error loading credentials: {str(e)}")
        return False

def test_python_dependencies():
    """Test if all required Python packages are installed."""
    print("\n🔍 Checking Python dependencies...")
    
    required_packages = {
        'flask': 'flask',
        'gspread': 'gspread',
        'google.auth': 'google.auth',
        'openpyxl': 'openpyxl',
        'dotenv': 'dotenv'
    }
    
    missing = []
    for package_name, import_name in required_packages.items():
        try:
            if '.' in import_name:
                # Handle packages with dots (like google.auth)
                parts = import_name.split('.')
                mod = __import__(import_name, fromlist=[parts[-1]])
            else:
                __import__(import_name)
            print(f"  ✅ {package_name}: Installed")
        except ImportError:
            print(f"  ❌ {package_name}: NOT INSTALLED")
            missing.append(package_name)
    
    if missing:
        print(f"\n  📦 Install missing packages: pip install {' '.join(missing)}")
        return False
    
    return True

def main():
    """Run all tests."""
    print("=" * 60)
    print("Facebook to Google Sheets - Setup Verification")
    print("=" * 60)
    
    tests = [
        ("Python Dependencies", test_python_dependencies),
        ("Environment Variables", test_environment_variables),
        ("Google Credentials", test_google_credentials),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n  ❌ Error running {name} test: {str(e)}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All tests passed! You're ready to run the webhook server.")
        print("   Start the server with: python app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above before starting the server.")
        sys.exit(1)

if __name__ == '__main__':
    main()

