import streamlit as st
import numpy as np
import re

# =========================
# Page Config & Branding
# =========================
st.set_page_config(page_title="Password Fortress", page_icon="🔐", layout="centered")

# Landing Page / Commercial Header
st.markdown("""
<div style='background-color:#0E1117;padding:25px;border-radius:10px'>
    <h1 style='color:white;text-align:center;'>🔐 Password Fortress</h1>
    <p style='color:white;text-align:center;font-size:18px;'>
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
    
    # Score based on length and complexity
    score = min(length * 5, 50)  # max 50 from length
    
    if re.search(r"[A-Z]", pw):
        score += 10
    if re.search(r"[a-z]", pw):
        score += 10
    if re.search(r"\d", pw):
        score += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        score += 10
    
    score = min(score, 100)
    
    if score < 50:
        verdict = "DANGER"
    elif score < 80:
        verdict = "WEAK"
    else:
        verdict = "SECURE"
    
    # Estimated crack time (approx. based on length)
    w = 1.5
    b = -5
    log_seconds = w * length + b
    seconds = np.exp(log_seconds)
    
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
# Subscription Plans / Landing Page Section
# =========================
st.markdown("---")
st.header("Choose Your Plan")

st.markdown("""
<div style='display:flex; gap:20px;'>
    <div style='background-color:#FF6B81; padding:15px; border-radius:10px; flex:1;'>
        <h3>Free Plan</h3>
        <ul>
            <li>Limited number of password analyses per day</li>
            <li>Basic security score</li>
            <li>General strength classification</li>
        </ul>
        <p><strong>Purpose:</strong></p>
        <ul>
            <li>Attract users</li>
            <li>Build trust</li>
            <li>Encourage upgrade through feature limitation</li>
        </ul>
        <button style='padding:10px 15px; background-color:#1f77b4;color:white;border:none;border-radius:5px;'>Start Free</button>
    </div>
    <div style='background-color:#FF6B81; padding:15px; border-radius:10px; flex:1;'>
        <h3>💎 Premium Plan</h3>
        <ul>
            <li>Unlimited password analyses</li>
            <li>Advanced risk scoring</li>
            <li>Detailed crack-time estimation</li>
            <li>Downloadable professional PDF reports</li>
            <li>Personalized security recommendations</li>
        </ul>
        <p><strong>Revenue Model:</strong> Monthly or yearly subscription</p>
        <p>This tier converts engaged users into paying customers by offering practical and professional value.</p>
        <button style='padding:10px 15px; background-color:#1f77b4;color:white;border:none;border-radius:5px;'>Subscribe Now</button>
    </div>
</div>
""", unsafe_allow_html=True)
