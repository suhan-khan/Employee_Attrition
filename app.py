import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("employee_attrition_model.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

st.title("Employee Attrition Prediction")
st.write("Predict whether an employee is likely to leave the company.")

# Employee Information
st.header("Employee Information")

Age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30
)
OverTime = st.selectbox(
    "OverTime",
    ["Yes", "No"]
)
JobRole = st.selectbox(
    "Job Role",
    [
        "Sales Executive",
        "Research Scientist",
        "Laboratory Technician",
        "Manufacturing Director",
        "Healthcare Representative",
        "Manager",
        "Sales Representative",
        "Research Director",
        "Human Resources"
    ]
)

BusinessTravel = st.selectbox(
    "Business Travel",
    [
        "Travel_Rarely",
        "Travel_Frequently",
        "Non-Travel"
    ]
)

TotalWorkingYears = st.number_input(
    "Total Working Years",
    min_value=0,
    max_value=40,
    value=10
)

JobLevel = st.number_input(
    "Job Level",
    min_value=1,
    max_value=5,
    value=2
)

MonthlyIncome = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=200000,
    value=30000
)

DistanceFromHome = st.number_input(
    "Distance From Home",
    min_value=1,
    max_value=29,
    value=5
)

JobSatisfaction = st.slider(
    "Job Satisfaction",
    min_value=1,
    max_value=4,
    value=3
)

EnvironmentSatisfaction = st.slider(
    "Environment Satisfaction",
    min_value=1,
    max_value=4,
    value=3
)

YearsAtCompany = st.number_input(
    "Years At Company",
    min_value=0,
    max_value=40,
    value=5
)

StockOptionLevel = st.number_input(
    "Stock Option Level",
    min_value=0,
    max_value=3,
    value=1
)

# Prediction
if st.button("Predict Attrition"):

    input_data = pd.DataFrame({
        "Age": [Age],
        "OverTime": [OverTime],
        "JobRole": [JobRole],
        "BusinessTravel": [BusinessTravel],
        "TotalWorkingYears": [TotalWorkingYears],
        "JobLevel": [JobLevel],
        "MonthlyIncome": [MonthlyIncome],
        "DistanceFromHome": [DistanceFromHome],
        "JobSatisfaction": [JobSatisfaction],
        "EnvironmentSatisfaction": [EnvironmentSatisfaction],
        "YearsAtCompany": [YearsAtCompany],
        "StockOptionLevel": [StockOptionLevel]
    })

    input_data = input_data[feature_columns]

    # Prediction
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Employee is likely to leave.")
    else:
        st.success("✅ Employee is likely to stay.") 