import streamlit as st
import numpy as np
import re

# =========================
# Page Config & Branding
# =========================
st.set_page_config(page_title="Password Fortress", page_icon="🔐", layout="centered")

st.markdown("""
<div style='background-color:#0E1117;padding:25px;border-radius:10px'>
    <h1 style='color:white;text-align:center;'>🔐 Password Fortress</h1>
    <p style='color:white;text-align:center;font-size:18px;'>
        Protect your accounts with data-driven password strength predictions.
        Free version shows basic score. Premium unlocks advanced analysis and reports.
        Enterprise plan is perfect for teams and organizations.
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
    
    # Estimated crack time
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
# Subscription Plans / Landing Page
# =========================
st.markdown("---")
st.header("Choose Your Plan")

# Free Plan
st.markdown("### Free Plan")
st.markdown("""
- Limited number of password analyses per day  
- Basic security score  
- General strength classification  

**Purpose:**  
- Attract users  
- Build trust  
- Encourage upgrade through feature limitation
""")
if st.button("Start Free", key="free_plan"):
    st.success("🎉 You are using the Free Plan!")

# Premium Plan
st.markdown("### 💎 Premium Plan")
st.markdown("""
- Unlimited password analyses  
- Advanced risk scoring  
- Detailed crack-time estimation  
- Downloadable professional PDF reports  
- Personalized security recommendations  

**Revenue Model:** Monthly or yearly subscription  
This tier converts engaged users into paying customers by offering practical and professional value.
""")
if st.button("Subscribe Now", key="premium_plan"):
    st.success("💳 Redirecting to subscription page...")

# Enterprise Plan
st.markdown("### 🏢 Enterprise Plan")
st.markdown("""
**Designed for SMEs, training institutions, and IT departments.**  

Includes:  
- Bulk password analysis  
- Organizational risk overview  
- Advanced reporting dashboard  
- API access for integration  
- Custom branding options  

**Commercial Strategy:**  
- Freemium drives adoption  
- Premium monetizes individuals  
- Enterprise generates scalable, recurring revenue  

This model ensures:  
- Continuous cash flow  
- Scalable growth  
- Clear upgrade incentives  
- Long-term SaaS sustainability
""")
if st.button("Contact Sales", key="enterprise_plan"):
    st.success("📧 Redirecting to Enterprise sales contact page...")
