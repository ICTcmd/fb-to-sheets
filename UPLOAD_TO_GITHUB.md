# Upload Your Code to GitHub - Step by Step! ✅

## ✅ Repository Created Successfully!

**Your repository:** `https://github.com/ICTcmd/fb-to-sheets`

**Now let's upload your code!**

---

## Step 1: Open PowerShell in Your Project Folder

**You're already in the right directory:**
```
C:\Users\ACER\Desktop\FB to Sheets
```

**If not, navigate there:**
```powershell
cd "C:\Users\ACER\Desktop\FB to Sheets"
```

---

## Step 2: Check if Git is Installed

**First, check if Git is installed:**
```powershell
git --version
```

**If Git is not installed:**
1. Download Git: https://git-scm.com/download/win
2. Install it (default settings are fine)
3. Restart PowerShell
4. Try again

---

## Step 3: Initialize Git Repository (If Not Already)

**Check if git is already initialized:**
```powershell
git status
```

**If it shows "not a git repository":**
```powershell
git init
```

**If it shows your files, Git is already initialized! ✅**

---

## Step 4: Add All Files to Git

**Add all your files (except those in .gitignore):**
```powershell
git add .
```

**This adds all files EXCEPT:**
- `credentials.json` (excluded by .gitignore ✅)
- `.env` (excluded by .gitignore ✅)
- Other files in .gitignore

**⚠️ Important:** `.gitignore` ensures secrets are NOT uploaded!

---

## Step 5: Check What Will Be Uploaded

**Verify what files will be committed (optional but recommended):**
```powershell
git status
```

**You should see:**
- All your `.py` files ✅
- `Procfile` ✅
- `requirements.txt` ✅
- `README.md` ✅
- `.gitignore` ✅
- Other documentation files ✅
- **NOT** `credentials.json` ✅
- **NOT** `.env` ✅

**If you see `credentials.json` or `.env` listed, STOP! Check your .gitignore file!**

---

## Step 6: Commit Your Files

**Create your first commit:**
```powershell
git commit -m "Initial commit: Facebook to Google Sheets automation"
```

**You should see:**
```
[main (root-commit) xxxxx] Initial commit: Facebook to Google Sheets automation
 X files changed, XXX insertions(+)
```

---

## Step 7: Set Branch to Main

**Ensure you're on the main branch:**
```powershell
git branch -M main
```

---

## Step 8: Add Remote Repository

**Connect to your GitHub repository:**
```powershell
git remote add origin https://github.com/ICTcmd/fb-to-sheets.git
```

**If you get "remote origin already exists" error:**
```powershell
git remote set-url origin https://github.com/ICTcmd/fb-to-sheets.git
```

---

## Step 9: Push to GitHub

**Upload your code:**
```powershell
git push -u origin main
```

**If prompted for credentials:**
- **Username:** Your GitHub username (`ICTcmd`)
- **Password:** Use a **Personal Access Token** (not your GitHub password)
  - Go to: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Generate new token
  - Select scopes: `repo` (full control)
  - Copy token and use it as password

**Or use GitHub Desktop (easier):**
1. Download: https://desktop.github.com
2. Sign in
3. Add repository
4. Click "Publish repository"

---

## Step 10: Verify Upload

**Go back to GitHub and refresh the page:**
```
https://github.com/ICTcmd/fb-to-sheets
```

**You should see all your files!** ✅

---

## Quick Command Summary:

**Copy and paste these commands one by one:**

```powershell
# Navigate to project folder
cd "C:\Users\ACER\Desktop\FB to Sheets"

# Check if Git is installed
git --version

# Initialize git (if not already)
git init

# Add all files
git add .

# Check what will be uploaded
git status

# Commit files
git commit -m "Initial commit: Facebook to Google Sheets automation"

# Set branch to main
git branch -M main

# Add remote repository
git remote add origin https://github.com/ICTcmd/fb-to-sheets.git

# Push to GitHub
git push -u origin main
```

---

## Troubleshooting:

### Issue: "git: command not found"
**Solution:** Install Git from https://git-scm.com/download/win

### Issue: "fatal: not a git repository"
**Solution:** Run `git init` first

### Issue: "remote origin already exists"
**Solution:** Run `git remote set-url origin https://github.com/ICTcmd/fb-to-sheets.git`

### Issue: Authentication failed
**Solution:** 
1. Use Personal Access Token instead of password
2. Or use GitHub Desktop (easier)

### Issue: "credentials.json" is showing in git status
**Solution:** Check `.gitignore` file includes `credentials.json`

---

## After Uploading:

**Once your code is on GitHub:**
1. ✅ Verify all files are there (except credentials.json and .env)
2. ✅ Check GitHub repository page
3. ✅ Next: Deploy to Railway!

---

**Ready to upload? Run the commands above!** 🚀

