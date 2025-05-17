import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💪 BMI Calculator</h1>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        height = st.slider("📏 Height (cm)", 100, 250, 175)

    with col2:
        weight = st.slider("⚖️ Weight (kg)", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

# BMI Result Box
st.markdown("---")
st.subheader("📊 Your BMI Result:")
bmi_color = "green"
category = ""

if bmi < 18.5:
    category = "Underweight"
    bmi_color = "blue"
elif 18.5 <= bmi < 25:
    category = "Normal Weight"
    bmi_color = "green"
elif 25 <= bmi < 30:
    category = "Overweight"
    bmi_color = "orange"
else:
    category = "Obesity"
    bmi_color = "red"

st.markdown(f"<div style='padding: 10px; background-color: {bmi_color}; color: white; text-align: center; border-radius: 10px;'>"
            f"<h2>BMI: {bmi:.2f}</h2><h3>{category}</h3></div>", unsafe_allow_html=True)

# BMI Categories
st.markdown("---")
st.markdown("### 📚 BMI Categories")
st.write("- **Underweight:** BMI less than 18.5")
st.write("- **Normal weight:** BMI between 18.5 and 24.9")
st.write("- **Overweight:** BMI between 25 and 29.9")
st.write("- **Obesity:** BMI 30 or greater")
