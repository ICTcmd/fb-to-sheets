# Complete Setup Guide
## Facebook Page Messages to Google Sheets

Follow these steps in order to set up your automation system.

---

## Step 1: Install Python (if not installed)

1. Download Python 3.7 or higher from [python.org](https://www.python.org/downloads/)
2. During installation, check **"Add Python to PATH"**
3. Verify installation by opening Command Prompt/PowerShell:
   ```bash
   python --version
   ```
   Should show Python 3.7 or higher.

---

## Step 2: Install Project Dependencies

1. Open Command Prompt/PowerShell in your project folder:
   ```bash
   cd "C:\Users\ACER\Desktop\FB to Sheets"
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   - Flask (web server)
   - gspread (Google Sheets API)
   - google-auth (Google authentication)
   - openpyxl (Excel export)
   - python-dotenv (environment variables)
   - requests (HTTP requests)

---

## Step 3: Set Up Google Sheets API

### 3.1 Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Click **"Select a project"** → **"New Project"**
4. Name it (e.g., "FB Messages Project")
5. Click **"Create"**

### 3.2 Enable APIs

1. In the left menu, go to **"APIs & Services"** → **"Library"**
2. Search for **"Google Sheets API"** → Click it → Click **"Enable"**
3. Go back to Library
4. Search for **"Google Drive API"** → Click it → Click **"Enable"**

### 3.3 Create Service Account

1. Go to **"APIs & Services"** → **"Credentials"**
2. Click **"+ CREATE CREDENTIALS"** → **"Service account"**
3. Name it (e.g., "fb-sheets-service")
4. Click **"Create and Continue"**
5. Skip optional steps (click **"Continue"** then **"Done"**)

### 3.4 Download Credentials

1. Click on the service account you just created
2. Go to **"Keys"** tab
3. Click **"Add Key"** → **"Create new key"**
4. Choose **JSON** format
5. Click **"Create"** - A file will download automatically

### 3.5 Save Credentials

1. **Rename** the downloaded file to `credentials.json`
2. **Move** it to your project folder:
   ```
   C:\Users\ACER\Desktop\FB to Sheets\credentials.json
   ```

### 3.6 Create Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new blank spreadsheet
3. Name it (e.g., "FB Messages")
4. **Copy the Sheet ID** from the URL:
   ```
   https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit
                                 ^^^^^^^^^^^^^^
                                 This is your Sheet ID
   ```

### 3.7 Share Sheet with Service Account

1. Open your Google Sheet
2. Click **"Share"** button (top right)
3. Get the service account email from `credentials.json`:
   - Open `credentials.json` in Notepad
   - Find `"client_email": "something@project.iam.gserviceaccount.com"`
   - Copy that email
4. Paste the email in the Share dialog
5. Make sure it has **"Editor"** permission
6. Uncheck **"Notify people"**
7. Click **"Share"**

---

## Step 4: Set Up Facebook App and Webhook

### 4.1 Create Facebook App

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Click **"My Apps"** → **"Create App"**
3. Choose **"Business"** type → Click **"Next"**
4. Fill in:
   - **App Name**: FB Messages Automation (or any name)
   - **App Contact Email**: Your email
5. Click **"Create App"**

### 4.2 Add Messenger Product

1. In your app dashboard, find **"Messenger"** in the left menu
2. Click **"Messenger"** → Click **"Set Up"**
3. You'll see Messenger settings page

### 4.3 Generate Page Access Token

1. In Messenger settings, scroll to **"Access Tokens"** section
2. Under **"Generate Token"**, select your Facebook Page
3. Click **"Generate Token"**
4. **Copy the token** - you'll need it later!
5. (Keep this page open or save the token securely)

### 4.4 Set Up Webhook (Local Testing with ngrok)

#### Install ngrok:

1. Download ngrok from [ngrok.com/download](https://ngrok.com/download)
2. Extract the `.exe` file to a folder (e.g., `C:\ngrok\`)
3. You can add it to PATH or use the full path

#### Start your webhook server (in one terminal):

```bash
cd "C:\Users\ACER\Desktop\FB to Sheets"
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

#### Start ngrok (in another terminal):

```bash
ngrok http 5000
```

You'll see something like:
```
Forwarding    https://abc123xyz.ngrok.io -> http://localhost:5000
```

**Copy the HTTPS URL** (e.g., `https://abc123xyz.ngrok.io`)

#### Configure Webhook in Facebook:

1. Go back to Facebook Developers → Your App → Messenger
2. Scroll to **"Webhooks"** section
3. Click **"Add Callback URL"**
4. Enter:
   - **Callback URL**: `https://your-ngrok-url.ngrok.io/webhook`
     (Replace with your actual ngrok URL)
   - **Verify Token**: `my_secure_token_123` (or any random string)
   - Check **"messages"** checkbox
5. Click **"Verify and Save"**
6. Click **"Add Subscriptions"** → Select your Page → Click **"Subscribe"**

---

## Step 5: Configure Environment Variables

### 5.1 Create .env File

1. In your project folder, copy the example file:
   ```bash
   copy config_example.env .env
   ```
   
   (On Mac/Linux: `cp config_example.env .env`)

2. Open `.env` file in Notepad

### 5.2 Fill in Your Values

Replace the placeholder values:

```env
# Facebook Webhook Configuration
FB_VERIFY_TOKEN=my_secure_token_123
FB_PAGE_ACCESS_TOKEN=your_page_access_token_paste_here

# Google Sheets Configuration
GOOGLE_SHEET_ID=your_google_sheet_id_paste_here
GOOGLE_SHEET_NAME=Messages
GOOGLE_CREDENTIALS_FILE=credentials.json

# Excel Export Configuration (Optional)
EXCEL_EXPORT_ENABLED=false
EXCEL_FILENAME=fb_messages.xlsx

# Server Configuration
PORT=5000
```

**Where to find each value:**

- `FB_VERIFY_TOKEN`: The same token you used in Facebook webhook (e.g., `my_secure_token_123`)
- `FB_PAGE_ACCESS_TOKEN`: From Step 4.3 (Facebook Page Access Token)
- `GOOGLE_SHEET_ID`: From Step 3.6 (the ID from your Google Sheet URL)
- `GOOGLE_SHEET_NAME`: Keep as `Messages` or change if needed
- Others: Keep as default for now

### 5.3 Save the .env file

---

## Step 6: Test Your Setup

### 6.1 Run Setup Verification

```bash
python test_setup.py
```

This checks:
- ✅ Python packages installed
- ✅ Environment variables set
- ✅ Google credentials valid
- ✅ Google Sheet accessible

Fix any errors before proceeding.

### 6.2 Start the Server

```bash
python app.py
```

You should see:
```
Google Sheets client initialized successfully
 * Running on http://0.0.0.0:5000
```

### 6.3 Keep ngrok Running

Make sure ngrok is still running (from Step 4.4):
```bash
ngrok http 5000
```

**Note**: ngrok URL changes each time you restart it (unless you have a paid account). If it changes, update your Facebook webhook URL!

---

## Step 7: Test with a Real Message

1. Open your Facebook Page (the one you connected)
2. Send a test message to the page (from another account or using the test feature)
3. Example message:
   ```
   Hi ako si John Doe, taga purok calubihan barangay sampinit
   Contact: 09914567842
   ```
4. Check your Google Sheet - the message should appear automatically!
5. Check the terminal where `app.py` is running - you should see logs

---

## Troubleshooting

### "Webhook verification failed"
- Make sure `FB_VERIFY_TOKEN` in `.env` matches the token in Facebook webhook settings
- Restart your server after changing `.env`

### "Google Sheets client not initialized"
- Check that `credentials.json` is in the project folder
- Verify the service account email has access to your Google Sheet

### "Messages not appearing in Sheets"
- Check server logs for errors
- Verify `GOOGLE_SHEET_ID` is correct
- Make sure ngrok is running and URL matches Facebook webhook
- Check Facebook App Dashboard → Webhooks → View logs

### "Cannot fetch sender name"
- Verify `FB_PAGE_ACCESS_TOKEN` is set correctly
- The name will fall back to extracting from message or show "User"

### ngrok URL keeps changing
- Free ngrok URLs change each restart
- Either:
  - Keep ngrok running continuously, OR
  - Get a paid ngrok account for a static URL, OR
  - Deploy to a permanent hosting service (Heroku, etc.)

---

## For Production (When Ready)

Instead of ngrok, deploy to:
- **Heroku** (free tier available)
- **AWS Lambda**
- **Google Cloud Run**
- **DigitalOcean App Platform**
- **Railway.app**

Update your Facebook webhook URL to your production server URL.

---

## Quick Reference

**Start the server:**
```bash
python app.py
```

**Start ngrok (in separate terminal):**
```bash
ngrok http 5000
```

**Test setup:**
```bash
python test_setup.py
```

**Check server health:**
Visit: `http://localhost:5000/health`

---

## Need Help?

1. Check server logs for error messages
2. Run `python test_setup.py` to verify configuration
3. Check Facebook App Dashboard → Webhooks → View logs
4. Verify all environment variables in `.env` file

---

**You're all set!** 🎉

Once everything is working, messages sent to your Facebook Page will automatically appear in your Google Sheet with all the parsed information!

