import streamlit as st
import pickle
import numpy as np

# Load Model
with open("models.pkl", 'rb') as obj1:
    dict1 = pickle.load(obj1)

# Custom CSS for Background and Formatting
st.markdown(
    """
    <style>
    /* Background Image */
    .stApp {
        background: url("https://i.postimg.cc/76pMnx7p/girl-1822702-1280.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Title Styling */
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        padding: 15px;
        background: linear-gradient(to right, #ff4b1f, #1fddff);
        border-radius: 10px;
    }

    /* Subheader Styling */
    .subheader {
        font-size: 24px;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        padding: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        border-radius: 10px;
        margin-bottom: 20px;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #ff4b1f;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #1fddff;
        color: black;
    }

    /* Prediction Box */
    .prediction-box {
        font-size: 24px;
        text-align: center;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        background-color: #000000;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="title">Student Depression Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Enter Your Details Below:</div>', unsafe_allow_html=True)

# Input Form Layout
col1, col2 = st.columns(2)

with col1:
    academic_pressure = st.number_input('📖 Academic Pressure (1-5 scale)', min_value=1, max_value=5)
    cgpa = st.number_input('🎓 CGPA')
    study_satisfaction = st.number_input('📚 Study Satisfaction (1-5 scale)', min_value=1, max_value=5)
    job_satisfaction = st.number_input('💼 Job Satisfaction (0-5 scale, 0 if not applicable)', min_value=0, max_value=5)
    sleep_duration = st.number_input('😴 Sleep Duration (1 = <5 hrs, 2 = 5-6 hrs, 3 = 7-8 hrs, 4 = >8 hrs)', min_value=1, max_value=4)

with col2:
    dietary_habits = st.number_input('🥗 Dietary Habits (1 = Unhealthy, 2 = Moderate, 3 = Healthy)', min_value=1, max_value=3)
    suicidal_thoughts = st.number_input('💔 Suicidal Thoughts? (1 = Yes, 0 = No)', min_value=0, max_value=1)
    work_study_hours = st.number_input('⏳ Work/Study Hours per day')
    financial_stress = st.number_input('💰 Financial Stress Level (1-5 scale)', min_value=1, max_value=5)
    family_history = st.number_input('🧬 Family History of Mental Illness? (1 = Yes, 0 = No)', min_value=0, max_value=1)

# Prepare Input Data
x1 = np.array([[academic_pressure, cgpa, study_satisfaction, job_satisfaction, sleep_duration, 
                dietary_habits, suicidal_thoughts, work_study_hours, financial_stress, family_history]])
new = np.hstack([x1])

# Predict Button
if st.button('🔍 Predict'):
    prediction = dict1["models"].predict(x1)
    
    # Display Prediction
    st.markdown(f'<div class="prediction-box">🧠 Predicted Depression Level: <b>{round(prediction[0])}</b></div>', unsafe_allow_html=True)

