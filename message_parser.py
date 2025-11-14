"""
Message Parser for extracting structured data from Facebook messages
Extracts: Name, Contact Number, Purok, Barangay, Email, etc.
"""

import re
from typing import Dict, Optional, List

def extract_contact_number(text: str) -> Optional[str]:
    """Extract contact number from message text."""
    if not text:
        return None
    
    # Clean text: remove spaces, dashes, parentheses
    cleaned_text = text.replace(' ', '').replace('-', '').replace('(', '').replace(')', '').replace('+', '')
    
    # Patterns for Philippine phone numbers (11 digits starting with 09 or 10 digits)
    patterns = [
        r'09\d{9}',  # 09123456789 (11 digits)
        r'099\d{9}',  # 09912345678 (11 digits)
        r'\+639\d{9}',  # +639123456789
        r'639\d{9}',  # 639123456789
        r'0\d{10}',  # 10 digits starting with 0
    ]
    
    # First try patterns
    for pattern in patterns:
        matches = re.findall(pattern, cleaned_text)
        if matches:
            number = matches[0]
            # Format as 09xxxxxxxxx (11 digits)
            if number.startswith('639') and len(number) == 12:
                number = '0' + number[2:]
            elif number.startswith('63') and len(number) == 12:
                number = '0' + number[2:]
            if len(number) == 11 and number.startswith('09'):
                return number
            elif len(number) == 10 and number.startswith('0'):
                return number  # Already valid 10-digit number
    
    # Fallback: find any sequence of 10-11 digits that might be a phone number
    digits_only = re.findall(r'\d+', text)
    for digit_sequence in digits_only:
        if len(digit_sequence) == 11 and digit_sequence.startswith('09'):
            return digit_sequence
        elif len(digit_sequence) == 10 and digit_sequence.startswith('09'):
            # Might be missing one digit
            return '0' + digit_sequence
        elif len(digit_sequence) == 10:
            return digit_sequence
    
    return None

def extract_purok(text: str) -> Optional[str]:
    """Extract Purok information from message text."""
    if not text:
        return None
    
    # Case insensitive search
    text_lower = text.lower()
    
    # Patterns for purok (more flexible matching)
    patterns = [
        r'purok\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|barangay|brgy|$|\n)',
        r'prk\.?\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|barangay|brgy|$|\n)',
        r'taga\s+purok\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|barangay|brgy|$|\n)',
        r'purok\s+([a-záéíóúñü0-9\s\-]+)',  # Catch all pattern
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text_lower, re.IGNORECASE | re.MULTILINE)
        if match:
            purok = match.group(1).strip()
            # Clean up: remove extra spaces, remove "purok" if it appears again
            purok = re.sub(r'\bpurok\b', '', purok, flags=re.IGNORECASE).strip()
            purok = re.sub(r'\s+', ' ', purok)
            # Remove trailing punctuation
            purok = re.sub(r'[,\.;]+$', '', purok).strip()
            # Filter out very short matches and common false positives
            if purok and len(purok) > 2 and purok.lower() not in ['sa', 'ng', 'ang', 'the', 'is']:
                # Capitalize properly (preserve special characters)
                words = purok.split()
                capitalized_words = []
                for word in words:
                    if word:
                        capitalized_words.append(word[0].upper() + word[1:].lower())
                return ' '.join(capitalized_words)
    
    return None

def extract_barangay(text: str) -> Optional[str]:
    """Extract Barangay information from message text."""
    if not text:
        return None
    
    text_lower = text.lower()
    
    # Patterns for barangay (more flexible matching)
    patterns = [
        r'barangay\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|purok|prk|$|\n)',
        r'brgy\.?\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|purok|prk|$|\n)',
        r'barangay\s+([a-záéíóúñü0-9\s\-]+?)(?:purok|prk|$)',
        r'brgy\.?\s+([a-záéíóúñü0-9\s\-]+?)(?:purok|prk|$)',
        r'taga\s+barangay\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|purok|prk|$|\n)',
        r'taga\s+brgy\.?\s+([a-záéíóúñü0-9\s\-]+?)(?:,|\.|purok|prk|$|\n)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text_lower, re.IGNORECASE | re.MULTILINE)
        if match:
            barangay = match.group(1).strip()
            # Clean up: remove "barangay" or "brgy" if it appears again
            barangay = re.sub(r'\b(barangay|brgy)\b', '', barangay, flags=re.IGNORECASE).strip()
            barangay = re.sub(r'\s+', ' ', barangay)
            # Remove trailing punctuation
            barangay = re.sub(r'[,\.;]+$', '', barangay).strip()
            # Filter out very short matches and common false positives
            if barangay and len(barangay) > 2 and barangay.lower() not in ['sa', 'ng', 'ang', 'the', 'is']:
                # Capitalize properly (preserve special characters)
                words = barangay.split()
                capitalized_words = []
                for word in words:
                    if word:
                        capitalized_words.append(word[0].upper() + word[1:].lower())
                return ' '.join(capitalized_words)
    
    return None

def extract_email(text: str) -> Optional[str]:
    """Extract email address from message text."""
    if not text:
        return None
    
    # Standard email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    match = re.search(email_pattern, text)
    
    if match:
        return match.group(0).lower()
    
    return None

def get_attachment_urls(attachments: Optional[List[Dict]]) -> Optional[str]:
    """Extract attachment URLs from message attachments."""
    if not attachments or not isinstance(attachments, list):
        return None
    
    urls = []
    for attachment in attachments:
        if isinstance(attachment, dict):
            # Check for image/picture attachments
            if attachment.get('type') in ['image', 'file']:
                url = None
                # Try different possible structures
                payload = attachment.get('payload', {})
                if isinstance(payload, dict):
                    url = payload.get('url') or payload.get('uri')
                if url:
                    urls.append(url)
    
    return ', '.join(urls) if urls else None

def parse_message_data(message_text: str, sender_name: str, attachments: Optional[List[Dict]] = None) -> Dict:
    """
    Parse message data and extract structured information.
    
    Returns:
        Dictionary with extracted fields:
        - name: Sender name
        - contact_number: Extracted phone number
        - purok: Extracted purok
        - barangay: Extracted barangay
        - mensahe: Full message text
        - attachment_url: Attachment URLs
        - email: Extracted email address
        - status: Default status
    """
    if not message_text:
        message_text = ''
    
    # Extract structured data
    contact_number = extract_contact_number(message_text)
    purok = extract_purok(message_text)
    barangay = extract_barangay(message_text)
    email = extract_email(message_text)
    attachment_url = get_attachment_urls(attachments)
    
    return {
        'name': sender_name or 'Unknown',
        'contact_number': contact_number or '',
        'purok': purok or '',
        'barangay': barangay or '',
        'mensahe': message_text.strip(),
        'attachment_url': attachment_url or '',
        'email': email or '',
        'status': 'New Message'
    }

