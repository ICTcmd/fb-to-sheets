"""
Facebook Page Messages to Google Sheets Automation
This server handles webhooks from Facebook Messenger and automatically
saves messages to Google Sheets.
"""

import os
import json
import logging
from flask import Flask, request, jsonify
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Facebook Webhook Verification Token (set in environment variable)
VERIFY_TOKEN = os.environ.get('FB_VERIFY_TOKEN', 'your_verify_token_here')

# Google Sheets Configuration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file"
]

# Initialize Google Sheets client
def init_google_sheets():
    """Initialize Google Sheets client using service account credentials."""
    try:
        creds_file = os.environ.get('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
        
        if not os.path.exists(creds_file):
            logger.error(f"Google credentials file not found: {creds_file}")
            logger.error("Please download your service account credentials and save as credentials.json")
            return None
        
        creds = Credentials.from_service_account_file(creds_file, scopes=SCOPE)
        client = gspread.authorize(creds)
        logger.info("Google Sheets client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Error initializing Google Sheets: {str(e)}")
        return None

# Initialize Google Sheets client
gs_client = init_google_sheets()

# Google Sheets Configuration
SPREADSHEET_ID = os.environ.get('GOOGLE_SHEET_ID', '')
SHEET_NAME = os.environ.get('GOOGLE_SHEET_NAME', 'Messages')

# Excel Export Configuration (Optional)
EXCEL_EXPORT_ENABLED = os.environ.get('EXCEL_EXPORT_ENABLED', 'false').lower() == 'true'
EXCEL_FILENAME = os.environ.get('EXCEL_FILENAME', 'fb_messages.xlsx')

def get_or_create_sheet():
    """Get or create the messages sheet with headers."""
    try:
        spreadsheet = gs_client.open_by_key(SPREADSHEET_ID) if SPREADSHEET_ID else None
        if not spreadsheet:
            # If no ID provided, try to open by title
            spreadsheet_name = os.environ.get('GOOGLE_SHEET_NAME', 'FB Messages')
            try:
                spreadsheet = gs_client.open(spreadsheet_name)
            except:
                # Create new spreadsheet if it doesn't exist
                spreadsheet = gs_client.create(spreadsheet_name)
                logger.info(f"Created new spreadsheet: {spreadsheet_name}")
                logger.info(f"Spreadsheet ID: {spreadsheet.id}")
                logger.info(f"Please set GOOGLE_SHEET_ID={spreadsheet.id} in your environment")
        
        # Get or create the sheet
        try:
            worksheet = spreadsheet.worksheet(SHEET_NAME)
            # Check if headers exist, if not, add them
            try:
                first_row = worksheet.row_values(1)
                expected_headers = ['Timestamp', 'Name', 'Contact Number', 'Purok', 'Barangay', 'Mensahe', 'Please Upload Picture', 'Email Address', 'Status']
                if first_row != expected_headers:
                    logger.info("Headers don't match. Adding correct headers...")
                    worksheet.clear()
                    worksheet.append_row(expected_headers)
            except:
                # If sheet is empty, add headers
                headers = ['Timestamp', 'Name', 'Contact Number', 'Purok', 'Barangay', 'Mensahe', 'Please Upload Picture', 'Email Address', 'Status']
                worksheet.append_row(headers)
        except:
            worksheet = spreadsheet.add_worksheet(title=SHEET_NAME, rows=1000, cols=10)
            # Add headers
            headers = ['Timestamp', 'Name', 'Contact Number', 'Purok', 'Barangay', 'Mensahe', 'Please Upload Picture', 'Email Address', 'Status']
            worksheet.append_row(headers)
            logger.info(f"Created new sheet: {SHEET_NAME}")
        
        return worksheet
    except Exception as e:
        logger.error(f"Error getting/creating sheet: {str(e)}")
        return None

def save_message_to_sheets(message_data):
    """Save message data to Google Sheets with parsed structured data."""
    if not gs_client:
        logger.error("Google Sheets client not initialized")
        return False
    
    try:
        worksheet = get_or_create_sheet()
        if not worksheet:
            logger.error("Could not get or create worksheet")
            return False
        
        # Import message parser
        from message_parser import parse_message_data
        
        # Extract basic message information
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sender_name = message_data.get('from', {}).get('name', 'Unknown')
        message_text = message_data.get('message', {}).get('text', '')
        attachments = message_data.get('message', {}).get('attachments', [])
        
        # Parse message to extract structured data
        parsed_data = parse_message_data(message_text, sender_name, attachments)
        
        # Prepare row data according to your sheet format
        row = [
            timestamp,                          # Timestamp
            parsed_data['name'],                # Name
            parsed_data['contact_number'],      # Contact Number
            parsed_data['purok'],               # Purok
            parsed_data['barangay'],            # Barangay
            parsed_data['mensahe'],             # Mensahe (Message)
            parsed_data['attachment_url'],      # Please Upload Picture (Attachment URL)
            parsed_data['email'],               # Email Address
            parsed_data['status']               # Status
        ]
        
        # Append to sheet
        worksheet.append_row(row)
        logger.info(f"Message saved to Google Sheets from {parsed_data['name']}")
        return True
    except Exception as e:
        logger.error(f"Error saving message to sheets: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return False

def save_message_to_excel(message_data):
    """Save message data to Excel file (optional)."""
    if not EXCEL_EXPORT_ENABLED:
        return True  # Excel export disabled, not an error
    
    try:
        from excel_export import append_to_excel
        result = append_to_excel(EXCEL_FILENAME, message_data)
        if result:
            logger.info(f"Message saved to Excel: {message_data.get('id', '')}")
        return result
    except Exception as e:
        logger.error(f"Error saving message to Excel: {str(e)}")
        return False

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """
    Webhook verification endpoint for Facebook.
    Facebook will send a GET request to verify the webhook.
    """
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if mode == 'subscribe' and token == VERIFY_TOKEN:
        logger.info("Webhook verified successfully")
        return challenge, 200
    else:
        logger.warning("Webhook verification failed")
        return jsonify({'error': 'Verification failed'}), 403

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    Handle incoming webhook events from Facebook.
    This endpoint receives message events and saves them to Google Sheets.
    """
    try:
        data = request.get_json()
        
        if data.get('object') == 'page':
            entries = data.get('entry', [])
            
            for entry in entries:
                messaging_events = entry.get('messaging', [])
                
                for event in messaging_events:
                    # Check if this is a message event
                    if 'message' in event:
                        # Get sender information
                        sender_id = event['sender']['id']
                        
                        # Get message text (might be empty for attachments)
                        message_text = event['message'].get('text', '')
                        
                        # Get attachments if present
                        attachments = event['message'].get('attachments', [])
                        
                        # Try to get sender name from Facebook Graph API
                        try:
                            from facebook_api import get_sender_name, extract_name_from_message
                            sender_name = get_sender_name(sender_id)
                            # If Graph API didn't return a name, try extracting from message
                            if sender_name == 'Unknown' and message_text:
                                extracted_name = extract_name_from_message(message_text)
                                if extracted_name:
                                    sender_name = extracted_name
                        except Exception as e:
                            logger.warning(f"Could not fetch sender name: {str(e)}")
                            sender_name = 'User'
                        
                        message_data = {
                            'id': event.get('message', {}).get('mid', ''),
                            'from': {
                                'id': sender_id,
                                'name': sender_name
                            },
                            'message': {
                                'text': message_text,
                                'attachments': attachments
                            },
                            'to': {
                                'data': [{
                                    'id': event['recipient']['id']
                                }]
                            }
                        }
                        
                        # Only process if message has text or attachments
                        if message_text or attachments:
                            # Save to Google Sheets
                            sheets_success = save_message_to_sheets(message_data)
                            
                            # Save to Excel (if enabled)
                            excel_success = save_message_to_excel(message_data)
                            
                            if sheets_success:
                                logger.info(f"Processed message from {sender_id}")
                            else:
                                logger.error(f"Failed to save message from {sender_id}")
        
        return jsonify({'status': 'success'}), 200
        
    except Exception as e:
        logger.error(f"Error handling webhook: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'google_sheets': 'initialized' if gs_client else 'not_initialized'
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

