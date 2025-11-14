# Use Your Service Account Key! 🔑

## ✅ You've Created the Service Account Key!

**You're looking at:**
- Service account: `fb-sheets-service`
- Key ID: `e928f0ff25004e2c1b0218dcb79c18d63f6e4e8a`
- Status: Active ✅

---

## Step 1: Download the Key File

**From the page you're on (Google Cloud Console):**

1. **Look for the key you just created** in the table
   - Type: Gear icon (JSON key)
   - Status: Active (green checkmark)
   - Key ID: `e928f0ff25004e2c1b0218dcb79c18d63f6e4e8a`

2. **Click on the key** (or find a download button):
   - Some versions: Click the **three dots menu (⋮)** → **"Download"**
   - Or: Click directly on the key row to download
   - Or: Look for **"Download"** or **"Create key"** button

3. **The key will download as a JSON file:**
   - Filename will be something like: `fb-sheets-service-xxxxx-xxxxx.json`
   - Or: `[project-name]-[random-id].json`

---

## Step 2: Save as `credentials.json`

**After downloading:**

1. **Find the downloaded file** in your Downloads folder
   - Usually: `C:\Users\ACER\Downloads\[filename].json`

2. **Rename it to:** `credentials.json`
   - Right-click → **Rename**
   - Change the name to exactly: `credentials.json`

3. **Move it to your project folder:**
   ```
   C:\Users\ACER\Desktop\FB to Sheets\credentials.json
   ```
   - Cut the file from Downloads
   - Paste it into: `C:\Users\ACER\Desktop\FB to Sheets\`

---

## Step 3: Verify `.env` File

**Your `.env` file should have:**
```env
GOOGLE_CREDENTIALS_FILE=credentials.json
```

**Check your `.env` file:**
- If it's already there ✅, you're good!
- If not, add this line to your `.env` file

---

## Step 4: Share Google Sheet with Service Account

**Important! The service account needs access to your Google Sheet:**

1. **Get the service account email:**
   - Open `credentials.json` in Notepad
   - Look for `"client_email"` field
   - Copy the email (looks like: `fb-sheets-service@[project].iam.gserviceaccount.com`)

2. **Share your Google Sheet with that email:**
   - Open your Google Sheet: https://docs.google.com/spreadsheets/d/1UKxylEP4Mp2grH_-ikbYK5fd4Cotxayd5F8K54gEfJM/edit
   - Click **"Share"** button (top right)
   - Paste the service account email
   - Give it **"Editor"** permissions
   - Click **"Send"**

---

## Step 5: Restart Server

**After placing `credentials.json` in project folder:**

1. **Stop your server** (Terminal 1):
   - Press `Ctrl+C`

2. **Restart it:**
   ```powershell
   python app.py
   ```

3. **You should see:**
   ```
   INFO:__main__:Google Sheets client initialized successfully
   ```

**If you see this, the credentials are working! ✅**

---

## Quick Checklist:

- [ ] Downloaded JSON key file from Google Cloud
- [ ] Renamed file to `credentials.json`
- [ ] Moved `credentials.json` to project folder (`C:\Users\ACER\Desktop\FB to Sheets\`)
- [ ] Checked `.env` has `GOOGLE_CREDENTIALS_FILE=credentials.json`
- [ ] Opened `credentials.json` and copied `client_email`
- [ ] Shared Google Sheet with service account email (Editor access)
- [ ] Restarted server
- [ ] Server shows "Google Sheets client initialized successfully"

---

## Where It's Used:

**The `credentials.json` file is used by:**

1. **`app.py`** (line 38-45):
   - Loads credentials when starting the server
   - Uses it to authenticate with Google Sheets API
   - Saves messages to your Google Sheet

2. **Your `.env` file**:
   - `GOOGLE_CREDENTIALS_FILE=credentials.json` tells the app where to find it

---

## File Structure:

**Your project folder should look like:**
```
C:\Users\ACER\Desktop\FB to Sheets\
├── app.py
├── credentials.json          ← YOUR KEY FILE GOES HERE!
├── .env
├── config_example.env
├── requirements.txt
└── ... (other files)
```

---

## Most Important Steps:

1. **Download the key** from Google Cloud Console
2. **Rename to `credentials.json`**
3. **Place in project folder**
4. **Share Google Sheet with service account email**
5. **Restart server**

---

**Download the key file, rename it to `credentials.json`, and place it in your project folder!** 🚀

