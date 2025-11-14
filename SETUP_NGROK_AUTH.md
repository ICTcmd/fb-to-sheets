# Setup ngrok Authentication - Free Account Required

## ✅ ngrok Needs Authentication

ngrok requires a free account to use. Here's how to set it up:

---

## Step 1: Sign Up for ngrok Account (Free)

1. **Go to:** https://dashboard.ngrok.com/signup
2. **Sign up** with:
   - Your email
   - Password
   - Or use Google/GitHub to sign in

3. **Verify your email** if needed

---

## Step 2: Get Your Authtoken

1. **After signing up**, you'll be taken to the dashboard
2. **Go to:** https://dashboard.ngrok.com/get-started/your-authtoken
3. **Copy your authtoken** - it will look like:
   ```
   ngrok authtoken 2abc123xyz456...
   ```

---

## Step 3: Configure ngrok with Your Authtoken

**In your PowerShell terminal, run:**

```powershell
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

Replace `YOUR_AUTHTOKEN_HERE` with the actual authtoken you copied.

**Example:**
```powershell
ngrok config add-authtoken 2abc123xyz456def789...
```

---

## Step 4: Start ngrok

After configuring the authtoken, start ngrok:

```powershell
ngrok http 5000
```

You should now see:
```
Forwarding    https://abc123xyz.ngrok.io -> http://localhost:5000
```

---

## Alternative: If You Already Have an Account

If you already have an ngrok account:

1. **Log in:** https://dashboard.ngrok.com/
2. **Get authtoken:** https://dashboard.ngrok.com/get-started/your-authtoken
3. **Run:** `ngrok config add-authtoken YOUR_AUTHTOKEN`

---

## Quick Steps Summary:

1. ✅ Sign up at: https://dashboard.ngrok.com/signup
2. ✅ Get authtoken at: https://dashboard.ngrok.com/get-started/your-authtoken
3. ✅ Run: `ngrok config add-authtoken YOUR_AUTHTOKEN`
4. ✅ Run: `ngrok http 5000`
5. ✅ Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`)

---

## After Getting ngrok Running:

1. **Copy your ngrok HTTPS URL** (e.g., `https://abc123.ngrok.io`)
2. **Go back to Facebook webhook configuration**
3. **Update Callback URL:** `https://your-ngrok-url.ngrok.io/webhook`
4. **Click "Verify and save"**
5. **Test it!**

---

**Ready?** Sign up at https://dashboard.ngrok.com/signup and get your authtoken! 🚀

