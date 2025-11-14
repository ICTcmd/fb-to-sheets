# Final Webhook Setup - Almost Done! ✅

## ✅ ngrok is Running!

**Your ngrok URL:**
```
https://radia-perissodactylous-cleo.ngrok-free.dev
```

**Your Webhook URL should be:**
```
https://radia-perissodactylous-cleo.ngrok-free.dev/webhook
```

**Keep both terminals open!**
- Terminal 1: Flask server (`python app.py`)
- Terminal 2: ngrok (currently running)

---

## Step 1: Update Webhook in Facebook

1. **Go back to Facebook Developer Console**
   - Navigate to: Webhooks configuration page
   - Where you saw the Callback URL field

2. **Update the Callback URL:**
   - Delete the Make.com URL
   - Enter: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook`
   - **Important:** Make sure it ends with `/webhook`

3. **Verify Token:**
   - Check the Verify Token field
   - **Write down this token** - You'll need it for `.env` file as `FB_VERIFY_TOKEN`
   - Or change it to something simple like: `my_secure_token_123`
   - If you change it, **remember it!**

4. **Click "Verify and save"** button (blue button, bottom right)

5. **If verification succeeds:**
   - You'll see a success message
   - The webhook is now connected to your server!

---

## Step 2: Subscribe to Events

After saving the webhook:

1. **Look for "Subscribe to fields" or "Subscribe to events" section**

2. **Check the boxes:**
   - ✅ **`messages`** (REQUIRED!)
   - ✅ `messaging_postbacks` (optional but recommended)

3. **Click "Save"**

---

## Step 3: Subscribe Your Page

1. **Look for "Add Subscriptions" or "Subscribe" section**

2. **Select your Facebook Page** from dropdown

3. **Click "Subscribe"**

---

## Step 4: Get Page Access Token

1. **Look for "Access Tokens" section** (same page or sidebar)

2. **Or click "Permissions and features"** in left panel

3. **Find "Generate Token" or "Access Tokens" button**

4. **Select your Facebook Page** from dropdown

5. **Click "Generate Token"**

6. **COPY THE TOKEN** - It's a long string
   - Save it securely!
   - You'll need it for `.env` file

---

## Step 5: Configure `.env` File

1. **In your project folder**, make sure you have a `.env` file
   - If not, copy from `config_example.env`:
   ```powershell
   copy config_example.env .env
   ```

2. **Edit `.env` file** and add/update these values:

   ```env
   # Facebook Webhook Configuration
   FB_VERIFY_TOKEN=your_verify_token_from_facebook
   FB_PAGE_ACCESS_TOKEN=your_page_access_token_here
   
   # Google Sheets Configuration
   GOOGLE_SHEET_ID=your_google_sheet_id_here
   GOOGLE_SHEET_NAME=Messages
   GOOGLE_CREDENTIALS_FILE=credentials.json
   
   # Server Configuration
   PORT=5000
   ```

3. **Replace:**
   - `FB_VERIFY_TOKEN` = The verify token from Facebook webhook
   - `FB_PAGE_ACCESS_TOKEN` = The Page Access Token you just generated
   - `GOOGLE_SHEET_ID` = Your Google Sheet ID

4. **Save the `.env` file**

---

## Step 6: Restart Your Server

1. **Go back to Terminal 1** (where `python app.py` is running)

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

## Step 7: Test It! 🎉

1. **Send a test message** to your Facebook Page
   - From another account, or use Facebook's test feature

2. **Check your server terminal** - You should see:
   ```
   INFO:__main__:Processed message from 123456789
   INFO:__main__:Message saved to Google Sheets from [Sender Name]
   ```

3. **Check your Google Sheet** - The message should appear automatically!

---

## Troubleshooting:

### Webhook verification fails:
- Make sure your server is running (`python app.py`)
- Make sure ngrok is running
- Check that the URL ends with `/webhook`
- Verify token must match in both Facebook and `.env` file

### Messages not appearing in Sheets:
- Check server logs for errors
- Verify `GOOGLE_SHEET_ID` in `.env` is correct
- Check that service account has access to sheet
- Make sure you subscribed to `messages` event
- Make sure you subscribed your Page

### Server errors:
- Check `.env` file is configured correctly
- Make sure `credentials.json` is in project folder
- Verify all environment variables are set

---

## Quick Checklist:

- [ ] ngrok running (`https://radia-perissodactylous-cleo.ngrok-free.dev`)
- [ ] Server running (`python app.py`)
- [ ] Webhook URL updated in Facebook
- [ ] Verify Token saved to `.env`
- [ ] Page Access Token generated and saved to `.env`
- [ ] `.env` file configured with all values
- [ ] Subscribed to `messages` event
- [ ] Subscribed your Page
- [ ] Server restarted (if you updated `.env`)
- [ ] Test message sent
- [ ] Message appears in Google Sheet! ✅

---

**You're almost done!** Just update the webhook URL in Facebook and configure your `.env` file! 🚀

