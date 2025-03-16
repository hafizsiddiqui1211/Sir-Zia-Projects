# 🔑 Password Strength Meter

A simple web app to check password strength using **Streamlit**. This app provides feedback on password security based on length, uppercase/lowercase letters, digits, and special characters.

## 🚀 Features
- Checks password strength based on multiple criteria.
- Provides feedback on improving weak passwords.
- Uses **Streamlit** for an interactive user experience.
- Easy to run and lightweight.

---

## 📦 Installation & Setup

### 1️⃣ Install **uv** (if not installed):
```sh
curl -fsSL https://astral.sh/uv/install.sh | sh
```

### 2️⃣ Create a virtual environment and activate it:
```sh
uv venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate     # For Windows
```

### 3️⃣ Install dependencies:
```sh
uv add streamlit
```

---

## ▶️ Run the App
Start the Streamlit app by running:
```sh
streamlit run app.py
```

---

## 📝 Usage
- Enter a password in the input field.
- Click on **"Check Strength"**.
- Get instant feedback on password security.

---

## 📌 Project Structure
```
📂 Password-Strength-Meter
│── app.py       # Main application file
│── README.md    # Project documentation
│── .venv/       # Virtual environment (created by uv)
└── requirements.txt # Dependencies list (auto-generated)
```

---

## 🔧 How It Works
The password strength is evaluated based on:
1. **Length:** Minimum 8 characters.
2. **Uppercase & Lowercase:** Must include both.
3. **Digits:** At least one number required.
4. **Special Characters:** Must contain at least one (`!@#$%^&*`).

The app provides feedback accordingly:
- ✅ **Strong Password** (Meets all requirements)
- ⚠️ **Moderate Password** (Missing one criterion)
- ❌ **Weak Password** (Needs improvement)

---

## 🤝 Contributing
Feel free to contribute by submitting issues or pull requests.

---

## 📜 License
This project is licensed under the **MIT License**.

