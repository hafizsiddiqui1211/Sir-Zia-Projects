# 🛡️ Secure Data Encryption System

A lightweight, secure, and user-friendly data encryption web app built with [Streamlit](https://streamlit.io/). This system allows users to register, log in, store sensitive data in encrypted form, and securely retrieve and decrypt it — **all without any external database**.

---

## 🚀 Features

- 🔐 **User Registration & Login System**
- 🔒 **AES-256 Level Encryption** using `cryptography.Fernet`
- 🧠 **Password & Passkey Hashing** with `PBKDF2 HMAC SHA-256`
- 🗃️ **Local JSON-based Storage** (no cloud or database required)
- ⏳ **Lockout Mechanism** after 3 failed login attempts (60 seconds)
- 📦 **Store and Retrieve Multiple Encrypted Entries**

---

## 🧩 Technologies Used

- `Streamlit` — For building the web interface
- `Cryptography` — For encrypting and decrypting data
- `Hashlib` — For password hashing
- `PBKDF2 HMAC` — For generating secure symmetric encryption keys
- `JSON` — For lightweight and portable local data storage

---

## 🖥️ How to Run

1. **Install Python Packages**:

```bash
pip install streamlit cryptography
```

2. **Run the App**:

```bash
streamlit run your_filename.py
```

3. The app will open in your browser at `http://localhost:8501`.

---

## 🔐 Encryption Logic

- **Passwords** are hashed and stored using `PBKDF2_HMAC`.
- **Passkeys** are used to derive a symmetric encryption key.
- Each piece of data is encrypted using this derived key via `Fernet`.

---

## 📂 File Structure

```
secure_encryption_app/
│
├── secure_data.json         # Local JSON storage for user credentials & data
├── your_filename.py         # Main Streamlit app
└── README.md                # You're here!
```

---

## 🛡️ Security Notes

- Do not use this app for highly sensitive or production-grade data.
- Passwords and data are stored **locally** in `secure_data.json`.
- Use strong passphrases for encryption keys.

---

## 🙋‍♂️ Author

Made with ❤️ by **Hafiz Siddiqui**

---

## 📜 License

This project is open-source and free to use.
```
