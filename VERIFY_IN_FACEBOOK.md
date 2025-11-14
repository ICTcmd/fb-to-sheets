# Verify Webhook in Facebook - Ready! ✅

## ✅ Your Webhook Endpoint is Working!

**Test Result:** `test123` displayed on page ✅

**This means:**
- ✅ Your webhook endpoint is working correctly!
- ✅ Token verification is working!
- ✅ Server is responding correctly!

**Now verify in Facebook!**

---

## Step 1: Make Sure Everything is Running

**Check both terminals:**

1. **Terminal 1:** Server running (`python app.py`)
   - Should show: `* Running on http://127.0.0.1:5000` ✅

2. **Terminal 2:** ngrok running (`ngrok http 5000`)
   - Should show: `Forwarding https://radia-perissodactylous-cleo.ngrok-free.dev -> http://localhost:5000` ✅
   - Should show: `Session Status online` ✅

**Keep both terminals open!**

---

## Step 2: Verify in Facebook

**Now go to Facebook webhook page:**

1. **Go to Facebook Developer Console**
   - Navigate to your webhook configuration page
   - Where you see: Callback URL and Verify Token fields

2. **Verify settings:**
   - Callback URL: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook` ✅
   - Verify Token: `fb-messages` ✅

3. **Click the blue "Verify and save" button** (bottom right)

4. **Watch your server terminal** (Terminal 1):
   - You should see logs when Facebook tries to verify
   - Look for: Successful verification or any errors

5. **If verification succeeds:**
   - ✅ Success message in Facebook
   - ✅ Error message disappears
   - ✅ Webhook fields table populates or updates
   - ✅ You can now subscribe to fields!

6. **If verification fails:**
   - Check server terminal for error messages
   - Make sure both server and ngrok are running
   - Make sure `.env` has correct token

---

## Step 3: After Successful Verification - Subscribe to Fields

**Once verification succeeds:**

1. **Scroll down to "Webhook fields" table**

2. **Find `messages` field:**
   - Scroll or search for "messages"
   - Look in the "Field" column

3. **Toggle "Subscribe" switch to ON** (green) for `messages` field

4. **Optional:** Also subscribe to:
   - `messaging_postbacks` (recommended)

5. **Click "Save"** or update button

---

## Step 4: Subscribe Your Page

**After subscribing to fields:**

1. **Look for "Add Subscriptions" or "Subscribe" section**

2. **Select your Facebook Page** from dropdown

3. **Click "Subscribe"**

---

## Step 5: Get Page Access Token

**Now get your Page Access Token:**

1. **Look for "Access Tokens" section**
   - Might be on same page
   - Or click "Permissions and features" in left sidebar

2. **Find "Generate Token" button**

3. **Select your Facebook Page** from dropdown

4. **Click "Generate Token"**

5. **COPY THE TOKEN** - It's a long string!
   - Save it securely
   - You'll need it for `.env` file as `FB_PAGE_ACCESS_TOKEN`

---

## Step 6: Update `.env` File

**After getting Page Access Token:**

1. **Open `.env` file** in Notepad

2. **Update these lines:**
   ```env
   FB_VERIFY_TOKEN=fb-messages
   FB_PAGE_ACCESS_TOKEN=your_actual_page_token_here
   GOOGLE_SHEET_ID=your_actual_sheet_id_here
   ```

3. **Replace with your actual values:**
   - `FB_PAGE_ACCESS_TOKEN` = The token you just copied
   - `GOOGLE_SHEET_ID` = Your Google Sheet ID (from sheet URL)

4. **Save the file**

---

## Step 7: Restart Server (If Updated `.env`)

**If you updated `.env` file:**

1. **Go to Terminal 1** (server terminal)

2. **Press `Ctrl+C`** to stop server

3. **Restart:**
   ```powershell
   python app.py
   ```

---

## Step 8: Test Everything! 🎉

**Send a test message:**

1. **Send a test message** to your Facebook Page
   - From another account or test feature

2. **Check your server terminal** - Should see:
   ```
   INFO:__main__:Processed message from [sender_id]
   INFO:__main__:Message saved to Google Sheets from [sender_name]
   ```

3. **Check your Google Sheet** - Message should appear automatically with:
   - Timestamp
   - Name
   - Contact Number (if in message)
   - Purok (if in message)
   - Barangay (if in message)
   - Message text
   - Status

---

## Quick Checklist:

- [x] Webhook endpoint tested: Shows `test123` ✅
- [x] Server running ✅
- [ ] ngrok running (check Terminal 2)
- [ ] Clicked "Verify and save" in Facebook
- [ ] Verification succeeded
- [ ] Subscribed to `messages` field
- [ ] Subscribed your Page
- [ ] Got Page Access Token
- [ ] Updated `.env` with Page Access Token
- [ ] Updated `.env` with Google Sheet ID
- [ ] Restarted server (if needed)
- [ ] Sent test message
- [ ] Message appears in Google Sheet! 🎉

---

**Next: Go to Facebook and click "Verify and save"!** 🚀

