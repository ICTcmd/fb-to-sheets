# Test Webhook and Verify in Facebook

## ✅ Server is Running!

**Status:**
- ✅ Google Sheets client initialized successfully
- ✅ Flask server running on `http://127.0.0.1:5000`
- ✅ Server is ready!

**Keep this terminal open!** Don't close it.

---

## Step 1: Test Webhook Endpoint Locally

**Before trying in Facebook, test locally:**

1. **Open your browser**

2. **Go to this URL:**
   ```
   http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123
   ```

3. **You should see:** `test123` displayed on the page

4. **If you see `test123`:**
   - ✅ Your webhook endpoint is working correctly!
   - ✅ Token verification is working!
   - ✅ Ready to verify in Facebook!

5. **If you see an error:**
   - Check server terminal for error messages
   - Make sure `.env` file has `FB_VERIFY_TOKEN=fb-messages`

---

## Step 2: Make Sure ngrok is Running

**Check Terminal 2** (where you ran `ngrok http 5000`):

1. **Should show:**
   ```
   Forwarding    https://radia-perissodactylous-cleo.ngrok-free.dev -> http://localhost:5000
   Session Status                online
   ```

2. **If ngrok is NOT running:**
   - Open a NEW PowerShell window
   - Run: `ngrok http 5000`
   - Keep it running!

3. **If ngrok URL changed:**
   - Copy the NEW ngrok URL
   - Update Callback URL in Facebook

---

## Step 3: Verify `.env` File

**Make sure your `.env` file has:**

```env
FB_VERIFY_TOKEN=fb-messages
GOOGLE_SHEET_ID=your_google_sheet_id_here
GOOGLE_CREDENTIALS_FILE=credentials.json
```

**Important:** `FB_VERIFY_TOKEN` must be exactly `fb-messages` (matching Facebook)

---

## Step 4: Go to Facebook and Click "Verify and save"

**Now that server is running:**

1. **Go to Facebook webhook configuration page**

2. **Verify settings:**
   - Callback URL: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook` ✅
   - Verify Token: `fb-messages` ✅

3. **Click the blue "Verify and save" button** (bottom right)

4. **Watch your server terminal** (Terminal 1):
   - You should see logs when Facebook tries to verify
   - Look for: `Webhook verified successfully` or similar

5. **If verification succeeds:**
   - ✅ Success message in Facebook
   - ✅ Error message disappears
   - ✅ Webhook fields table populates or updates
   - ✅ You can now subscribe to fields!

6. **If verification still fails:**
   - Check server terminal for error messages
   - Make sure test URL works (Step 1)
   - Make sure ngrok is running
   - Make sure `.env` has correct token

---

## Step 5: After Successful Verification - Subscribe to Fields

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

## Step 6: Subscribe Your Page

**After subscribing to fields:**

1. **Look for "Add Subscriptions" or "Subscribe" section**

2. **Select your Facebook Page** from dropdown

3. **Click "Subscribe"**

---

## Step 7: Get Page Access Token

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

## Step 8: Update `.env` File

**After getting Page Access Token:**

1. **Edit `.env` file** and update:
   ```env
   FB_VERIFY_TOKEN=fb-messages
   FB_PAGE_ACCESS_TOKEN=your_page_access_token_here
   GOOGLE_SHEET_ID=your_google_sheet_id_here
   GOOGLE_SHEET_NAME=Messages
   GOOGLE_CREDENTIALS_FILE=credentials.json
   PORT=5000
   ```

2. **Replace `your_page_access_token_here`** with the actual token you copied

3. **Replace `your_google_sheet_id_here`** with your Google Sheet ID

4. **Save the file**

---

## Step 9: Restart Server (If Updated `.env`)

**If you updated `.env` file:**

1. **Go to Terminal 1** (server terminal)

2. **Press `Ctrl+C`** to stop server

3. **Restart:**
   ```powershell
   python app.py
   ```

---

## Step 10: Test Everything! 🎉

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

- [x] Server running ✅
- [ ] Test URL works: `http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123`
- [ ] Shows `test123` on page
- [ ] ngrok running (Terminal 2)
- [ ] `.env` file has `FB_VERIFY_TOKEN=fb-messages`
- [ ] Clicked "Verify and save" in Facebook
- [ ] Verification succeeded
- [ ] Subscribed to `messages` field
- [ ] Subscribed your Page
- [ ] Got Page Access Token
- [ ] Updated `.env` with tokens
- [ ] Sent test message
- [ ] Message appears in Google Sheet! 🎉

---

**Next: Test the local URL first, then verify in Facebook!** 🚀

