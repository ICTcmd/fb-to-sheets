# Webhook Setup Guide - You're Almost Done! ✅

## ✅ You're on the Webhooks Configuration Page!

I can see:
- **Callback URL:** Currently has a Make.com URL
- **Verify Token:** Already filled in (masked)
- **Buttons:** "Remove subscription" and "Verify and save"

---

## Step 1: Update Callback URL (For Your Local Server)

**The current URL** (`https://hook.eu2.make.com/...`) is for Make.com.

**You need to change it to your local server URL:**

### For Local Testing (with ngrok):

1. **First, you'll need to:**
   - Set up ngrok (see next steps)
   - Start your Python server (`python app.py`)
   - Start ngrok (`ngrok http 5000`)
   - Get your ngrok HTTPS URL (e.g., `https://abc123.ngrok.io`)

2. **Then update the Callback URL:**
   - Replace the current URL with: `https://your-ngrok-url.ngrok.io/webhook`
   - Example: `https://abc123xyz.ngrok.io/webhook`

### For Production:

- Use your actual server URL + `/webhook`
- Example: `https://yourdomain.com/webhook`

---

## Step 2: Check/Update Verify Token

1. **The Verify Token is already filled in** (shown as dots)
2. **Click in the field** to see/unmask the token (if needed)
3. **Write down this token** - You'll need it for your `.env` file as `FB_VERIFY_TOKEN`
4. **If you want to change it:**
   - Type a new token (e.g., `my_secure_token_123`)
   - Make sure it matches what you'll put in your `.env` file

---

## Step 3: Subscribe to Events

**Look for "Subscribe to fields" or "Subscribe to events" section:**

1. **Find checkboxes** for events like:
   - ✅ **`messages`** - CHECK THIS! (Required)
   - ✅ `messaging_postbacks` (Optional but recommended)
   - ✅ `message_deliveries` (Optional)
   - ✅ `message_reads` (Optional)

2. **Make sure `messages` is checked!**

---

## Step 4: Verify and Save

1. **After updating Callback URL and checking events:**
   - Click **"Verify and save"** button (blue button, bottom right)

2. **If verification fails:**
   - Make sure your server is running
   - Make sure ngrok is running (if testing locally)
   - Check that the URL ends with `/webhook`
   - Verify token must match what's in your server's `.env` file

---

## Step 5: Subscribe Your Page

**After saving the webhook:**

1. **Look for "Add Subscriptions" or "Subscribe" section**
2. **Select your Facebook Page** from dropdown
3. **Click "Subscribe"**

---

## Step 6: Get Page Access Token

**Now you need to get your Page Access Token:**

1. **Look for "Access Tokens" section** (might be on same page or sidebar)
2. **Or click "Permissions and features"** in the left panel
3. **Find "Generate Token" button**
4. **Select your Facebook Page** from dropdown
5. **Click "Generate Token"**
6. **COPY THE TOKEN** - Save it securely!
7. Use in your `.env` file as `FB_PAGE_ACCESS_TOKEN`

---

## Important Notes:

⚠️ **Warning Box Notice:**
- While your app is unpublished, you can only receive test webhooks
- For production data, you'll need to publish the app later
- For now, this is fine for testing!

---

## What to Save:

After configuration, you'll need these for your `.env` file:

1. **Verify Token** (from the Verify Token field)
   - Use as: `FB_VERIFY_TOKEN=your_token_here`

2. **Page Access Token** (after generating)
   - Use as: `FB_PAGE_ACCESS_TOKEN=your_page_token_here`

---

## Next Steps After Webhook Setup:

1. **Update `.env` file** with tokens
2. **Start your server:** `python app.py`
3. **Start ngrok:** `ngrok http 5000` (in separate terminal)
4. **Update webhook URL** in Facebook if ngrok URL changes
5. **Test it!** Send a message to your Facebook Page

---

## Quick Action Plan:

1. **For now:** Update Callback URL to use a placeholder or wait until ngrok is set up
2. **Save the Verify Token** you see (or change it if needed)
3. **Check `messages` event** is subscribed
4. **Click "Verify and save"**
5. **Get Page Access Token**

**Do you want to set up ngrok first, or configure the webhook now with a placeholder?** 🚀

