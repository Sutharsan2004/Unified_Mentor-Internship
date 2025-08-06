import streamlit as st
import requests

st.title("Tobacco Use Mortality Predictor")

aff_index = st.slider("Affordability Index (%)", 0.0, 100.0, 50.0)
expenditure = st.slider("Tobacco Expenditure Ratio (%)", 0.0, 50.0, 10.0)
smoker_rate = st.slider("Smoker Rate (%)", 0.0, 100.0, 25.0)
admission_rate = st.number_input("Admission Rate", min_value=0.0, value=3000.0)
tobacco_price = st.number_input("Tobacco Price Index", min_value=0.0, value=110.0)
expenditure_tobacco = st.number_input("Household Expenditure on Tobacco", min_value=0.0, value=1000.0)

data = {
    "Affordability Index Scaled": aff_index / 100,
    "Expenditure Ratio": expenditure,
    "Smoker Rate": smoker_rate,
    "Admission Rate": admission_rate,
    "Tobacco Price Index": tobacco_price,
    "Household Expenditure on Tobacco": expenditure_tobacco
}

if st.button("Predict"):
    response = requests.post("http://localhost:5000/predict", json=data)
    result = response.json()
    mortality_risk = 99.5
    if "mortality_risk" in result:
        st.success(f"Predicted Mortality Risk: {result['mortality_risk']} (probability: {result['probability']})")
    else:
        st.error(f"Error from API: {result.get('error', 'Unknown error')}")
