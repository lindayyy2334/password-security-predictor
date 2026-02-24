import streamlit as st
import numpy as np
import re

# =========================
# Page Config & Branding
# =========================
st.set_page_config(page_title="Password Fortress", page_icon="🔐", layout="centered")

# Landing page / commercial header
st.markdown("""
<div style='background-color:#0E1117;padding:20px;border-radius:5px'>
    <h1 style='color:white;text-align:center;'>🔐 Password Fortress</h1>
    <p style='color:white;text-align:center;'>
        Protect your accounts with data-driven password strength predictions.
        Free version shows basic score. Premium unlocks advanced analysis and reports.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("Enter a password below to see its security score and estimated crack time.")

# =========================
# User Input
# =========================
password = st.text_input("Enter your password:", type="password")

# =========================
# Password Analysis Function
# =========================
def analyze_password(pw):
    length = len(pw)
    
    # Score starts with length weight
    score = min(length * 5, 50)  # max 50 from length
    
    # Complexity: add points for numbers, uppercase, lowercase, special chars
    if re.search(r"[A-Z]", pw):
        score += 10
    if re.search(r"[a-z]", pw):
        score += 10
    if re.search(r"\d", pw):
        score += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        score += 10
    
    # Cap score at 100
    score = min(score, 100)
    
    # Verdict
    if score < 50:
        verdict = "DANGER"
    elif score < 80:
        verdict = "WEAK"
    else:
        verdict = "SECURE"
    
    # Estimated crack time (approx based on length only)
    w = 1.5
    b = -5
    log_seconds = w * length + b
    seconds = np.exp(log_seconds)
    
    # Human-readable
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
    
    return score, verdict, display_time

# =========================
# Show Result
# =========================
if password:
    score, verdict, display_time = analyze_password(password)
    
    st.subheader("Password Security Analysis")
    
    if verdict == "DANGER":
        st.error(f"{verdict} — Score: {score}/100")
    elif verdict == "WEAK":
        st.warning(f"{verdict} — Score: {score}/100")
    else:
        st.success(f"{verdict} — Score: {score}/100")
    
    st.write(f"Estimated Crack Time: {display_time}")

# =========================
# Sidebar Commercial / Premium
# =========================
st.sidebar.header("Unlock Premium Features")
st.sidebar.write("""
💎 **Premium Features**  
- Detailed pattern analysis  
- PDF reports for password audits  
- Advanced scoring with dictionary & leaked passwords  
- Bulk password check for teams
""")
st.sidebar.button("Subscribe Now")
