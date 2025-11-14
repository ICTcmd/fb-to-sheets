# Facebook Page Messages to Google Sheets Automation

This system automatically captures messages from your Facebook Page and saves them to Google Sheets in real-time.

## Features

- ✅ Automatic message capture from Facebook Page
- ✅ Real-time data entry into Google Sheets
- ✅ Optional Excel export functionality
- ✅ Webhook-based architecture (no polling needed)
- ✅ Easy setup and configuration
- ✅ Support for message text, sender info, timestamps

## Prerequisites

1. **Python 3.7+** installed on your system
2. **Facebook Page** with admin access
3. **Facebook App** (to set up webhooks)
4. **Google Cloud Project** with Sheets API enabled
5. **Google Service Account** credentials
6. **Public URL** for webhooks (use ngrok for local testing)

## Setup Instructions

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Set Up Google Sheets API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable **Google Sheets API** and **Google Drive API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Sheets API" and enable it
   - Search for "Google Drive API" and enable it
4. Create a Service Account:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "Service Account"
   - Create the service account and download the JSON key file
   - Rename it to `credentials.json` and place it in the project root
5. Share your Google Sheet with the service account email:
   - Open your Google Sheet (or create a new one)
   - Click "Share" and add the service account email (found in credentials.json)
   - Give it "Editor" permissions

### Step 3: Configure Environment Variables

1. Copy `config_example.env` to `.env` (recommended for local development)
2. Set the following variables:
   - `FB_VERIFY_TOKEN`: A random string for webhook verification (same as Facebook webhook)
   - `FB_PAGE_ACCESS_TOKEN`: Your Facebook Page Access Token (for fetching sender names)
   - `GOOGLE_SHEET_ID`: Your Google Sheet ID (found in the sheet URL)
   - `GOOGLE_SHEET_NAME`: Name of the worksheet (default: "Messages")
   - `GOOGLE_CREDENTIALS_FILE`: Path to credentials.json (default: "credentials.json")
   - `EXCEL_EXPORT_ENABLED`: Set to "true" to also save to Excel (optional)
   - `EXCEL_FILENAME`: Name of Excel file (default: "fb_messages.xlsx")

### Step 4: Set Up Facebook Webhook

1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create a new app or use an existing one
3. Add "Messenger" product to your app
4. Configure Webhooks:
   - Go to Messenger > Settings > Webhooks
   - Click "Add Callback URL"
   - Enter your webhook URL: `https://your-domain.com/webhook`
   - Enter your Verify Token (same as `FB_VERIFY_TOKEN`)
   - Subscribe to: `messages` and `messaging_postbacks`
5. Get Page Access Token:
   - Go to Messenger > Settings > Access Tokens
   - Generate a token for your page
   - Copy the token and save it in your `.env` file as `FB_PAGE_ACCESS_TOKEN`
   - This token is used to fetch sender names from Facebook profiles

### Step 5: Make Your Server Accessible

For local testing, use **ngrok**:

```bash
# Install ngrok: https://ngrok.com/download
ngrok http 5000
```

Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`) and use it in your Facebook webhook callback URL.

For production, deploy to:
- Heroku
- AWS Lambda
- Google Cloud Run
- DigitalOcean App Platform
- Any hosting service that supports Python/Flask

### Step 6: Verify Setup (Optional but Recommended)

Before running the server, verify your setup:

```bash
python test_setup.py
```

This will check:
- Python dependencies
- Environment variables
- Google credentials and sheet access

### Step 7: Run the Server

```bash
python app.py
```

Or with environment variables:

```bash
export FB_VERIFY_TOKEN=your_token
export GOOGLE_SHEET_ID=your_sheet_id
python app.py
```

## Data Format

Messages are automatically parsed and saved to Google Sheets with the following columns:

| Timestamp | Name | Contact Number | Purok | Barangay | Mensahe | Please Upload Picture | Email Address | Status |
|-----------|------|----------------|-------|----------|---------|----------------------|---------------|--------|
| 2025-10-15 02:15:51 | Joy Parreño | 09914567842 | Purok Cadena De Amor | Brgy Abuanan | Good morning sir... | (URL if attached) | (email if provided) | New Message |

The system automatically extracts:
- **Name**: From Facebook profile (via Graph API) or message content
- **Contact Number**: Phone numbers (Philippine format: 09xxxxxxxxx)
- **Purok**: Detected from patterns like "purok X" or "prk X"
- **Barangay**: Detected from patterns like "barangay X" or "brgy X"
- **Mensahe**: Full message text
- **Please Upload Picture**: URLs of attached images/files
- **Email Address**: Email addresses found in messages
- **Status**: Default "New Message" (can be customized)

## Testing

1. Send a test message to your Facebook Page
2. Check your Google Sheet - the message should appear automatically
3. Check server logs for any errors

## Troubleshooting

### Webhook Verification Failed
- Ensure `FB_VERIFY_TOKEN` matches in both your app and Facebook webhook settings
- Check that your server is accessible from the internet

### Google Sheets Not Updating
- Verify `credentials.json` is in the correct location
- Check that the service account email has edit access to the sheet
- Verify `GOOGLE_SHEET_ID` is correct (from the sheet URL)
- Check server logs for error messages

### Messages Not Received
- Verify webhook is subscribed to `messages` event
- Check that your page has messages enabled
- Ensure your webhook URL is accessible and returns 200 status
- Check Facebook App Dashboard for webhook delivery logs

## Security Notes

- **Never commit** `credentials.json` to version control
- Use environment variables for sensitive tokens
- Add `credentials.json` to `.gitignore`
- Use HTTPS in production
- Rotate access tokens periodically

## Advanced Features (Future Enhancements)

- Support for attachments/images
- Sender profile name fetching
- Reply automation
- Message filtering/routing
- Excel export option
- Database backup

## License

This project is provided as-is for personal and commercial use.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review Facebook Messenger Platform documentation
3. Review Google Sheets API documentation

