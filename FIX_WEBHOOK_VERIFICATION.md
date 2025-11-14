# Fix Webhook Verification Error

## ❌ Verification Failed!

**Error Message:**
"The callback URL or verify token couldn't be validated. Please verify the provided information or try again later."

**Current Configuration:**
- Callback URL: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook` ✅
- Verify Token: `fb-messages` ✅

---

## Troubleshooting Steps:

### Step 1: Check Your Server is Running

1. **Go to Terminal 1** (where `python app.py` is running)
2. **Make sure you see:**
   ```
   * Running on http://0.0.0.0:5000
   ```
3. **If server is NOT running:**
   - Start it: `python app.py`
   - Keep it running!

---

### Step 2: Check ngrok is Running

1. **Go to Terminal 2** (where `ngrok http 5000` is running)
2. **Make sure you see:**
   ```
   Forwarding    https://radia-perissodactylous-cleo.ngrok-free.dev -> http://localhost:5000
   Session Status                online
   ```
3. **If ngrok is NOT running:**
   - Start it: `ngrok http 5000`
   - Keep it running!

---

### Step 3: Check `.env` File Configuration

**Critical:** The Verify Token in Facebook MUST match your `.env` file!

1. **Check your `.env` file** exists:
   ```powershell
   dir .env
   ```

2. **If `.env` doesn't exist, create it:**
   ```powershell
   copy config_example.env .env
   ```

3. **Open `.env` file** and check:
   ```env
   FB_VERIFY_TOKEN=fb-messages
   ```

   **Must match exactly!** If your Verify Token in Facebook is `fb-messages`, then `.env` must have `FB_VERIFY_TOKEN=fb-messages`

4. **If you need to update it:**
   - Edit `.env` file
   - Make sure `FB_VERIFY_TOKEN` matches Facebook exactly
   - Save the file

---

### Step 4: Restart Your Server

After updating `.env` file:

1. **Go to Terminal 1** (server terminal)
2. **Press `Ctrl+C`** to stop the server
3. **Restart it:**
   ```powershell
   python app.py
   ```

4. **Check the logs** - Should see:
   ```
   Google Sheets client initialized successfully
   * Running on http://0.0.0.0:5000
   ```

---

### Step 5: Test Webhook Endpoint Manually

1. **Open your browser**
2. **Go to:** `http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123`
3. **You should see:** `test123` displayed on the page
4. **If you see an error**, there's an issue with your server

---

### Step 6: Check Server Logs for Errors

When you click "Verify and save" in Facebook:

1. **Watch Terminal 1** (server terminal)
2. **Look for logs** showing:
   - Webhook verification request received
   - Any error messages

3. **Common errors:**
   - `403` or `Verification failed` - Verify token mismatch
   - `Connection refused` - Server not running
   - `404` - Wrong URL path

---

### Step 7: Try Again

After fixing any issues:

1. **Make sure:**
   - ✅ Server is running (`python app.py`)
   - ✅ ngrok is running (`ngrok http 5000`)
   - ✅ `.env` file has `FB_VERIFY_TOKEN=fb-messages` (matching Facebook)
   - ✅ Server was restarted after updating `.env`

2. **Go back to Facebook webhook page**

3. **Click "Verify and save" button again**

4. **Should succeed this time!**

---

## Common Issues:

### Issue 1: Verify Token Mismatch
**Problem:** Facebook token doesn't match `.env` file
**Solution:** Make sure both have exactly the same token

### Issue 2: Server Not Running
**Problem:** Server is stopped or crashed
**Solution:** Restart server with `python app.py`

### Issue 3: ngrok Not Running
**Problem:** ngrok stopped or URL changed
**Solution:** Restart ngrok with `ngrok http 5000`

### Issue 4: Server Crashed
**Problem:** Server has an error
**Solution:** Check server terminal for error messages and fix them

---

## Quick Checklist:

- [ ] Server running (`python app.py` in Terminal 1)
- [ ] ngrok running (`ngrok http 5000` in Terminal 2)
- [ ] `.env` file exists and has `FB_VERIFY_TOKEN=fb-messages`
- [ ] Verify token in Facebook matches `.env` exactly
- [ ] Server restarted after updating `.env`
- [ ] No errors in server terminal
- [ ] ngrok URL is still `https://radia-perissodactylous-cleo.ngrok-free.dev`

---

## Alternative: Try a Different Verify Token

If it still doesn't work:

1. **Change Verify Token in Facebook** to something simpler:
   - Try: `test123` or `my_token`

2. **Update `.env` file** to match:
   ```env
   FB_VERIFY_TOKEN=test123
   ```

3. **Restart server**

4. **Try "Verify and save" again**

---

**First, check that your server and ngrok are both running, then verify your `.env` file has the matching token!** 🚀

