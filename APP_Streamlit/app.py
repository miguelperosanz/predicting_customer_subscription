import streamlit as st
import urllib.request
import json

# Set the title of the app
st.title("Predicting Customer Subscription - User Interface")

def get_numeric_input(label, options, mapping):
    selected = st.selectbox(label, options)
    return mapping.get(selected, "Invalid status")

# Define mappings for categorical variables
mappings = {
    "Job": (["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", 
             "services", "student", "technician", "unemployed", "unknown"],
            {'admin.': 0, 'blue-collar': 1, 'entrepreneur': 2, 'housemaid': 3, 'management': 4, 'retired': 5, 
             'self-employed': 6, 'services': 7, 'student': 8, 'technician': 9, 'unemployed': 10, 'unknown': 11}),
    
    "Marital Status": (['divorced', 'married', 'single', 'unknown'],
                       {'divorced': 0, 'married': 1, 'single': 2, 'unknown': 3}),
    
    "Education": (['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 
                   'university.degree', 'unknown'],
                  {'basic.4y': 0, 'basic.6y': 1, 'basic.9y': 2, 'high.school': 3, 'illiterate': 4, 
                   'professional.course': 5, 'university.degree': 6, 'unknown': 7}),
    
    "Default": (['no', 'unknown', 'yes'], {'no': 0, 'unknown': 1, 'yes': 2}),
    "Housing": (['no', 'unknown', 'yes'], {'no': 0, 'unknown': 1, 'yes': 2}),
    "Loan": (['no', 'unknown', 'yes'], {'no': 0, 'unknown': 1, 'yes': 2}),
    "Contact": (['cellular', 'telephone'], {'cellular': 0, 'telephone': 1}),
    "Day of the Week": (['mon', 'tue', 'wed', 'thu', 'fri'], {'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5}),
    "Poutcome": (['failure', 'nonexistent', 'success'], {'failure': 0, 'nonexistent': 1, 'success': 2}),
}

col1, col2 = st.columns(2)

# Collect user inputs:
with col1:
    age = st.text_input("Enter your age:", value="30")
    job = get_numeric_input("Job:", *mappings["Job"])
    marital = get_numeric_input("Select your marital status:", *mappings["Marital Status"])
    education = get_numeric_input("Select your education:", *mappings["Education"])
    default = get_numeric_input("Select your default:", *mappings["Default"])
    housing = get_numeric_input("Select your housing:", *mappings["Housing"])
    loan = get_numeric_input("Select your loan:", *mappings["Loan"])
    

with col2:
    contact = get_numeric_input("Select your contact:", *mappings["Contact"])
    dayweek = get_numeric_input("Select your day of the week:", *mappings["Day of the Week"])
    poutcome = get_numeric_input("Select your poutcome:", *mappings["Poutcome"])
    month = st.selectbox("Select a month:", [str(i) for i in range(1, 13)])
    duration = st.text_input("Enter the duration of the call in minutes:", value="3")
    campaign = st.text_input("Enter the campaign number:", value="1")
    previous = st.selectbox("Select previous:", ["0", "1"])


# API Request
url = f"http://127.0.0.1:5000/prediction?age={age}&job={job}&marital={marital}&education={education}&default={default}&housing={housing}&loan={loan}&contact={contact}&month={month}&dayweek={dayweek}&duration={duration}&campaign={campaign}&previous={previous}&poutcome={poutcome}"
with urllib.request.urlopen(url) as response:
    Total_data = json.loads(response.read().decode())


st.write("")
# Display Results
if st.button("Show Prediction"):
    st.write("Prediction:", Total_data)
