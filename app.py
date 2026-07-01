import streamlit as st
import joblib

st.title("Sales Forecasting App")

model = joblib.load("polynomial_model.pkl")
poly = joblib.load("poly_features.pkl")

st.success("Both files loaded successfully!")