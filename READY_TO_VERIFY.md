# Ready to Verify Webhook - Server is Running! ✅

## ✅ Your Server is Running!

I can see:
- ✅ Google Sheets client initialized successfully
- ✅ Flask server running on `http://127.0.0.1:5000`
- ✅ Server is ready!

**Keep this terminal window open!** Don't close it.

---

## Step 1: Make Sure ngrok is Still Running

**Check Terminal 2** (where you ran `ngrok http 5000`):

1. **Is ngrok still running?**
   - Should show: `Forwarding https://radia-perissodactylous-cleo.ngrok-free.dev -> http://localhost:5000`
   - Should show: `Session Status online`

2. **If ngrok is NOT running:**
   - Open a NEW PowerShell window
   - Run: `ngrok http 5000`
   - Keep it running!

3. **If ngrok URL changed:**
   - Copy the NEW ngrok URL
   - Update the Callback URL in Facebook to the new URL

---

## Step 2: Verify `.env` File Has Correct Token

**Make sure your `.env` file exists and has:**

1. **Check `.env` file exists:**
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

   **IMPORTANT:** `FB_VERIFY_TOKEN` must be exactly `fb-messages` (matching Facebook)

4. **If you updated `.env` file:**
   - You already restarted the server ✅
   - That's good!

---

## Step 3: Test Webhook Endpoint Manually

**Before trying in Facebook, test locally:**

1. **Open your browser**
2. **Go to this URL:**
   ```
   http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123
   ```

3. **You should see:** `test123` displayed on the page

4. **If you see an error:**
   - Check server terminal for error messages
   - Make sure `.env` file has `FB_VERIFY_TOKEN=fb-messages`

---

## Step 4: Check Server Terminal for Errors

**Watch your server terminal** (Terminal 1):

1. **When you click "Verify and save" in Facebook:**
   - You should see logs in the terminal
   - Look for any error messages

2. **Good signs:**
   - `Webhook verified successfully`
   - `127.0.0.1 - - [timestamp] "GET /webhook?hub.mode=subscribe..." 200`

3. **Bad signs:**
   - `403` or `Verification failed`
   - `404` or `Not Found`
   - Any error messages

---

## Step 5: Try "Verify and Save" in Facebook Again

**Now go back to Facebook:**

1. **Go to Facebook webhook configuration page**

2. **Check the settings:**
   - Callback URL: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook`
   - Verify Token: `fb-messages`

3. **Click "Verify and save" button** (blue button, bottom right)

4. **Watch your server terminal** - You should see logs!

5. **If verification succeeds:**
   - ✅ You'll see a success message in Facebook
   - ✅ The error message will disappear
   - ✅ Webhook fields table will populate or update

6. **If verification still fails:**
   - Check server terminal for error messages
   - Make sure both server and ngrok are running
   - Verify `.env` file has correct token

---

## Step 6: After Successful Verification

Once verification succeeds:

1. **Scroll down to "Webhook fields" table**

2. **Find `messages` field:**
   - Scroll or search for "messages"
   - Look for it in the table

3. **Toggle "Subscribe" switch to ON** (green) for `messages` field

4. **Click "Save"**

5. **Subscribe your Page:**
   - Look for "Add Subscriptions" or "Subscribe" section
   - Select your Facebook Page
   - Click "Subscribe"

---

## Quick Checklist Before Trying Again:

- [ ] Server running (`python app.py` in Terminal 1) ✅
- [ ] ngrok running (`ngrok http 5000` in Terminal 2) - Check this!
- [ ] `.env` file has `FB_VERIFY_TOKEN=fb-messages` ✅
- [ ] Server restarted after updating `.env` ✅
- [ ] Test URL works: `http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123`

---

## If Verification Still Fails:

1. **Check ngrok is running** - This is the most common issue!
2. **Check `.env` file** - Token must match exactly
3. **Check server terminal** - Look for error messages
4. **Try test URL** - Should show `test123`
5. **Check ngrok URL** - Make sure it hasn't changed

---

**Next Step:** Make sure ngrok is running, then click "Verify and save" in Facebook again! 🚀

