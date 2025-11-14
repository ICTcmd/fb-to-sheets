# Final Steps - Almost Done! ✅

## ✅ You've Subscribed to `messages` Field!

**Status:**
- ✅ Webhook verified successfully
- ✅ `messages` field subscribed (blue toggle, "Subscribed")
- ✅ Webhook fields table populated

**You're almost done! Just a few more steps:**

---

## Step 1: Subscribe Your Page

**You need to subscribe your Facebook Page to receive messages:**

1. **Look for "Add Subscriptions" or "Subscribe" section**
   - This might be below the webhook fields table
   - Or in a separate section
   - Or you might need to click on your Page in the "Manage Pages" dropdown

2. **Select your Facebook Page** from dropdown
   - Use "Manage Pages" dropdown at the top if available
   - Or look for a Page selection dropdown

3. **Click "Subscribe" button**

4. **You should see your Page listed as subscribed**

---

## Step 2: Get Page Access Token

**Now get your Page Access Token (required for fetching sender names):**

1. **Look for "Access Tokens" section**
   - Might be on the same page
   - Or click "Permissions and features" in left sidebar
   - Or look for a separate "Access Tokens" link/button

2. **Alternative: Check if token is already visible**
   - Some pages show the token right in the webhook section
   - Look around the page for token information

3. **Find "Generate Token" or "Access Tokens" button**

4. **Select your Facebook Page** from dropdown

5. **Click "Generate Token"**

6. **COPY THE TOKEN** - It's a long string (starts with something like `EAAB...`)
   - Save it securely (copy to Notepad temporarily)
   - You'll need it for `.env` file as `FB_PAGE_ACCESS_TOKEN`

---

## Step 3: Get Google Sheet ID

**You need your Google Sheet ID:**

1. **Open your Google Sheet** (the one you shared with the service account)

2. **Look at the URL** in your browser:
   ```
   https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit
   ```

3. **Copy the `SHEET_ID_HERE` part**
   - It's the long string between `/d/` and `/edit`
   - Example: `1abc123xyz456def789...`

4. **Save it** - You'll need it for `.env` file

---

## Step 4: Update `.env` File

**After getting Page Access Token and Sheet ID:**

1. **Open `.env` file** in Notepad

2. **Update these lines:**
   ```env
   # Facebook Webhook Configuration
   FB_VERIFY_TOKEN=fb-messages
   FB_PAGE_ACCESS_TOKEN=your_actual_page_token_here
   
   # Google Sheets Configuration
   GOOGLE_SHEET_ID=your_actual_sheet_id_here
   GOOGLE_SHEET_NAME=Messages
   GOOGLE_CREDENTIALS_FILE=credentials.json
   ```

3. **Replace with your actual values:**
   - `FB_PAGE_ACCESS_TOKEN` = The token you copied from Facebook
   - `GOOGLE_SHEET_ID` = Your Google Sheet ID (from sheet URL)

4. **Save the file** (Ctrl+S)

---

## Step 5: Restart Server

**After updating `.env` file:**

1. **Go to Terminal 1** (where `python app.py` is running)

2. **Press `Ctrl+C`** to stop the server

3. **Restart it:**
   ```powershell
   python app.py
   ```

4. **You should see:**
   ```
   Google Sheets client initialized successfully
   * Running on http://127.0.0.1:5000
   ```

---

## Step 6: Test Everything! 🎉

**Now send a test message:**

1. **Send a test message** to your Facebook Page
   - From another Facebook account
   - Or use Facebook's test feature
   - Example message: "Hi ako si John Doe, taga purok calubihan barangay sampinit, 09914567842"

2. **Check your server terminal** (Terminal 1):
   - You should see logs like:
     ```
     INFO:__main__:Processed message from [sender_id]
     INFO:__main__:Message saved to Google Sheets from [sender_name]
     ```

3. **Check your Google Sheet:**
   - Open your Google Sheet
   - The message should appear automatically!
   - Should show columns:
     - Timestamp
     - Name
     - Contact Number (if in message)
     - Purok (if in message)
     - Barangay (if in message)
     - Mensahe (full message text)
     - Please Upload Picture (if attachment)
     - Email Address (if in message)
     - Status (New Message)

4. **Check ngrok terminal** (Terminal 2):
   - You might see new requests logged

---

## Quick Checklist:

- [x] Webhook verified ✅
- [x] Subscribed to `messages` field ✅
- [ ] Subscribed your Page
- [ ] Got Page Access Token
- [ ] Got Google Sheet ID
- [ ] Updated `.env` with Page Access Token
- [ ] Updated `.env` with Google Sheet ID
- [ ] Saved `.env` file
- [ ] Restarted server
- [ ] Sent test message
- [ ] Message appears in Google Sheet! 🎉

---

## Troubleshooting:

**If message doesn't appear in Sheet:**
- Check server terminal for errors
- Verify `GOOGLE_SHEET_ID` is correct
- Make sure service account email has access to sheet
- Check that Page is subscribed

**If server errors:**
- Check `.env` file has correct values
- Make sure `credentials.json` exists
- Verify Google Sheet ID is correct

---

**Next: Subscribe your Page, get tokens, update `.env`, and test!** 🚀

