# ✅ Step 1 Complete! Dependencies Installed

Great! All Python packages are installed successfully. 

---

## 🎯 Next Steps

### Step 2: Set Up Google Sheets API

**Time: ~10 minutes**

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create a Project**
   - Click "Select a project" → "New Project"
   - Name it (e.g., "FB Messages")
   - Click "Create"

3. **Enable APIs**
   - Go to "APIs & Services" → "Library"
   - Search "Google Sheets API" → Click → Enable
   - Search "Google Drive API" → Click → Enable

4. **Create Service Account**
   - Go to "APIs & Services" → "Credentials"
   - Click "+ CREATE CREDENTIALS" → "Service account"
   - Name it (e.g., "fb-sheets-service")
   - Click "Create and Continue" → "Done"

5. **Download Credentials**
   - Click on your service account name
   - Go to "Keys" tab
   - Click "Add Key" → "Create new key"
   - Choose **JSON** → Click "Create"
   - File will download automatically

6. **Save Credentials**
   - Find the downloaded file (usually in Downloads folder)
   - **Rename it to:** `credentials.json`
   - **Move it to:** `C:\Users\ACER\Desktop\FB to Sheets\credentials.json`

7. **Create Google Sheet**
   - Go to https://sheets.google.com
   - Create a new blank spreadsheet
   - Name it (e.g., "FB Messages")
   - Copy the Sheet ID from the URL:
     ```
     https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit
                                     ^^^^^^^^^^^^^^
                                     This is your Sheet ID
     ```

8. **Share Sheet with Service Account**
   - Open `credentials.json` in Notepad
   - Find this line: `"client_email": "something@project.iam.gserviceaccount.com"`
   - Copy that email address
   - Open your Google Sheet
   - Click "Share" button (top right)
   - Paste the email address
   - Make sure it has "Editor" permission
   - Uncheck "Notify people"
   - Click "Share"

**✅ Checkpoint:** You should have:
- `credentials.json` in your project folder
- Google Sheet created and shared with service account
- Sheet ID copied

---

### Step 3: Set Up Facebook App

**Time: ~10 minutes**

1. **Go to Facebook Developers**
   - Visit: https://developers.facebook.com/
   - Sign in with your Facebook account

2. **Create an App**
   - Click "My Apps" → "Create App"
   - Choose "Business" type → Click "Next"
   - Fill in:
     - **App Name:** FB Messages Automation
     - **App Contact Email:** Your email
   - Click "Create App"

3. **Skip Use Cases Dialog (if shown)**
   - When you see "Add use cases" dialog, you can:
     - **Option A:** Click "Cancel" or close it (if possible)
     - **Option B:** Just click "Next" without selecting anything
     - **Option C:** Select any generic option like "Facebook Login" just to proceed
   - **Important:** You don't need to select Messenger here - that comes next!

4. **Skip Publishing Requirements (if shown)**
   - When you see "Publishing requirements" page:
     - **Just click "Next"** - You can skip Business Verification and App Review for now
     - These are needed later when you publish your app
     - For basic Messenger/webhook functionality, you don't need them yet
     - You can complete verification later when needed

5. **Messenger is Added! ✅** You're on Messenger API Setup page!

   **I can see:**
   - Left panel: "Webhooks" link
   - Right panel: "1. Configure webhooks" section
   
   **Click on "Webhooks" (left panel) OR "1. Configure webhooks" (right panel)**

6. **Configure Webhook** ✅ You're here now!
   
   **I can see your webhook page - current URL is Make.com**
   
   **Step 1: Update Callback URL**
   - The Callback URL field currently has a Make.com URL
   - **For local testing:** You'll change this to your ngrok URL later
   - Format: `https://your-ngrok-url.ngrok.io/webhook`
   - **For now:** You can leave it temporarily, or wait until ngrok is set up
   
   **Step 2: Check Verify Token**
   - Verify Token field is already filled (shown as dots)
   - **Click in the field to see it** or keep it as is
   - **WRITE THIS DOWN!** You'll need it for `.env` as `FB_VERIFY_TOKEN`
   - If you want to change it, type a new one (e.g., `my_secure_token_123`)
   
   **Step 3: Subscribe to Events**
   - Look for "Subscribe to fields" or events section
   - Check ✅ **`messages`** (REQUIRED!)
   - Check ✅ `messaging_postbacks` (optional)
   - Make sure `messages` is checked!
   
   **Step 4: Verify and Save**
   - After checking events, click **"Verify and save"** button
   - **Note:** Verification will fail if server isn't running yet - that's OK for now
   
   **Step 5: Subscribe Your Page**
   - Look for "Add Subscriptions" or "Subscribe" section
   - Select your Facebook Page
   - Click "Subscribe"
   
   See `WEBHOOK_SETUP_GUIDE.md` for detailed instructions!

7. **Get Page Access Token:**
   - Look for "Access Tokens" section or link
   - Select your Facebook Page
   - Click "Generate Token"
   - **COPY THE TOKEN** - Save it securely!
   - Use in `.env` as `FB_PAGE_ACCESS_TOKEN`
   
   See `CONFIGURE_WEBHOOK.md` for detailed instructions!

8. **Your Server is Running! ✅** Now set up ngrok:
   
   **Server Status:**
   - ✅ Google Sheets client initialized
   - ✅ Flask server running on http://127.0.0.1:5000
   - **KEEP THIS TERMINAL OPEN!**
   
   **Step 1: Open a NEW Terminal Window**
   - Don't close the server terminal
   - Open a new PowerShell window
   
   **Step 2: Install ngrok (if not installed)**
   - Download from: https://ngrok.com/download
   - Extract `.exe` to a folder (e.g., `C:\ngrok\`)
   
   **Step 3: Set Up ngrok Account (Required!)**
   - Sign up (free): https://dashboard.ngrok.com/signup
   - Get authtoken: https://dashboard.ngrok.com/get-started/your-authtoken
   - Configure ngrok: `ngrok config add-authtoken YOUR_AUTHTOKEN`
   
   **Step 4: Start ngrok**
   - Navigate to ngrok folder: `cd C:\ngrok`
   - Run: `ngrok http 5000`
   - **Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)
   - **KEEP THIS TERMINAL OPEN TOO!**
   
   See `SETUP_NGROK_AUTH.md` for detailed instructions!
   
   **Step 5: Update Webhook URL in Facebook** ⚠️ NEEDS UPDATE!
   - ⚠️ Callback URL is still Make.com URL!
   - **CHANGE IT TO:** `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook`
   - Delete Make.com URL and enter your ngrok URL
   - Verify Token: Check it's `fb-messages` (or set it to `fb-messages`)
   
   **Step 6: Add Verify Token** ✅ DO THIS FIRST!
   - Verify Token field is empty - you need to fill it!
   - Type any token (e.g., `my_secure_token_123`)
   - **IMPORTANT:** Write this down! You'll need it for `.env` file
   - Make sure it matches what you put in `.env` as `FB_VERIFY_TOKEN`
   
   **Step 7: Fix `.env` File Error** ⚠️ IMPORTANT!
   - **ERROR FOUND:** Your `.env` has `FB_VERIFY_TOKEN=FB_VERIFY_TOKEN=fb-messages` (duplicate!)
   - **FIX IT TO:** `FB_VERIFY_TOKEN=fb-messages` (remove duplicate!)
   - Make sure you're editing `.env` file (NOT `config_example.env`)
   - Save the file
   - Restart server (`Ctrl+C`, then `python app.py`)
   - See `FIX_ENV_FILE_ERROR.md` for details!
   
   **Step 8: Verify and Save** ✅ SUCCESS!
   - ✅ Webhook verified successfully! (ngrok shows: `GET /webhook 200 OK`)
   - ✅ Facebook successfully verified your webhook!
   - **Now in Facebook:** Subscribe to fields and your Page
   - See `AFTER_VERIFICATION_SUCCESS.md` for next steps!
   
   **Step 9: Subscribe to Fields** ✅ DONE!
   - ✅ `messages` field subscribed (blue toggle, "Subscribed")
   - ✅ Webhook fields table populated
   - **Next:** Subscribe your Page!
   
   **Step 9.5: Subscribe Your Page** ❌ MISSING STEP!
   - ❌ **PROBLEM:** Nothing happening because Page is NOT subscribed!
   - ⚠️ This is DIFFERENT from subscribing to fields!
   - **Find "Page Subscriptions" or "Add Subscriptions" section**
   - **Subscribe your Page** to the webhook
   - **Select `messages` events** for your Page
   - **Click "Subscribe"** or "Save"
   - **Your Page should appear in "Subscribed Pages" table**
   - **This is required for Facebook to send webhook events!**
   - See `SUBSCRIBE_PAGE_FIX.md` for detailed instructions!
   
   **Step 10: Test It Now!** ✅ READY TO TEST!
   - ✅ `.env` file configured with Google Sheet ID! ✅
   - ✅ `GOOGLE_SHEET_ID=1UKxylEP4Mp2grH_-ikbYK5fd4Cotxayd5F8K54gEfJM` ✅
   - ⚠️ `FB_PAGE_ACCESS_TOKEN` is optional - can add later
   - **CRITICAL:** Subscribe your Page first! (Step 9.5 above)
   - **Step 1:** Restart server (`Ctrl+C`, then `python app.py`)
   - **Step 2:** Make sure both server and ngrok are running
   - **Step 3:** Send test message to your Facebook Page
   - **Step 4:** Check Google Sheet - message should appear automatically!
   - **If it works:** Setup is COMPLETE! 🎉
   - See `READY_TO_TEST.md` for complete guide!
   
   See `ADD_VERIFY_TOKEN.md` for detailed instructions!
   
   **Step 6: Get Page Access Token**
   - Look for "Access Tokens" section
   - Select your Page → Generate Token
   - COPY THE TOKEN - Save for `.env` as `FB_PAGE_ACCESS_TOKEN`
   
   **Step 7: Configure `.env` file**
   - Copy: `copy config_example.env .env`
   - Edit `.env` and add:
     - `FB_VERIFY_TOKEN=your_token_from_facebook`
     - `FB_PAGE_ACCESS_TOKEN=your_page_token`
     - `GOOGLE_SHEET_ID=your_sheet_id`
   
   **Step 8: Restart Server**
   - Press `Ctrl+C` in server terminal
   - Run: `python app.py` again
   
   **Step 9: Test!**
   - Send a message to your Facebook Page
   - Check Google Sheet - message should appear!
   
   See `FINAL_WEBHOOK_SETUP.md` for complete instructions!

**✅ Checkpoint:** You should have:
- Facebook App created
- Messenger product added
- Page Access Token copied

---

### Step 4: Configure Environment Variables

**Time: ~2 minutes**

1. **Create `.env` file**
   ```powershell
   copy config_example.env .env
   ```

2. **Edit `.env` file**
   - Open `.env` in Notepad
   - Fill in these values:
   
   ```env
   FB_VERIFY_TOKEN=my_secure_token_123
   FB_PAGE_ACCESS_TOKEN=paste_your_page_token_here
   GOOGLE_SHEET_ID=paste_your_sheet_id_here
   ```

   **Where to get each:**
   - `FB_VERIFY_TOKEN`: Any random string (e.g., `my_secure_token_123`)
   - `FB_PAGE_ACCESS_TOKEN`: From Step 3 (Facebook Page Token)
   - `GOOGLE_SHEET_ID`: From Step 2 (Google Sheet ID)

3. **Save the file**

---

### Step 5: Test Your Setup

**Time: ~2 minutes**

Run the test script:

```powershell
python test_setup.py
```

This will check if everything is configured correctly.

---

### Step 6: Start Your Server

**Time: ~1 minute**

```powershell
python app.py
```

You should see:
```
Google Sheets client initialized successfully
 * Running on http://0.0.0.0:5000
```

Keep this window open!

---

### Step 7: Set Up Webhook (with ngrok)

**Time: ~5 minutes**

1. **Open a NEW PowerShell window** (keep the server running)

2. **Navigate to ngrok folder** (or use full path):
   ```powershell
   cd C:\ngrok
   ngrok http 5000
   ```
   
   Or if ngrok is in PATH:
   ```powershell
   ngrok http 5000
   ```

3. **Copy the HTTPS URL** - You'll see something like:
   ```
   Forwarding    https://abc123xyz.ngrok.io -> http://localhost:5000
   ```
   Copy the `https://abc123xyz.ngrok.io` part

4. **Configure Facebook Webhook**
   - Go back to Facebook Developers → Your App → Messenger
   - Scroll to "Webhooks" section
   - Click "Add Callback URL"
   - Enter:
     - **Callback URL:** `https://your-ngrok-url.ngrok.io/webhook`
       (Replace with your actual ngrok URL)
     - **Verify Token:** `my_secure_token_123`
       (Same as `FB_VERIFY_TOKEN` in your `.env` file)
     - Check **"messages"** checkbox
   - Click "Verify and Save"
   - Click "Add Subscriptions" → Select your Page → "Subscribe"

**✅ Checkpoint:** Webhook should be verified and subscribed!

---

### Step 8: Test with Real Message

1. Open your Facebook Page
2. Send a test message to your page (from another account or test feature)
3. Check your Google Sheet - message should appear automatically! 🎉

---

## 🔧 Quick Reference

**Current Status:**
- ✅ Python dependencies installed
- ⏳ Google Sheets API setup needed
- ⏳ Facebook App setup needed
- ⏳ Environment variables needed
- ⏳ Webhook configuration needed

**Files You'll Create:**
- `credentials.json` (from Google Cloud)
- `.env` (copy from `config_example.env`)

**You'll Need:**
- Google account
- Facebook account with a Page
- About 30 more minutes

---

## 🚨 Having Issues?

- **Can't find Google Cloud Console?** → Use: https://console.cloud.google.com/
- **Can't find Facebook Developers?** → Use: https://developers.facebook.com/
- **Not sure about Sheet ID?** → It's in the URL between `/d/` and `/edit`
- **Need more help?** → Check `SETUP_GUIDE.md` for detailed instructions

---

**Ready for Step 2?** → Set up Google Sheets API! 📊

