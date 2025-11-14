# Final Verification Steps - Everything is Running! ✅

## ✅ Perfect! Both Server and ngrok are Running!

**Status:**
- ✅ Server running on `http://127.0.0.1:5000`
- ✅ ngrok running and forwarding: `https://radia-perissodactylous-cleo.ngrok-free.dev -> http://localhost:5000`
- ✅ Keep both terminals open!

---

## Step 1: Verify `.env` File Configuration

**Make sure your `.env` file has the correct token:**

1. **Check if `.env` exists:**
   ```powershell
   dir .env
   ```

2. **If `.env` doesn't exist, create it:**
   ```powershell
   copy config_example.env .env
   ```

3. **Edit `.env` file** and make sure it has:
   ```env
   FB_VERIFY_TOKEN=fb-messages
   GOOGLE_SHEET_ID=your_google_sheet_id_here
   GOOGLE_CREDENTIALS_FILE=credentials.json
   ```

   **CRITICAL:** `FB_VERIFY_TOKEN` must be exactly `fb-messages` (matching Facebook)

4. **If you just updated `.env`:**
   - Go to Terminal 1 (server terminal)
   - Press `Ctrl+C` to stop server
   - Restart: `python app.py`

---

## Step 2: Test Webhook Endpoint Manually (Optional but Recommended)

**Before trying in Facebook, test locally:**

1. **Open your browser**
2. **Go to this URL:**
   ```
   http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123
   ```

3. **You should see:** `test123` displayed on the page

4. **If it works:**
   - ✅ Your webhook endpoint is working correctly!
   - Ready to verify in Facebook

5. **If you see an error:**
   - Check server terminal for error messages
   - Make sure `.env` file has `FB_VERIFY_TOKEN=fb-messages`

---

## Step 3: Go Back to Facebook and Click "Verify and save"

**Now that everything is running:**

1. **Go to Facebook webhook configuration page**

2. **Verify settings:**
   - Callback URL: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook` ✅
   - Verify Token: `fb-messages` ✅

3. **Click the blue "Verify and save" button** (bottom right)

4. **Watch your server terminal (Terminal 1):**
   - You should see logs when Facebook tries to verify
   - Look for: `Webhook verified successfully` or similar

5. **If verification succeeds:**
   - ✅ Success message in Facebook
   - ✅ Error message disappears
   - ✅ Webhook fields table populates or updates
   - ✅ You can now subscribe to fields

6. **If verification still fails:**
   - Check server terminal for error messages
   - Try the test URL above first
   - Make sure `.env` has correct token
   - Make sure server was restarted after updating `.env`

---

## Step 4: After Successful Verification - Subscribe to Fields

**Once verification succeeds:**

1. **Scroll down to "Webhook fields" table**

2. **Find `messages` field:**
   - You might need to scroll or search
   - Look for "messages" in the Field column

3. **Toggle "Subscribe" switch to ON** (green) for `messages` field

4. **Optional:** Also subscribe to:
   - `messaging_postbacks` (recommended)

5. **Click "Save"** or update button

---

## Step 5: Subscribe Your Page

**After subscribing to fields:**

1. **Look for "Add Subscriptions" or "Subscribe" section**
   - This might be below the webhook fields
   - Or in a separate section

2. **Select your Facebook Page** from dropdown
   - Use "Manage Pages" dropdown if available

3. **Click "Subscribe"** button

4. **You should see your Page listed as subscribed**

---

## Step 6: Get Page Access Token

**Now get your Page Access Token:**

1. **Look for "Access Tokens" section**
   - Might be on the same page
   - Or click "Permissions and features" in left sidebar
   - Or look for a link/button

2. **Find "Generate Token" or "Access Tokens" button**

3. **Select your Facebook Page** from dropdown

4. **Click "Generate Token"**

5. **COPY THE TOKEN** - It's a long string!
   - Save it securely
   - You'll need it for `.env` file as `FB_PAGE_ACCESS_TOKEN`

---

## Step 7: Update `.env` File with Page Access Token

1. **Edit `.env` file** and add/update:
   ```env
   FB_VERIFY_TOKEN=fb-messages
   FB_PAGE_ACCESS_TOKEN=your_page_access_token_here
   GOOGLE_SHEET_ID=your_google_sheet_id_here
   GOOGLE_SHEET_NAME=Messages
   GOOGLE_CREDENTIALS_FILE=credentials.json
   PORT=5000
   ```

2. **Replace `your_page_access_token_here`** with the actual token you just copied

3. **Replace `your_google_sheet_id_here`** with your Google Sheet ID

4. **Save the file**

---

## Step 8: Restart Server (If You Updated `.env`)

**If you updated `.env` file:**

1. **Go to Terminal 1** (server terminal)
2. **Press `Ctrl+C`** to stop
3. **Restart:**
   ```powershell
   python app.py
   ```

---

## Step 9: Test Everything! 🎉

**Now test the complete setup:**

1. **Send a test message** to your Facebook Page
   - From another account, or use Facebook's test feature

2. **Check your server terminal** - You should see:
   ```
   INFO:__main__:Processed message from [sender_id]
   INFO:__main__:Message saved to Google Sheets from [sender_name]
   ```

3. **Check your Google Sheet** - The message should appear automatically with:
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
- [x] ngrok running ✅
- [ ] `.env` file has `FB_VERIFY_TOKEN=fb-messages`
- [ ] Test URL works (optional but recommended)
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

**You're ready!** Go to Facebook and click "Verify and save"! 🚀

Let me know what happens!

