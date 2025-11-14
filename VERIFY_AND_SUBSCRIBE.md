# Verify Webhook and Subscribe to Fields

## ✅ Webhook URL Updated!

I can see:
- **Callback URL:** `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook` ✅
- **Verify Token:** Filled in (masked)
- **"Verify and save"** button (blue)

---

## Step 1: Verify and Save Webhook

1. **Make sure your server is running** (`python app.py` in Terminal 1)
2. **Make sure ngrok is running** (in Terminal 2)

3. **Click the blue "Verify and save" button** (bottom right)

4. **If verification succeeds:**
   - You'll see a success message
   - The webhook is now connected!
   - The "Webhook fields" section will appear or update

5. **If verification fails:**
   - Check that your server is running
   - Check that ngrok is running
   - Check the server terminal for error messages
   - Make sure the URL ends with `/webhook`
   - Make sure the Verify Token matches what's in your `.env` file

---

## Step 2: Subscribe to Webhook Fields

After saving the webhook, you'll see a **"Webhook fields"** section with a table.

**The table has columns:**
- Field
- Version
- Test
- Subscribe

**What to do:**

1. **Look for `messages` field** in the table
   - This is the field for receiving messages

2. **Check the "Subscribe" checkbox** for `messages`
   - ✅ Check the box in the "Subscribe" column

3. **Optional: Check other fields:**
   - ✅ `messaging_postbacks` (optional but recommended)
   - ✅ `message_deliveries` (optional)
   - ✅ `message_reads` (optional)

4. **Click "Save"** or the update button

---

## Step 3: Subscribe Your Page

After subscribing to fields, you need to subscribe your Page:

1. **Look for "Add Subscriptions" or "Subscribe" section**
   - This might be below the webhook fields table
   - Or in a separate section

2. **Select your Facebook Page** from dropdown
   - If you see "Manage Pages" dropdown at top, select your page there

3. **Click "Subscribe"** button

4. **You should see your Page listed as subscribed**

---

## Step 4: Get Page Access Token

Now you need to get your Page Access Token:

1. **Look for "Access Tokens" section**
   - Might be on the same page
   - Or click "Permissions and features" in left sidebar
   - Or look for a link/button that says "Access Tokens" or "Generate Token"

2. **Find "Generate Token" button**

3. **Select your Facebook Page** from dropdown

4. **Click "Generate Token"**

5. **COPY THE TOKEN** - It's a long string!
   - Save it securely
   - You'll need it for `.env` file as `FB_PAGE_ACCESS_TOKEN`

---

## Step 5: Write Down Your Verify Token

1. **In the Verify Token field**, click to see/unmask it
2. **Write down this token** - You'll need it for `.env` file as `FB_VERIFY_TOKEN`

---

## Step 6: Configure `.env` File

1. **Create `.env` file** (if not exists):
   ```powershell
   copy config_example.env .env
   ```

2. **Edit `.env` file** and add:
   ```env
   FB_VERIFY_TOKEN=your_verify_token_from_facebook
   FB_PAGE_ACCESS_TOKEN=your_page_access_token_here
   GOOGLE_SHEET_ID=your_google_sheet_id_here
   GOOGLE_SHEET_NAME=Messages
   GOOGLE_CREDENTIALS_FILE=credentials.json
   ```

3. **Replace with your actual values:**
   - `FB_VERIFY_TOKEN` = The verify token from the webhook field
   - `FB_PAGE_ACCESS_TOKEN` = The Page Access Token you just generated
   - `GOOGLE_SHEET_ID` = Your Google Sheet ID (from the sheet URL)

4. **Save the `.env` file**

---

## Step 7: Restart Your Server

1. **Go to Terminal 1** (where `python app.py` is running)
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

## Step 8: Test It! 🎉

1. **Send a test message** to your Facebook Page
   - From another account, or use Facebook's test feature

2. **Check your server terminal** - You should see:
   ```
   INFO:__main__:Processed message from [sender_id]
   INFO:__main__:Message saved to Google Sheets from [sender_name]
   ```

3. **Check your Google Sheet** - The message should appear automatically!

---

## Quick Checklist:

- [ ] Clicked "Verify and save" button ✅
- [ ] Webhook verified successfully
- [ ] Subscribed to `messages` field (checked the box)
- [ ] Subscribed your Facebook Page
- [ ] Got Page Access Token (copied and saved)
- [ ] Got Verify Token (copied and saved)
- [ ] Created `.env` file
- [ ] Configured `.env` with all tokens
- [ ] Restarted server
- [ ] Sent test message
- [ ] Message appears in Google Sheet! 🎉

---

**First, click "Verify and save" button!** Then subscribe to fields and your Page! 🚀

