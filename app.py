import streamlit as st
import joblib
import numpy as np

# Load model and transformer
model = joblib.load("polynomial_model.pkl")
poly = joblib.load("poly_features.pkl")

st.title("Sales Forecasting App")
st.write("Predict Sales based on Temperature")

# User input
temperature = st.number_input(
    "Enter Temperature",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

# Prediction
if st.button("Predict Sales"):
    try:
        data = np.array([[temperature]])
        st.write("Input:", data)

        data_poly = poly.transform(data)
        st.write("Polynomial Features Created Successfully!")

        prediction = model.predict(data_poly)
        st.write("Prediction:", prediction)

        st.success(f"Predicted Sales: {prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
