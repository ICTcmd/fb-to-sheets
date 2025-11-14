# Update Your .env File - Replace Placeholder Values!

## ❌ Your `.env` File Still Has Placeholder Values!

Your `.env` file currently has:
```
FB_VERIFY_TOKEN=your_facebook_verify_token_here
FB_PAGE_ACCESS_TOKEN=your_page_access_token_here
GOOGLE_SHEET_ID=your_google_sheet_id_here
```

**These need to be replaced with ACTUAL values!**

---

## Step 1: Update Verify Token

**Replace:**
```
FB_VERIFY_TOKEN=your_facebook_verify_token_here
```

**With:**
```
FB_VERIFY_TOKEN=fb-messages
```

**This MUST match what you entered in Facebook webhook!**

---

## Step 2: Get and Add Page Access Token

**You need to get your Page Access Token from Facebook:**

1. **Go to Facebook Developer Console**
   - Go to your webhook configuration page
   - Or click "Permissions and features" in left sidebar

2. **Look for "Access Tokens" section**

3. **Find "Generate Token" button**

4. **Select your Facebook Page** from dropdown

5. **Click "Generate Token"**

6. **COPY THE TOKEN** - It's a long string!

7. **Replace in `.env`:**
   ```
   FB_PAGE_ACCESS_TOKEN=your_actual_token_here
   ```

---

## Step 3: Get and Add Google Sheet ID

**You need your Google Sheet ID:**

1. **Open your Google Sheet** (the one you shared with the service account)

2. **Look at the URL** - It should look like:
   ```
   https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit
   ```

3. **Copy the `SHEET_ID_HERE` part** - That's your Sheet ID!

4. **Replace in `.env`:**
   ```
   GOOGLE_SHEET_ID=your_actual_sheet_id_here
   ```

---

## Step 4: Final `.env` File Should Look Like:

```env
# Facebook Webhook Configuration
FB_VERIFY_TOKEN=fb-messages
FB_PAGE_ACCESS_TOKEN=EAABsbCS1iHgBO...your_actual_token_here

# Google Sheets Configuration
GOOGLE_SHEET_ID=1abc123xyz456...your_actual_sheet_id_here
GOOGLE_SHEET_NAME=Messages
GOOGLE_CREDENTIALS_FILE=credentials.json

# Excel Export Configuration (Optional)
EXCEL_EXPORT_ENABLED=false
EXCEL_FILENAME=fb_messages.xlsx

# Server Configuration
PORT=5000
```

---

## Step 5: Save and Restart Server

1. **Save your `.env` file**

2. **Go to Terminal 1** (where `python app.py` is running)

3. **Press `Ctrl+C`** to stop the server

4. **Restart it:**
   ```powershell
   python app.py
   ```

5. **Check the logs** - Should see:
   ```
   Google Sheets client initialized successfully
   * Running on http://0.0.0.0:5000
   ```

---

## Step 6: Now Try "Verify and save" in Facebook

**After updating `.env` and restarting:**

1. **Go to Facebook webhook configuration**

2. **Click "Verify and save"** button

3. **Should succeed now!**

---

## Quick Checklist:

- [ ] Updated `FB_VERIFY_TOKEN=fb-messages` in `.env`
- [ ] Got Page Access Token from Facebook
- [ ] Added `FB_PAGE_ACCESS_TOKEN=actual_token` to `.env`
- [ ] Got Google Sheet ID from sheet URL
- [ ] Added `GOOGLE_SHEET_ID=actual_id` to `.env`
- [ ] Saved `.env` file
- [ ] Restarted server (`Ctrl+C`, then `python app.py`)
- [ ] Server running successfully
- [ ] Ready to verify webhook in Facebook!

---

**Update your `.env` file with actual values, then restart your server!** 🚀

