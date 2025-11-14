# Add Verify Token to Webhook

## ✅ Webhook URL is Set!

I can see:
- **Callback URL:** `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook` ✅
- **Verify Token:** Empty field ❌ - Need to fill this!

---

## Step 1: Create a Verify Token

**A Verify Token is a secret string** that Facebook will use to verify your webhook.

**You can use any random string**, for example:
- `my_secure_token_123`
- `fb_webhook_verify_2024`
- `secret_token_xyz`
- Or any combination of letters and numbers

**Choose something you'll remember** because:
1. You'll enter it in Facebook webhook configuration
2. You'll also need to put it in your `.env` file as `FB_VERIFY_TOKEN`
3. They must match!

---

## Step 2: Enter Verify Token in Facebook

1. **Click in the "Verify token" field** (below Callback URL)

2. **Type your verify token**, for example:
   ```
   my_secure_token_123
   ```

3. **Remember this token!** Write it down or save it somewhere - you'll need it for `.env` file

---

## Step 3: Save Same Token to `.env` File

**Important:** The Verify Token in Facebook MUST match the one in your `.env` file!

1. **Create or edit `.env` file** in your project folder:
   ```powershell
   copy config_example.env .env
   ```

2. **Edit `.env` file** and add:
   ```env
   FB_VERIFY_TOKEN=my_secure_token_123
   ```

   **Replace `my_secure_token_123`** with the EXACT token you just entered in Facebook!

3. **Save the `.env` file**

---

## Step 4: Verify and Save

After entering the Verify Token:

1. **Make sure your server is running** (`python app.py` in Terminal 1)
2. **Make sure ngrok is running** (in Terminal 2)

3. **Click the blue "Verify and save" button** (bottom right)

4. **If verification succeeds:**
   - You'll see a success message
   - The webhook is connected!
   - The webhook fields table will populate

5. **If verification fails:**
   - Check that your server is running
   - Check that ngrok is running
   - Make sure the Verify Token in Facebook matches the one in `.env` file
   - Check server terminal for error messages

---

## Quick Example:

**In Facebook Webhook:**
- Verify Token: `my_secure_token_123`

**In your `.env` file:**
```env
FB_VERIFY_TOKEN=my_secure_token_123
```

**They must be EXACTLY the same!**

---

## Step 5: After Verification - Subscribe to Fields

After successfully verifying the webhook:

1. **Scroll down to "Webhook fields" table**

2. **Look for `messages` field** in the list
   - You might need to scroll or search for it
   - It might not be at the top (I see `affiliation` and `attire` in the list)

3. **Find `messages` field:**
   - Use the scrollbar on the right
   - Or use Ctrl+F to search for "messages"

4. **Toggle the "Subscribe" switch** for `messages` field to ON (green)

5. **Click "Save"** or similar button

---

## Step 6: Subscribe Your Page

1. **Look for "Add Subscriptions" or "Subscribe" section**

2. **Select your Facebook Page** from dropdown

3. **Click "Subscribe"**

---

## Quick Action Plan:

1. ✅ **Enter Verify Token:** Type `my_secure_token_123` (or your chosen token)
2. ✅ **Save to `.env`:** Add `FB_VERIFY_TOKEN=my_secure_token_123`
3. ✅ **Click "Verify and save"**
4. ✅ **Find `messages` field** in the webhook fields table
5. ✅ **Subscribe to `messages`**
6. ✅ **Subscribe your Page**
7. ✅ **Get Page Access Token**

---

**First, enter a Verify Token in the empty field, then click "Verify and save"!** 🚀

