import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Page Config & Branding
# =========================
st.set_page_config(
    page_title="Password Fortress",
    page_icon="🔐",
    layout="centered"
)

st.markdown(
    """
    <div style='background-color:#0E1117;padding:15px;border-radius:5px'>
        <h1 style='color:white;text-align:center;'>Password Fortress Security Predictor</h1>
    </div>
    """, unsafe_allow_html=True
)

st.write("🔹 Estimate how long it would take to crack a password based on its length.")
st.write("Use the slider or input box below to enter your password length.")

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
# Security Verdict
# =========================
if length < 8:
    verdict = "DANGER"
    st.error(verdict)
elif length < 12:
    verdict = "WEAK"
    st.warning(verdict)
else:
    verdict = "SECURE"
    st.success(verdict)

st.subheader("Estimated Crack Time")
st.write(display_time)

# =========================
# Graph: Password Length vs Time
# =========================
lengths = np.arange(4, 21)
times = predict_crack_time(lengths)

fig, ax = plt.subplots()
ax.plot(lengths, times, marker='o', color='#1f77b4')
ax.set_yscale('log')  # logarithmic scale to show exponential growth
ax.set_xlabel("Password Length")
ax.set_ylabel("Time to Crack (seconds, log scale)")
ax.set_title("Password Length vs Crack Time")
st.pyplot(fig)

# =========================
# Premium Features (Sidebar)
# =========================
st.sidebar.header("Premium Features")
premium = st.sidebar.checkbox("Activate Premium Mode")

if premium:
    st.sidebar.write("💎 Advanced Security Score & Recommendations")
    
    # Example: Score based on password length
    score = min(length * 8, 100)  # max 100
    st.sidebar.metric("Password Security Score", f"{score}/100")
    
    # Recommendations
    if score < 50:
        st.sidebar.warning("Consider increasing password length or complexity!")
    elif score < 80:
        st.sidebar.info("Medium strength password. Could be improved.")
    else:
        st.sidebar.success("Strong password! Well done.")

# =========================
# Footer / Business Pitch
# =========================
st.markdown(
    """
    ---
    🔐 **Password Fortress** helps fintechs and security-conscious organizations
    evaluate password strength with a scientific, data-driven approach.
    
    Premium subscription unlocks advanced scoring, recommendations, and PDF reports.
    Enterprise clients can integrate via API for bulk analysis and dashboards.
    """
)
