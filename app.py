import streamlit as st
import numpy as np

# ==============================
# Model Parameters (Replace with your trained values if needed)
# ==============================
w = 1.5
b = -5.0

# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="Password Fortress Security Predictor",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Fortress Security Predictor")
st.markdown("Estimate how long a password would take to crack using a predictive ML model.")

st.divider()

# ==============================
# User Input
# ==============================
length = st.number_input(
    "Enter password length:",
    min_value=4,
    max_value=32,
    value=8,
    step=1
)

# ==============================
# Prediction
# ==============================
log_seconds = w * length + b
seconds = np.exp(log_seconds)

# ==============================
# Convert to Human-Readable Time
# ==============================
if seconds >= 31536000:
    display_time = f"{seconds/31536000:.2f} years"
elif seconds >= 86400:
    display_time = f"{seconds/86400:.2f} days"
elif seconds >= 3600:
    display_time = f"{seconds/3600:.2f} hours"
elif seconds >= 60:
    display_time = f"{seconds/60:.2f} minutes"
else:
    display_time = f"{seconds:.2f} seconds"

# ==============================
# Security Verdict
# ==============================
if length < 8:
    verdict = "🔴 DANGER"
    color = "red"
elif length < 12:
    verdict = "🟠 WEAK"
    color = "orange"
else:
    verdict = "🟢 SECURE"
    color = "green"

# ==============================
# Display Results
# ==============================
st.subheader("Prediction Result")
st.write(f"**Estimated Crack Time:** {display_time}")
st.markdown(f"**Security Verdict:** :{color}[{verdict}]")

st.divider()

# ==============================
# Business Insight Section
# ==============================
st.subheader("Business Insight")
st.write(
    """
    This prediction helps financial institutions evaluate password policy strength.
    By estimating crack time, organizations can:
    - Improve security standards
    - Reduce cyber risk exposure
    - Increase customer trust
    """
)

st.caption("Model based on log-transformed linear regression.")
