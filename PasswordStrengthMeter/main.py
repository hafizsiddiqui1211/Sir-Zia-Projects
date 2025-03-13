import re
import streamlit as st

st.set_page_config(page_title="🔑 Password Stregth Meter",
                   page_icon="📶", layout="centered")
st.title("🔑 Password Stregth Meter by Hafiz Siddiqui")
st.write("Enter your password")


def check_password_strength(password):
    score = 0
    feedback = []
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password! 🎉")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.warning("❌ Weak Password - Improve it using the suggestions above.")

    # Feedback
    if feedback:
        with st.expander("Improve your password"):
            for item in feedback:
                st.write(item)


# Get user input
password = st.text_input("Enter your password:",
                         type="password", placeholder="Enter your password")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("⚠️ Please enter a password.")
