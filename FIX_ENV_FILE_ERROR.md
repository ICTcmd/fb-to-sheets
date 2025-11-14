# Fix .env File Error - Duplicate FB_VERIFY_TOKEN

## ❌ Error Found in Your `.env` File!

**Current (WRONG):**
```
FB_VERIFY_TOKEN=FB_VERIFY_TOKEN=fb-messages
```

**Should be (CORRECT):**
```
FB_VERIFY_TOKEN=fb-messages
```

**The problem:** `FB_VERIFY_TOKEN` appears twice! The value is reading as `FB_VERIFY_TOKEN=fb-messages` instead of just `fb-messages`.

---

## Step 1: Make Sure You're Editing the RIGHT File

**Important:** You need to edit the `.env` file, NOT `config_example.env`!

1. **Check if `.env` file exists:**
   ```powershell
   dir .env
   ```

2. **If `.env` doesn't exist, create it:**
   ```powershell
   copy config_example.env .env
   ```

3. **Open `.env` file** (NOT `config_example.env`)

---

## Step 2: Fix the Error

**In your `.env` file, find this line:**
```
FB_VERIFY_TOKEN=FB_VERIFY_TOKEN=fb-messages
```

**Change it to:**
```
FB_VERIFY_TOKEN=fb-messages
```

**Make sure:**
- ✅ Only one `FB_VERIFY_TOKEN=`
- ✅ Value is just `fb-messages`
- ✅ No duplicate keys
- ✅ No spaces around `=`

---

## Step 3: Complete `.env` File Should Look Like:

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

**Important points:**
- ✅ `FB_VERIFY_TOKEN=fb-messages` (no duplicate!)
- ✅ Each variable appears only once
- ✅ No spaces around `=`
- ✅ No quotes around values

---

## Step 4: Save the File

**After fixing the error:**

1. **Save your `.env` file**

2. **Make sure it's saved as `.env`** (not `.env.txt` or anything else)

---

## Step 5: Restart Your Server

**After fixing `.env` file, you MUST restart the server:**

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

---

## Step 6: Test the Webhook URL Again

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

---

## Quick Checklist:

- [ ] Opened `.env` file (NOT `config_example.env`)
- [ ] Fixed `FB_VERIFY_TOKEN=FB_VERIFY_TOKEN=fb-messages` to `FB_VERIFY_TOKEN=fb-messages`
- [ ] Removed duplicate `FB_VERIFY_TOKEN=`
- [ ] Saved `.env` file
- [ ] Stopped server (`Ctrl+C`)
- [ ] Restarted server (`python app.py`)
- [ ] Test URL works: Shows `test123`
- [ ] Ready to verify in Facebook

---

**Fix the duplicate, save, restart server, then test again!** 🚀

