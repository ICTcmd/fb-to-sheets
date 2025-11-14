# Quick Start Guide

**New to this?** Start with [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed step-by-step instructions.

**Already familiar?** Follow this quick start guide.

## 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 2. Set Up Google Sheets API (5 minutes)

1. Go to https://console.cloud.google.com/
2. Create a new project (or select existing)
3. Enable APIs:
   - Search for "Google Sheets API" → Enable
   - Search for "Google Drive API" → Enable
4. Create Service Account:
   - Go to "Credentials" → "Create Credentials" → "Service Account"
   - Click "Create Key" → Choose JSON → Download
   - Rename downloaded file to `credentials.json`
   - Place it in this project folder
5. Create a Google Sheet (or use existing)
6. Share the sheet with the service account email:
   - Open your sheet
   - Click "Share"
   - Add the email from `credentials.json` (look for `client_email`)
   - Give it "Editor" permission

## 3. Set Up Facebook Webhook (5 minutes)

1. Go to https://developers.facebook.com/
2. Create a new app or select existing
3. Add "Messenger" product
4. Set up Webhook:
   - Go to Messenger → Settings → Webhooks
   - Click "Add Callback URL"
   - **For local testing:** Use ngrok: `ngrok http 5000`
   - **Callback URL:** `https://your-ngrok-url.ngrok.io/webhook`
   - **Verify Token:** Create a random string (e.g., `my_secure_token_123`)
   - Subscribe to: `messages` checkbox
5. Save the Verify Token - you'll need it in the next step

## 4. Configure Environment (2 minutes)

1. Copy `config_example.env` to `.env`:
   ```bash
   copy config_example.env .env
   ```
   (On Linux/Mac: `cp config_example.env .env`)

2. Edit `.env` and set:
   ```
   FB_VERIFY_TOKEN=my_secure_token_123  # Same as Facebook webhook
   FB_PAGE_ACCESS_TOKEN=your_page_token  # From Facebook App > Messenger > Access Tokens
   GOOGLE_SHEET_ID=your_sheet_id_here   # From sheet URL
   ```

3. Get your Google Sheet ID from the URL:
   - Sheet URL looks like: `https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit`
   - Copy the `SHEET_ID_HERE` part

## 5. Run the Server (1 minute)

```bash
python app.py
```

The server will start on `http://localhost:5000`

## 6. Test It! (2 minutes)

1. **For local testing:** Start ngrok in another terminal:
   ```bash
   ngrok http 5000
   ```
   Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`)

2. **Update Facebook webhook** with your ngrok URL (if changed)

3. **Send a test message** to your Facebook Page

4. **Check your Google Sheet** - the message should appear automatically!

## Troubleshooting

### Webhook Verification Failed
- Make sure `FB_VERIFY_TOKEN` in `.env` matches the token you set in Facebook

### Messages Not Appearing in Sheets
- Check that `GOOGLE_SHEET_ID` is correct
- Verify the service account email has access to the sheet
- Check server logs for error messages

### Server Won't Start
- Make sure `credentials.json` is in the project folder
- Check that all dependencies are installed: `pip install -r requirements.txt`

## Next Steps

- For production: Deploy to Heroku, AWS, or any cloud service
- Enable Excel export: Set `EXCEL_EXPORT_ENABLED=true` in `.env`
- Check the full README.md for advanced configuration

