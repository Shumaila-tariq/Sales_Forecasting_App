import streamlit as st
import joblib

st.title("Sales Forecasting App")

st.write("Loading model...")

model = joblib.load("polynomial_model.pkl")

st.success("Model loaded successfully!")