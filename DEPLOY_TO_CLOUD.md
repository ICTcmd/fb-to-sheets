# Deploy to Cloud - Free Options & Step-by-Step Guide! ☁️

## ✅ Why Deploy to Cloud?

**Benefits:**
- ✅ Always-on operation (24/7)
- ✅ No need for ngrok (server has public URL)
- ✅ More reliable (no 2-hour timeouts)
- ✅ Static URL (never changes)
- ✅ Free options available!
- ✅ Your computer can sleep/restart - app still runs!

---

## Free Cloud Hosting Options:

### Option 1: Railway (Recommended - $5 Free Credit/Month) ⭐

**Free Tier:**
- ✅ $5 credit/month (free)
- ✅ Enough for small apps
- ✅ Easy deployment
- ✅ Auto-deploy from GitHub

**Pros:**
- ✅ Very easy to use
- ✅ Good free tier
- ✅ Great documentation
- ✅ Auto-redeploy on code changes

**Cons:**
- ⚠️ $5 credit might run out for heavy usage
- ⚠️ Sleeps after inactivity (free tier)

**Best for:** Quick deployment, beginners

---

### Option 2: Render (Free Tier Available) ⭐

**Free Tier:**
- ✅ Free tier available
- ✅ Static URL
- ✅ Always-on (with limitations)

**Pros:**
- ✅ Free tier available
- ✅ Easy deployment
- ✅ Good documentation

**Cons:**
- ⚠️ Sleeps after 15 minutes of inactivity (free tier)
- ⚠️ Slow wake-up time (~30 seconds)

**Best for:** Small apps, low traffic

---

### Option 3: Fly.io (Free Tier Available)

**Free Tier:**
- ✅ Free tier available
- ✅ 3 shared-cpu VMs free
- ✅ 3GB persistent volumes

**Pros:**
- ✅ Generous free tier
- ✅ Global edge network
- ✅ Good performance

**Cons:**
- ⚠️ More complex setup
- ⚠️ Requires more configuration

**Best for:** Developers comfortable with CLI

---

### Option 4: PythonAnywhere (Free Tier Available)

**Free Tier:**
- ✅ Free tier available
- ✅ Good for Python apps
- ✅ Simple setup

**Pros:**
- ✅ Free tier available
- ✅ Made for Python
- ✅ Easy to use

**Cons:**
- ⚠️ Limited resources (free tier)
- ⚠️ Must visit site daily (free tier)

**Best for:** Python-specific apps, simple deployments

---

## Recommended: Railway (Easiest & Best Free Tier)

**Why Railway:**
- ✅ $5 free credit/month (enough for small apps)
- ✅ Easiest deployment
- ✅ Good documentation
- ✅ Auto-deploy from GitHub

---

## Step-by-Step: Deploy to Railway

### Prerequisites:
1. **GitHub account** (free)
2. **Railway account** (free signup)
3. **Your code** (already have this!)

---

### Step 1: Prepare Your Code

**You need to make a few small changes:**

#### 1.1: Create `Procfile` (Required for Railway)

**Create a new file in your project:** `Procfile` (no extension)

**Contents:**
```
web: python app.py
```

This tells Railway how to run your app.

#### 1.2: Create `runtime.txt` (Optional - Specifies Python Version)

**Create a new file:** `runtime.txt`

**Contents:**
```
python-3.11.0
```

Or whatever Python version you're using.

#### 1.3: Update `.env` to Use Environment Variables

**Railway uses environment variables (not `.env` file).**

Your code already uses `os.environ.get()` which works! ✅

You just need to set environment variables in Railway dashboard.

---

### Step 2: Create GitHub Repository

**If you haven't already:**

1. **Go to GitHub:** https://github.com
2. **Sign up** (if you don't have account)
3. **Create new repository:**
   - Click "New" or "+" → "New repository"
   - Name: `fb-to-sheets` (or any name)
   - Description: "Facebook Messages to Google Sheets"
   - **Public** or **Private** (your choice)
   - **Don't** initialize with README (we have files already)
   - Click "Create repository"

4. **Upload your code:**
   - Download **GitHub Desktop** (easiest): https://desktop.github.com
   - Or use Git commands:
     ```bash
     cd "C:\Users\ACER\Desktop\FB to Sheets"
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/fb-to-sheets.git
     git push -u origin main
     ```
   - Replace `YOUR_USERNAME` with your GitHub username

**⚠️ Important:** Don't commit `credentials.json` or `.env` to GitHub!

**Create `.gitignore` file:**
```
credentials.json
.env
*.pyc
__pycache__/
*.log
```

---

### Step 3: Sign Up for Railway

1. **Go to Railway:** https://railway.app
2. **Click "Login" or "Start a New Project"**
3. **Sign up with GitHub** (easiest)
4. **Authorize Railway** to access GitHub

---

### Step 4: Deploy from GitHub

1. **In Railway dashboard:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"

2. **Select your repository:**
   - Choose `fb-to-sheets` (or your repo name)
   - Click "Deploy"

3. **Railway will:**
   - Detect Python app
   - Install dependencies from `requirements.txt`
   - Start your app

---

### Step 5: Configure Environment Variables

**This is IMPORTANT - Set all your secrets:**

1. **In Railway project dashboard:**
   - Click on your deployed service
   - Go to "Variables" tab

2. **Add these environment variables:**
   ```
   FB_VERIFY_TOKEN=fb-messages
   FB_PAGE_ACCESS_TOKEN=your_actual_page_token
   GOOGLE_SHEET_ID=1UKxylEP4Mp2grH_-ikbYK5fd4Cotxayd5F8K54gEfJM
   GOOGLE_SHEET_NAME=Messages
   GOOGLE_CREDENTIALS_FILE=credentials.json
   EXCEL_EXPORT_ENABLED=false
   PORT=5000
   ```

3. **Add Google Credentials:**
   - **Option A:** Upload `credentials.json` file
     - In Railway dashboard → Variables
     - Click "Add Variable"
     - Name: `GOOGLE_CREDENTIALS_JSON`
     - Value: Copy entire contents of `credentials.json` file
   
   - **Option B:** Use Railway's file upload
     - Upload `credentials.json` file
     - Railway will handle it

**⚠️ Important:** Make sure all variables are set correctly!

---

### Step 6: Update Facebook Webhook URL

**After Railway deploys:**

1. **Get your Railway URL:**
   - Railway provides a public URL like: `https://your-app.railway.app`
   - Find it in Railway dashboard → "Settings" → "Domains"

2. **Update Facebook webhook:**
   - Go to Facebook Developer Console
   - Messenger → Settings → Webhooks
   - Update Callback URL to: `https://your-app.railway.app/webhook`
   - Verify Token: `fb-messages` (same as before)
   - Click "Verify and save"

3. **Done!** Your app is now running in cloud! ✅

---

## Alternative: Deploy to Render (Free Tier)

### Step 1: Create GitHub Repository (Same as above)

### Step 2: Sign Up for Render

1. **Go to Render:** https://render.com
2. **Sign up** (free)
3. **Connect GitHub** account

### Step 3: Create Web Service

1. **In Render dashboard:**
   - Click "New" → "Web Service"
   - Select your GitHub repository

2. **Configure:**
   - **Name:** `fb-to-sheets`
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** (leave empty)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

3. **Set Environment Variables:**
   - Same as Railway (FB_VERIFY_TOKEN, GOOGLE_SHEET_ID, etc.)
   - Add `credentials.json` as secret file

4. **Click "Create Web Service"**

5. **Render will deploy** (takes a few minutes)

6. **Get URL:**
   - Render provides: `https://your-app.onrender.com`
   - Update Facebook webhook URL

---

## Comparing Free Options:

| Platform | Free Tier | Ease of Use | Always-On | Best For |
|----------|-----------|-------------|-----------|----------|
| **Railway** | $5 credit/month | ⭐⭐⭐⭐⭐ | ✅ (with credit) | Beginners |
| **Render** | Yes (sleeps) | ⭐⭐⭐⭐ | ⚠️ (sleeps 15min) | Small apps |
| **Fly.io** | 3 VMs free | ⭐⭐⭐ | ✅ | Developers |
| **PythonAnywhere** | Yes (daily visit) | ⭐⭐⭐⭐ | ⚠️ (daily visit) | Python apps |

---

## My Recommendation:

**Start with Railway:**
- ✅ Easiest to use
- ✅ $5 free credit/month
- ✅ Best documentation
- ✅ Good for beginners

**If Railway credit runs out:**
- Try Render (free tier available)
- Or consider paid Railway ($5/month)

---

## Quick Checklist:

### Before Deploying:
- [ ] Create `Procfile` with `web: python app.py`
- [ ] Create `.gitignore` (exclude `credentials.json` and `.env`)
- [ ] Create GitHub repository
- [ ] Upload code to GitHub
- [ ] **Don't commit credentials.json or .env!**

### During Deployment:
- [ ] Sign up for Railway/Render
- [ ] Deploy from GitHub
- [ ] Set environment variables
- [ ] Add Google credentials

### After Deployment:
- [ ] Get cloud URL
- [ ] Update Facebook webhook URL
- [ ] Test with a message
- [ ] Verify it works!

---

## Cost Summary:

**Railway (Recommended):**
- Free: $5 credit/month ✅
- After credit: ~$5/month (if usage continues)

**Render:**
- Free: Free tier (with limitations) ✅
- Paid: $7/month (always-on)

**Fly.io:**
- Free: 3 VMs free ✅
- Paid: Pay as you go

---

## Quick Start: Railway (Fastest)

**Want me to help you create the files needed for Railway deployment?**
- `Procfile`
- `.gitignore`
- `runtime.txt` (optional)

**Just let me know and I'll create them for you!** 🚀

---

**Railway is the easiest and has the best free tier. Want step-by-step help deploying?** 😊

