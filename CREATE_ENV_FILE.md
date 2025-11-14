# Create .env File - You Don't Have One Yet!

## ⚠️ Problem: No `.env` File Found!

**Your search results show:**
- ✅ `config_example.env` (template file)
- ❌ NO `.env` file!

**You need to CREATE the `.env` file first!**

---

## Step 1: Create `.env` File

**You need to copy from the example file:**

### Option 1: Using File Explorer (Easy!)

1. **In File Explorer**, find `config_example.env` in your project folder:
   ```
   C:\Users\ACER\Desktop\FB to Sheets\config_example.env
   ```

2. **Right-click** on `config_example.env`

3. **Select "Copy"**

4. **Right-click** in the same folder (empty space)

5. **Select "Paste"**

6. **Rename the copied file:**
   - Right-click the copied file: `config_example.env - Copy`
   - Select "Rename"
   - Change name to: `.env`
   - Press Enter

### Option 2: Using PowerShell (Fast!)

1. **Open PowerShell** in your project folder

2. **Run this command:**
   ```powershell
   copy config_example.env .env
   ```

3. **Verify it was created:**
   ```powershell
   dir .env
   ```
   Should show: `.env` file

---

## Step 2: Fix the `.env` File

**After creating `.env`, open it and fix the errors:**

### Open `.env` File

1. **Double-click** `.env` file in File Explorer
2. **Opens in Notepad or your default text editor**

### Fix the Content

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
- ✅ `FB_VERIFY_TOKEN=fb-messages` (NOT `FB_VERIFY_TOKEN=FB_VERIFY_TOKEN=fb-messages`)
- ✅ Only one `FB_VERIFY_TOKEN=`
- ✅ No spaces around `=`
- ✅ No quotes around values

### If You See This Error:

**If you see:**
```
FB_VERIFY_TOKEN=FB_VERIFY_TOKEN=fb-messages
```

**Change it to:**
```
FB_VERIFY_TOKEN=fb-messages
```

**Remove the duplicate!**

---

## Step 3: Save the File

**After fixing:**

1. **Save the `.env` file** (Ctrl+S)

2. **Make sure it's saved as `.env`** (not `.env.txt`)

---

## Step 4: Restart Your Server

**After creating and fixing `.env` file:**

1. **Go to Terminal 1** (where `python app.py` is running)

2. **Press `Ctrl+C`** to stop the server

3. **Restart the server:**
   ```powershell
   python app.py
   ```

4. **You should see:**
   ```
   Google Sheets client initialized successfully
   * Running on http://127.0.0.1:5000
   ```

---

## Step 5: Test the Webhook URL

**After restarting:**

1. **Open your browser**

2. **Go to:**
   ```
   http://localhost:5000/webhook?hub.mode=subscribe&hub.verify_token=fb-messages&hub.challenge=test123
   ```

3. **You should now see:** `test123` on the page (not an error!)

---

## Quick Steps:

1. ✅ Copy `config_example.env` to `.env`
2. ✅ Open `.env` file
3. ✅ Fix `FB_VERIFY_TOKEN=fb-messages` (remove duplicate if present)
4. ✅ Save `.env` file
5. ✅ Restart server (`Ctrl+C`, then `python app.py`)
6. ✅ Test URL: Should show `test123`

---

**Create the `.env` file first, then fix it and restart your server!** 🚀

