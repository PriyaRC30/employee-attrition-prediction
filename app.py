# ============================================================
# EMPLOYEE ATTRITION PREDICTION - STREAMLIT APPLICATION
# ============================================================

import streamlit as st
import pandas as pd
import joblib
import os


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

MODEL_PATH = "models/final_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(
        "Final model not found. Please make sure "
        "models/final_model.pkl exists."
    )
    st.stop()

model = joblib.load(MODEL_PATH)


# ============================================================
# TITLE
# ============================================================

st.title("👨‍💼 Employee Attrition Prediction")

st.write(
    """
    This application predicts whether an employee is likely
    to leave the organization based on employee, job,
    salary and satisfaction information.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Employee Information")

age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=65,
    value=30
)

business_travel = st.sidebar.selectbox(
    "Business Travel",
    ["Non-Travel", "Travel_Rarely", "Travel_Frequently"]
)

daily_rate = st.sidebar.number_input(
    "Daily Rate",
    min_value=0,
    max_value=1500,
    value=500
)

department = st.sidebar.selectbox(
    "Department",
    [
        "Sales",
        "Research & Development",
        "Human Resources"
    ]
)

distance_from_home = st.sidebar.number_input(
    "Distance From Home",
    min_value=1,
    max_value=30,
    value=5
)

education = st.sidebar.selectbox(
    "Education Level",
    [1, 2, 3, 4, 5],
    index=2
)

education_field = st.sidebar.selectbox(
    "Education Field",
    [
        "Life Sciences",
        "Medical",
        "Marketing",
        "Technical Degree",
        "Human Resources",
        "Other"
    ]
)

environment_satisfaction = st.sidebar.selectbox(
    "Environment Satisfaction",
    [1, 2, 3, 4],
    index=2
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

hourly_rate = st.sidebar.number_input(
    "Hourly Rate",
    min_value=0,
    max_value=100,
    value=60
)

job_involvement = st.sidebar.selectbox(
    "Job Involvement",
    [1, 2, 3, 4],
    index=2
)

job_level = st.sidebar.selectbox(
    "Job Level",
    [1, 2, 3, 4, 5],
    index=1
)

job_role = st.sidebar.selectbox(
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

job_satisfaction = st.sidebar.selectbox(
    "Job Satisfaction",
    [1, 2, 3, 4],
    index=2
)

marital_status = st.sidebar.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

monthly_income = st.sidebar.number_input(
    "Monthly Income",
    min_value=100,
    max_value=20000,
    value=5000
)

monthly_rate = st.sidebar.number_input(
    "Monthly Rate",
    min_value=0,
    max_value=30000,
    value=14000
)

num_companies_worked = st.sidebar.number_input(
    "Number of Companies Worked",
    min_value=0,
    max_value=10,
    value=2
)

overtime = st.sidebar.selectbox(
    "Overtime",
    ["Yes", "No"]
)

percent_salary_hike = st.sidebar.number_input(
    "Percent Salary Hike",
    min_value=0,
    max_value=30,
    value=15
)

performance_rating = st.sidebar.selectbox(
    "Performance Rating",
    [1, 2, 3, 4],
    index=2
)

relationship_satisfaction = st.sidebar.selectbox(
    "Relationship Satisfaction",
    [1, 2, 3, 4],
    index=2
)

stock_option_level = st.sidebar.selectbox(
    "Stock Option Level",
    [0, 1, 2, 3],
    index=0
)

total_working_years = st.sidebar.number_input(
    "Total Working Years",
    min_value=0,
    max_value=40,
    value=8
)

training_times_last_year = st.sidebar.number_input(
    "Training Times Last Year",
    min_value=0,
    max_value=10,
    value=3
)

work_life_balance = st.sidebar.selectbox(
    "Work-Life Balance",
    [1, 2, 3, 4],
    index=2
)

years_at_company = st.sidebar.number_input(
    "Years At Company",
    min_value=0,
    max_value=40,
    value=5
)

years_in_current_role = st.sidebar.number_input(
    "Years In Current Role",
    min_value=0,
    max_value=20,
    value=3
)

years_since_last_promotion = st.sidebar.number_input(
    "Years Since Last Promotion",
    min_value=0,
    max_value=15,
    value=1
)

years_with_curr_manager = st.sidebar.number_input(
    "Years With Current Manager",
    min_value=0,
    max_value=20,
    value=3
)


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({
    "Age": [age],
    "BusinessTravel": [business_travel],
    "DailyRate": [daily_rate],
    "Department": [department],
    "DistanceFromHome": [distance_from_home],
    "Education": [education],
    "EducationField": [education_field],
    "EnvironmentSatisfaction": [environment_satisfaction],
    "Gender": [gender],
    "HourlyRate": [hourly_rate],
    "JobInvolvement": [job_involvement],
    "JobLevel": [job_level],
    "JobRole": [job_role],
    "JobSatisfaction": [job_satisfaction],
    "MaritalStatus": [marital_status],
    "MonthlyIncome": [monthly_income],
    "MonthlyRate": [monthly_rate],
    "NumCompaniesWorked": [num_companies_worked],
    "OverTime": [overtime],
    "PercentSalaryHike": [percent_salary_hike],
    "PerformanceRating": [performance_rating],
    "RelationshipSatisfaction": [relationship_satisfaction],
    "StockOptionLevel": [stock_option_level],
    "TotalWorkingYears": [total_working_years],
    "TrainingTimesLastYear": [training_times_last_year],
    "WorkLifeBalance": [work_life_balance],
    "YearsAtCompany": [years_at_company],
    "YearsInCurrentRole": [years_in_current_role],
    "YearsSinceLastPromotion": [years_since_last_promotion],
    "YearsWithCurrManager": [years_with_curr_manager]
})


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.subheader("Prediction")

if st.button(
    "🔮 Predict Employee Attrition",
    type="primary",
    use_container_width=True
):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0][1]

    probability_percent = probability * 100


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    if prediction == 1:

        st.error(
            "⚠️ HIGH RISK OF EMPLOYEE ATTRITION"
        )

        st.write(
            f"Estimated probability of attrition: "
            f"**{probability_percent:.2f}%**"
        )

        st.warning(
            "The employee may be at risk of leaving "
            "the organization."
        )

    else:

        st.success(
            "✅ LOW RISK OF EMPLOYEE ATTRITION"
        )

        st.write(
            f"Estimated probability of attrition: "
            f"**{probability_percent:.2f}%**"
        )

        st.info(
            "The employee is predicted to stay "
            "with the organization."
        )


# ============================================================
# SHOW INPUT DATA
# ============================================================

with st.expander("View Employee Information"):

    st.dataframe(
        input_data,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Employee Attrition Prediction | "
    "Machine Learning Classification Project"
)
