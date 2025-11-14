"""
Facebook Graph API helper functions
Used to fetch sender profile information
"""

import os
import requests
import logging

logger = logging.getLogger(__name__)

def get_sender_name(sender_id: str, page_access_token: str = None) -> str:
    """
    Get sender's name from Facebook Graph API.
    
    Args:
        sender_id: Facebook user ID
        page_access_token: Page Access Token (from environment if not provided)
    
    Returns:
        Sender's name or 'Unknown' if not available
    """
    if not page_access_token:
        page_access_token = os.environ.get('FB_PAGE_ACCESS_TOKEN')
    
    if not page_access_token:
        logger.warning("Facebook Page Access Token not set. Cannot fetch sender names.")
        return 'Unknown'
    
    try:
        # Use Graph API to get user profile
        url = f"https://graph.facebook.com/v18.0/{sender_id}"
        params = {
            'fields': 'name,first_name,last_name',
            'access_token': page_access_token
        }
        
        response = requests.get(url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            name = data.get('name') or data.get('first_name', 'Unknown')
            logger.info(f"Fetched sender name: {name} for ID: {sender_id}")
            return name
        else:
            logger.warning(f"Failed to fetch sender name for {sender_id}: {response.status_code}")
            return 'Unknown'
            
    except Exception as e:
        logger.error(f"Error fetching sender name: {str(e)}")
        return 'Unknown'

def extract_name_from_message(text: str) -> str:
    """
    Try to extract name from message text (fallback method).
    Looks for patterns like "Hi, I'm John" or "This is John Doe"
    """
    if not text:
        return None
    
    text_lower = text.lower()
    
    # Common patterns for introducing oneself
    patterns = [
        r"(?:hi|hello|good morning|good afternoon|good evening)[\s,]+(?:i['']m|i am|this is|ako si|ako siya|ako kay|taga si)[\s,]+([a-z\s]+?)(?:\.|,|$|\n)",
        r"^([a-z\s]+?)[\s,]+(?:ako|taga|si|here)",
    ]
    
    import re
    for pattern in patterns:
        match = re.search(pattern, text_lower, re.IGNORECASE)
        if match:
            name = match.group(1).strip()
            # Clean up and capitalize
            name = ' '.join(word.capitalize() for word in name.split())
            if len(name) > 1 and len(name) < 50:  # Reasonable name length
                return name
    
    return None

