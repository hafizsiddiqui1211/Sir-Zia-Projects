import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# Page setup
st.set_page_config(
    page_icon="🛡️", page_title="Secure Data Encryption System", layout="centered")

# Constants
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60  # in seconds

# Session state initialization
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Load and Save Data


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Key Generation


def generate_key(passkey):
    key = pbkdf2_hmac("sha256", passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)


def hash_password(password):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), SALT, 100000).hex()

# Encryption and Decryption


def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()


def decrypt(encrypted_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None


# Load stored data
stored_data = load_data()

# UI Layout
st.title("🛡️ Secure Data Encryption System by Hafiz Siddiqui")
menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("Navigation", menu)

# === HOME PAGE ===
if choice == "Home":
    st.subheader("Welcome to your 🛡️ Data Encryption System")
    st.markdown("""
This system allows you to:
- Register with a username and password
- Store sensitive data using encryption
- Retrieve and decrypt data securely
- Get locked out temporarily after multiple failed login attempts
**Note:** Everything is stored locally in memory using JSON, no external databases used.
    """)

# === REGISTER ===
elif choice == "Register":
    st.subheader("🔐 Register New User")
    user_name = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")

    if st.button("Register"):
        if user_name and password:
            if user_name in stored_data:
                st.warning("⚠️ User already exists!")
            else:
                stored_data[user_name] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User Registered Successfully!")
        else:
            st.error("Please fill both fields.")

# === LOGIN ===
elif choice == "Login":
    st.subheader("🔑 User Login")

    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(
            f"🚫 Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    user_name = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if user_name in stored_data and stored_data[user_name]["password"] == hash_password(password):
            st.session_state.authenticated_user = user_name
            st.session_state.failed_attempts = 0
            st.success(f"🎉 Welcome back, {user_name}!")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid credentials! {remaining} attempt(s) left.")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error(
                    "🔐 Account locked for 60 seconds due to too many failed attempts.")
                st.stop()

# === STORE DATA ===
elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("🚨 Please login first!")
    else:
        st.subheader("📦 Store Encrypted Data")
        data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Encryption Key (passphrase)", type="password")

        if st.button("Encrypt and Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(
                    encrypted)
                save_data(stored_data)
                st.success("✅ Data encrypted and saved successfully!")
            else:
                st.error("All fields are required.")

# === RETRIEVE DATA ===
elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("🔐 Please login first!")
    else:
        st.subheader("🔎 Retrieve & Decrypt Data")
        user_data = stored_data.get(
            st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("📭 No stored data found.")
        else:
            st.write("🧾 Encrypted Data Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language="text")

            encrypted_input = st.text_area("Enter Encrypted Text to Decrypt")
            passkey = st.text_input("Enter Passkey", type="password")

            if st.button("Decrypt"):
                result = decrypt(encrypted_input, passkey)
                if result:
                    st.success(f"✅ Decrypted Text:\n{result}")
                else:
                    st.error("❌ Incorrect passkey or corrupted data.")
