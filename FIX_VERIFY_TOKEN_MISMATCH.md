# Fix Verify Token Mismatch - "Verification failed"

## ❌ Verify Token Mismatch!

**Error:** `{"error": "Verification failed"}`

**This means:** The verify token in your `.env` file doesn't match what you're testing with!

**Test URL uses:** `hub.verify_token=fb-messages`
**Server expects:** Whatever is in `FB_VERIFY_TOKEN` in your `.env` file

---

## Step 1: Check Your `.env` File

**Make sure your `.env` file exists and has the correct token:**

1. **Open your `.env` file** in Notepad or any text editor

2. **Check this line:**
   ```env
   FB_VERIFY_TOKEN=fb-messages
   ```

3. **Must be EXACTLY:**
   - ✅ `FB_VERIFY_TOKEN=fb-messages`
   - ❌ NOT `FB_VERIFY_TOKEN=your_facebook_verify_token_here`
   - ❌ NOT `FB_VERIFY_TOKEN=fb-messages ` (no extra spaces)
   - ❌ NOT `FB_VERIFY_TOKEN = fb-messages` (no spaces around =)
   - ❌ NOT `FB_VERIFY_TOKEN="fb-messages"` (no quotes)

4. **If it's wrong, fix it:**
   - Replace `your_facebook_verify_token_here` with `fb-messages`
   - Make sure no spaces or quotes
   - Save the file

---

## Step 2: Restart Your Server

**After updating `.env` file, you MUST restart the server:**

1. **Go to Terminal 1** (where `python app.py` is running)

2. **Press `Ctrl+C`** to stop the server

3. **Wait a few seconds**

4. **Restart the server:**
   ```powershell
   python app.py
   ```

5. **You should see:**
   ```
   Google Sheets client initialized successfully
   * Running on http://127.0.0.1:5000
   ```

6. **The server now reads the updated `.env` file!**

---

## Step 3: Test the Webhook URL Again

**After restarting the server:**

1. **Open your browser**

2. **Go to this URL:**
   ```
   http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123
   ```

3. **You should now see:** `test123` displayed on the page (not an error!)

4. **If it works:**
   - ✅ Token matching is working!
   - ✅ Webhook endpoint is working!
   - ✅ Ready to verify in Facebook!

5. **If you still see an error:**
   - Make sure `.env` file has `FB_VERIFY_TOKEN=fb-messages` exactly
   - Make sure server was restarted after updating `.env`
   - Check server terminal for error messages

---

## Step 4: Example `.env` File

**Your `.env` file should look like this:**

```env
# Facebook Webhook Configuration
FB_VERIFY_TOKEN=fb-messages
FB_PAGE_ACCESS_TOKEN=your_page_access_token_here

# Google Sheets Configuration
GOOGLE_SHEET_ID=your_google_sheet_id_here
GOOGLE_SHEET_NAME=Messages
GOOGLE_CREDENTIALS_FILE=credentials.json

# Excel Export Configuration (Optional)
EXCEL_EXPORT_ENABLED=false
EXCEL_FILENAME=fb_messages.xlsx

# Server Configuration
PORT=5000
```

**Important:**
- ✅ `FB_VERIFY_TOKEN=fb-messages` (exact match, no spaces, no quotes)
- ✅ Save the file
- ✅ Restart server after updating

---

## Quick Checklist:

- [ ] `.env` file exists in project folder
- [ ] `.env` file has `FB_VERIFY_TOKEN=fb-messages` exactly
- [ ] No spaces around `=`
- [ ] No quotes around the value
- [ ] Saved `.env` file
- [ ] Stopped server (`Ctrl+C`)
- [ ] Restarted server (`python app.py`)
- [ ] Test URL works: Shows `test123`
- [ ] Ready to verify in Facebook

---

## Common Mistakes:

### Mistake 1: Placeholder Not Replaced
**Problem:** `.env` still has `FB_VERIFY_TOKEN=your_facebook_verify_token_here`
**Solution:** Replace with `FB_VERIFY_TOKEN=fb-messages`

### Mistake 2: Extra Spaces
**Problem:** `FB_VERIFY_TOKEN = fb-messages` or `FB_VERIFY_TOKEN=fb-messages `
**Solution:** Remove spaces: `FB_VERIFY_TOKEN=fb-messages`

### Mistake 3: Quotes
**Problem:** `FB_VERIFY_TOKEN="fb-messages"`
**Solution:** Remove quotes: `FB_VERIFY_TOKEN=fb-messages`

### Mistake 4: Forgot to Restart Server
**Problem:** Updated `.env` but server still has old value
**Solution:** Always restart server after updating `.env`

---

**Fix your `.env` file, restart server, then test again!** 🚀

