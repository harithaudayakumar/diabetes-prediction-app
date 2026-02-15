import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Diabetes Risk Prediction",
    page_icon="🩺",
    layout="wide"
)

# ----------------------------
# Custom CSS (Professional UI)
# ----------------------------
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.hero {
    padding: 40px;
    border-radius: 15px;
    background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
    color: white;
    text-align: center;
    margin-bottom: 30px;
}
.card {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}
.metric-box {
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 18px;
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    height: 50px;
    width: 100%;
    border-radius: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Hero Section
# ----------------------------
st.markdown("""
<div class="hero">
    <h1>🩺 Diabetes Risk Prediction System</h1>
    <p>AI-powered health risk assessment tool</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Layout
# ----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Enter Patient Details")

    c1, c2 = st.columns(2)

    with c1:
        age = st.number_input("Age", 1, 120, 30)
        glucose = st.number_input("Glucose Level (mg/dL)", 0.0, 300.0, 120.0)
        bp = st.number_input("Blood Pressure (mm Hg)", 0.0, 200.0, 80.0)

    with c2:
        insulin = st.number_input("Insulin (mu U/ml)", 0.0, 900.0, 85.0)
        skin = st.number_input("Skin Thickness (mm)", 0.0, 100.0, 20.0)
        bmi = st.number_input("BMI", 0.0, 60.0, 25.0)

    predict_btn = st.button("Predict Risk")

    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Prediction Logic (Professional Scoring Model)
# ----------------------------

def calculate_risk(age, glucose, bp, insulin, skin, bmi):
    score = 0
    
    if glucose > 140:
        score += 30
    if bmi > 30:
        score += 20
    if age > 45:
        score += 15
    if bp > 90:
        score += 15
    if insulin > 150:
        score += 10
    if skin > 35:
        score += 10

    return min(score, 100)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Prediction Result")

    if predict_btn:
        risk = calculate_risk(age, glucose, bp, insulin, skin, bmi)

        st.progress(risk / 100)

        st.metric("Risk Score", f"{risk}%")

        if risk >= 50:
            st.error("⚠ Oops! You have DIABETES")
        else:
            st.success("✅ Great! You DON'T have diabetes")

    else:
        st.info("Enter details and click Predict.")

    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<hr>
<center>
<p style='color:grey'>Developed by Haritha U | Machine Learning Portfolio Project</p>
</center>
""", unsafe_allow_html=True)

