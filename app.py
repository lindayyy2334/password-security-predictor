import streamlit as st
import numpy as np

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Password Fortress", page_icon="🔐")
st.title("Password Fortress Security Predictor")
st.write("🔹 Enter your password length to estimate its security score.")

# =========================
# Model Parameters
# =========================
w = 1.5
b = -5.0

# =========================
# User Input
# =========================
length = st.number_input(
    "Enter password length:",
    min_value=4,
    max_value=20,
    value=8
)

# =========================
# Prediction Function
# =========================
def predict_crack_time(length, w=w, b=b):
    log_sec = w * length + b
    sec = np.exp(log_sec)
    return sec

seconds = predict_crack_time(length)

# =========================
# Convert to human-readable
# =========================
if seconds >= 31536000:
    display_time = f"{seconds/31536000:.1f} years"
elif seconds >= 86400:
    display_time = f"{seconds/86400:.1f} days"
elif seconds >= 3600:
    display_time = f"{seconds/3600:.1f} hours"
elif seconds >= 60:
    display_time = f"{seconds/60:.1f} minutes"
else:
    display_time = f"{seconds:.2f} seconds"

# =========================
# Security Score
# =========================
# On donne un score simple basé sur la longueur (max 100)
score = min(length * 8, 100)

# Verdict basé sur le score
if score < 50:
    verdict = "DANGER"
    st.error(f"{verdict} — Score: {score}/100")
elif score < 80:
    verdict = "WEAK"
    st.warning(f"{verdict} — Score: {score}/100")
else:
    verdict = "SECURE"
    st.success(f"{verdict} — Score: {score}/100")

# =========================
# Display Estimated Crack Time
# =========================
st.subheader("Estimated Crack Time")
st.write(display_time)
