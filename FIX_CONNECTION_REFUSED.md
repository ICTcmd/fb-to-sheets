# Fix Connection Refused Error

## ❌ Server is Not Running!

**Error:** `ERR_CONNECTION_REFUSED` - "localhost refused to connect"

**This means:** Your Flask server (`python app.py`) is NOT running or crashed!

---

## Step 1: Check Server Terminal

1. **Go to Terminal 1** (where you ran `python app.py`)

2. **Check if you see:**
   ```
   * Running on http://0.0.0.0:5000
   ```
   Or:
   ```
   * Running on http://127.0.0.1:5000
   ```

3. **If you DON'T see these messages:**
   - ❌ Server is not running
   - ❌ Server crashed
   - ❌ Server was stopped

---

## Step 2: Start/Restart Your Server

**If server is NOT running:**

1. **Go to Terminal 1** (your PowerShell window)

2. **Make sure you're in the project folder:**
   ```powershell
   cd "C:\Users\ACER\Desktop\FB to Sheets"
   ```

3. **Start the server:**
   ```powershell
   python app.py
   ```

4. **You should see:**
   ```
   INFO:__main__:Google Sheets client initialized successfully
    * Serving Flask app 'app'
    * Debug mode: on
    * Running on all addresses (0.0.0.0)
    * Running on http://127.0.0.1:5000
    * Running on http://10.0.0.22:5000
   ```

5. **Keep this terminal open!** Don't close it.

---

## Step 3: Test the Webhook URL Again

**After starting the server:**

1. **Wait a few seconds** for server to fully start

2. **Open your browser**

3. **Go to this URL:**
   ```
   http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123
   ```

4. **You should now see:** `test123` displayed on the page

5. **If you still see an error:**
   - Check server terminal for error messages
   - Make sure server is fully started
   - Try again after a few seconds

---

## Step 4: Common Issues

### Issue 1: Server Not Started
**Problem:** You never started the server or it was closed
**Solution:** Start it with `python app.py`

### Issue 2: Server Crashed
**Problem:** Server started but crashed
**Solution:** Check terminal for errors, fix them, restart server

### Issue 3: Wrong Port
**Problem:** Server running on different port
**Solution:** Check terminal logs - should say `port 5000`

### Issue 4: Port Already in Use
**Problem:** Another app using port 5000
**Solution:** 
- Close other apps using port 5000
- Or change port in `.env` file: `PORT=5001`
- Update ngrok: `ngrok http 5001`

---

## Step 5: After Server is Running

**Once server is running and test URL works:**

1. **Make sure ngrok is still running** (Terminal 2)
   - Should show: `Forwarding https://radia-perissodactylous-cleo.ngrok-free.dev -> http://localhost:5000`

2. **Go back to Facebook webhook page**

3. **Click "Verify and save"** button again

4. **Should work now!**

---

## Quick Checklist:

- [ ] Server terminal shows: `* Running on http://127.0.0.1:5000`
- [ ] Test URL works: Shows `test123` on page
- [ ] ngrok is still running (Terminal 2)
- [ ] `.env` file has `FB_VERIFY_TOKEN=fb-messages`
- [ ] Ready to verify webhook in Facebook

---

**Action: Start your server with `python app.py` in Terminal 1!** 🚀

