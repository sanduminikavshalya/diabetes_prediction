import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("🩺 Diabetes Prediction System")

labels = [
    "Pregnancies", "Glucose", "BloodPressure",
    "SkinThickness", "Insulin", "BMI",
    "DiabetesPedigreeFunction", "Age"
]

inputs = []

for label in labels:
    inputs.append(st.number_input(label, min_value=0.0))

if st.button("Predict"):
    result = model.predict([inputs])
    if result[0] == 1:
        st.error("⚠ Diabetes Detected")
    else:
        st.success("✅ No Diabetes")
