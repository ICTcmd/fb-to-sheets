# Start ngrok - Expose Your Local Server

## ✅ Your Server is Running!

I can see:
- ✅ Google Sheets client initialized successfully
- ✅ Flask server running on `http://127.0.0.1:5000`
- ✅ Server is ready and waiting for webhooks!

**Keep this terminal window open!** Don't close it.

---

## Step 1: Install ngrok (If Not Already Installed)

### Download ngrok:

1. **Go to:** https://ngrok.com/download
2. **Download** ngrok for Windows
3. **Extract** the `.exe` file to a folder (e.g., `C:\ngrok\`)

---

## Step 2: Start ngrok in a NEW Terminal Window

### Open a NEW PowerShell/Command Prompt Window:

1. **Keep your server running** (don't close the current terminal)
2. **Open a NEW PowerShell window** (or Command Prompt)
3. **Navigate to ngrok folder** (if not in PATH):
   ```powershell
   cd C:\ngrok
   ```

4. **Start ngrok:**
   ```powershell
   ngrok http 5000
   ```

   **OR if ngrok is in your PATH:**
   ```powershell
   ngrok http 5000
   ```

---

## Step 3: Get Your ngrok URL

After starting ngrok, you'll see something like:

```
Forwarding    https://abc123xyz.ngrok.io -> http://localhost:5000

Session Status                online
Account                       Your Name (Plan: Free)
Version                       3.x.x
Region                        United States (us)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://abc123xyz.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

**Copy the HTTPS URL** - it will be something like:
- `https://abc123xyz.ngrok.io`
- This is your public URL!

---

## Step 4: Update Webhook in Facebook

Now go back to Facebook Developer Console:

1. **Go to your webhook configuration page** (where you saw the Callback URL field)

2. **Update the Callback URL:**
   - Replace the Make.com URL with: `https://your-ngrok-url.ngrok.io/webhook`
   - Example: `https://abc123xyz.ngrok.io/webhook`
   - **Important:** Make sure it ends with `/webhook`

3. **Make sure Verify Token matches:**
   - The Verify Token in Facebook should match what you'll put in your `.env` file
   - If you changed it, make sure it matches

4. **Click "Verify and save"** button

5. **If verification succeeds:** You'll see a success message!

---

## Step 5: Subscribe to Events

After saving the webhook:

1. **Look for "Subscribe to fields" or events section**
2. **Check the boxes:**
   - ✅ **`messages`** (REQUIRED!)
   - ✅ `messaging_postbacks` (optional)

3. **Click "Save"**

---

## Step 6: Subscribe Your Page

1. **Look for "Add Subscriptions" or "Subscribe" section**
2. **Select your Facebook Page** from dropdown
3. **Click "Subscribe"**

---

## Important Notes:

⚠️ **Keep Both Terminal Windows Open:**
- **Terminal 1:** Your Flask server (`python app.py`) - Keep running!
- **Terminal 2:** ngrok (`ngrok http 5000`) - Keep running!

⚠️ **Free ngrok URLs Change:**
- Each time you restart ngrok, you get a new URL
- If you restart ngrok, **update the webhook URL in Facebook again**
- For production, use a paid ngrok account or deploy to a real server

---

## Quick Checklist:

- [ ] Server running (`python app.py`)
- [ ] ngrok running (`ngrok http 5000`)
- [ ] Copied ngrok HTTPS URL
- [ ] Updated webhook URL in Facebook
- [ ] Clicked "Verify and save"
- [ ] Subscribed to `messages` event
- [ ] Subscribed your Page

---

## Next: Test It!

Once everything is set up:

1. **Send a test message** to your Facebook Page
2. **Check your server terminal** - you should see logs
3. **Check your Google Sheet** - message should appear!

---

**Ready to start ngrok?** Open a new terminal window and run:
```powershell
ngrok http 5000
```

Then copy the HTTPS URL and update your webhook! 🚀

