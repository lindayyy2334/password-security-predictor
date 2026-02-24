import streamlit as st
import numpy as np
import re

# =========================
# Page Config & Branding
# =========================
st.set_page_config(page_title="Password Fortress", page_icon="🔐", layout="centered")

# Landing page header
st.markdown("""
<div style='background-color:#0E1117;padding:30px;border-radius:10px;margin-bottom:20px'>
    <h1 style='color:white;text-align:center;font-size:36px;'>🔐 Password Fortress</h1>
    <p style='color:white;text-align:center;font-size:18px;'>
        Protect your accounts with data-driven password strength predictions.<br>
        Free version shows basic score. Premium unlocks advanced analysis. Enterprise is for teams.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Password Input Section
# =========================
st.subheader("🔑 Check Your Password")
password = st.text_input("Enter your password:", type="password")

def analyze_password(pw):
    length = len(pw)
    score = min(length * 5, 50)
    if re.search(r"[A-Z]", pw): score += 10
    if re.search(r"[a-z]", pw): score += 10
    if re.search(r"\d", pw): score += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw): score += 10
    score = min(score, 100)
    if score < 50:
        verdict = "DANGER"
    elif score < 80:
        verdict = "WEAK"
    else:
        verdict = "SECURE"
    w, b = 1.5, -5
    seconds = np.exp(w*length + b)
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

if password:
    score, verdict, display_time = analyze_password(password)
    st.markdown("### Password Security Analysis")
    if verdict == "DANGER":
        st.error(f"{verdict} — Score: {score}/100")
    elif verdict == "WEAK":
        st.warning(f"{verdict} — Score: {score}/100")
    else:
        st.success(f"{verdict} — Score: {score}/100")
    st.write(f"Estimated Crack Time: {display_time}")

# =========================
# Subscription Plans Section
# =========================
st.markdown("---")
st.header("💼 Choose Your Plan")

col1, col2, col3 = st.columns(3)

# Free Plan
with col1:
    st.markdown("""
    <div style='background-color:#f0f2f6;padding:20px;border-radius:15px;box-shadow:2px 2px 10px rgba(0,0,0,0.1)'>
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
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Free", key="free_plan"):
        st.success("🎉 You are using the Free Plan!")

# Premium Plan
with col2:
    st.markdown("""
    <div style='background-color:#f0f2f6;padding:20px;border-radius:15px;box-shadow:2px 2px 10px rgba(0,0,0,0.1)'>
        <h3>💎 Premium Plan</h3>
        <ul>
            <li>Unlimited password analyses</li>
            <li>Advanced risk scoring</li>
            <li>Detailed crack-time estimation</li>
            <li>Downloadable professional PDF reports</li>
            <li>Personalized security recommendations</li>
        </ul>
        <p><strong>Revenue Model:</strong> Monthly or yearly subscription</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Subscribe Now", key="premium_plan"):
        st.success("💳 Redirecting to subscription page...")

# Enterprise Plan
with col3:
    st.markdown("""
    <div style='background-color:#f0f2f6;padding:20px;border-radius:15px;box-shadow:2px 2px 10px rgba(0,0,0,0.1)'>
        <h3>🏢 Enterprise Plan</h3>
        <ul>
            <li>Bulk password analysis</li>
            <li>Organizational risk overview</li>
            <li>Advanced reporting dashboard</li>
            <li>API access for integration</li>
            <li>Custom branding options</li>
        </ul>
        <p><strong>Commercial Strategy:</strong></p>
        <ul>
            <li>Freemium drives adoption</li>
            <li>Premium monetizes individuals</li>
            <li>Enterprise generates scalable recurring revenue</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Contact Sales", key="enterprise_plan"):
        st.success("📧 Redirecting to Enterprise sales contact page...")
