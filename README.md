# ✉️ Email Signature Generator

A signature **App** designed by AAW department in IAMO to generate standardized email signatures for the department staff. The app collects your details (prefix, name, profession, phone extension, and email) and produces a ready-to-use **rendered email signature** with a preview and copy button.

---

## 🚀 Live Demo  
[👉 **Open the Signature App**](https://emailsignature-ixbjmazbscbrwgjahfmmgk.streamlit.app/)  

---

## 📸 Features  
- ✅ Choose or enter a **custom prefix** (`Dr.`, `Professor`, or custom).  
- ✅ Separate fields for **first name** and **family name**.  
- ✅ Collects the **last 3 digits** of your phone number (base fixed: `+49 345 2928-XXX`).  
- ✅ Uses only the **local part** of your IAMO email (`@iamo.de` is fixed).  
- ✅ Automatically formats IAMO links:  
  - With profile → shows `www.iamo.de/familyname`.  
  - Without profile → shows `www.iamo.de` (links to IAMO home).  
- ✅ Preview your signature live and copy the HTML with one click.  

---

## 🛠 Installation (Local Development)
1. **Clone the repo**:  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   streamlit run app.py
   ```
4. **Open in your browser**:
   ```bash
    Visit   
            Local URL: http://localhost:8503
            Network URL: http://10.0.11.5:8503
            External URL: http://20.61.126.214:8503
    ```
---

## 📂 Project Structure

```markdown
📁 email_signature
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
└── README.md # This file
```

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Please open an issue to discuss changes before submitting.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
