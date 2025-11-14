# 🚀 START HERE - Setup Checklist

## ✅ Complete Setup Checklist

Follow the [**SETUP_GUIDE.md**](SETUP_GUIDE.md) for detailed instructions, or check off items below:

### 1. Install Python & Dependencies
- [ ] Python 3.7+ installed
- [ ] Run: `pip install -r requirements.txt`

### 2. Google Sheets Setup
- [ ] Google Cloud Project created
- [ ] Google Sheets API enabled
- [ ] Google Drive API enabled
- [ ] Service Account created
- [ ] JSON key downloaded → Renamed to `credentials.json` → Placed in project folder
- [ ] Google Sheet created
- [ ] Service account email shared with sheet (Editor permission)
- [ ] Sheet ID copied from URL

### 3. Facebook Setup
- [ ] Facebook App created
- [ ] Messenger product added
- [ ] Page Access Token generated → Saved securely
- [ ] ngrok installed (for local testing)
- [ ] Webhook configured in Facebook:
  - [ ] Callback URL set (ngrok URL)
  - [ ] Verify Token set
  - [ ] "messages" subscribed
  - [ ] Page subscribed

### 4. Environment Configuration
- [ ] `.env` file created (copy from `config_example.env`)
- [ ] `FB_VERIFY_TOKEN` set (same as Facebook webhook)
- [ ] `FB_PAGE_ACCESS_TOKEN` set (from Facebook App)
- [ ] `GOOGLE_SHEET_ID` set (from Google Sheet URL)

### 5. Testing
- [ ] Run: `python test_setup.py` → All tests pass
- [ ] Run: `python app.py` → Server starts
- [ ] Run: `ngrok http 5000` (in separate terminal) → ngrok running
- [ ] Facebook webhook URL updated with ngrok URL
- [ ] Test message sent to Facebook Page
- [ ] Message appears in Google Sheet ✅

---

## 📚 Documentation

- **New to this?** → Read [**SETUP_GUIDE.md**](SETUP_GUIDE.md) (Complete step-by-step guide)
- **Quick setup?** → Read [**QUICKSTART.md**](QUICKSTART.md) (For experienced users)
- **Full documentation** → Read [**README.md**](README.md)

---

## 🚨 Common Issues

| Issue | Solution |
|-------|----------|
| Webhook verification failed | Check `FB_VERIFY_TOKEN` matches in `.env` and Facebook |
| Messages not appearing | Check `GOOGLE_SHEET_ID` and service account access |
| Server won't start | Verify `credentials.json` is in project folder |
| ngrok URL changed | Update Facebook webhook URL with new ngrok URL |

---

## 🎯 Quick Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Test setup
python test_setup.py

# Start server
python app.py

# Start ngrok (in separate terminal)
ngrok http 5000
```

---

## 📞 Need Help?

1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md) troubleshooting section
2. Run `python test_setup.py` to verify configuration
3. Check server logs for error messages
4. Verify all values in `.env` file

---

**Ready to start?** → Open [**SETUP_GUIDE.md**](SETUP_GUIDE.md) and follow step-by-step! 🎉

