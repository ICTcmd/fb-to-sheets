# Update Webhook URL in Facebook

## ⚠️ Your Callback URL is Still Pointing to Make.com!

**Current Callback URL:**
```
https://hook.eu2.make.com/7nlvmhsnbhv5tynbp81pb22ngw8lwenj
```

**This needs to be changed to your ngrok URL!**

---

## Step 1: Update Callback URL in Facebook

1. **On the Facebook webhook page**, find the **"Callback URL"** field

2. **Delete the Make.com URL:**
   - Select all text: `https://hook.eu2.make.com/7nlvmhsnbhv5tynbp81pb22ngw8lwenj`
   - Delete it

3. **Enter your ngrok URL:**
   ```
   https://radia-perissodactylous-cleo.ngrok-free.dev/webhook
   ```
   **Important:** Must end with `/webhook`

---

## Step 2: Check Verify Token

1. **The "Verify token" field** shows masked dots (`............`)

2. **Click in the field** to see/unmask the token

3. **Make sure it's:** `fb-messages` (or whatever you set it to)

4. **If it's different or empty:**
   - Enter: `fb-messages`
   - **Remember this!** You'll need it for `.env` file

---

## Step 3: Make Sure `.env` File Matches

**Your `.env` file must have:**

```env
FB_VERIFY_TOKEN=fb-messages
```

**Must match exactly what's in Facebook!**

---

## Step 4: Verify and Save

1. **Make sure:**
   - ✅ Server is running (`python app.py` in Terminal 1)
   - ✅ ngrok is running (`ngrok http 5000` in Terminal 2)
   - ✅ Callback URL updated to: `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook`
   - ✅ Verify Token is `fb-messages` (matching `.env`)

2. **Click the blue "Verify and save" button** (bottom right)

3. **Watch your server terminal** (Terminal 1) - You should see logs!

4. **If verification succeeds:**
   - ✅ Success message in Facebook
   - ✅ Webhook fields table will populate
   - ✅ You can now subscribe to fields

5. **If verification fails:**
   - Check server terminal for error messages
   - Make sure both server and ngrok are running
   - Make sure `.env` has correct token
   - Make sure URL ends with `/webhook`

---

## Step 5: After Successful Verification

Once verification succeeds:

1. **Scroll down to "Webhook fields" table**

2. **Find `messages` field:**
   - Scroll or search for "messages"

3. **Toggle "Subscribe" switch to ON** (green) for `messages`

4. **Click "Save"**

5. **Subscribe your Page:**
   - Find "Add Subscriptions" or "Subscribe"
   - Select your Facebook Page
   - Click "Subscribe"

---

## Quick Action:

1. **Update Callback URL:** Change to `https://radia-perissodactylous-cleo.ngrok-free.dev/webhook`
2. **Check Verify Token:** Make sure it's `fb-messages`
3. **Update `.env`:** Make sure it has `FB_VERIFY_TOKEN=fb-messages`
4. **Restart server** (if you updated `.env`)
5. **Click "Verify and save"** in Facebook

---

**Update the Callback URL to your ngrok URL, then click "Verify and save"!** 🚀

