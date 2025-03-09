import streamlit as st
import urllib.request
import json

# Set the title of the app
st.title("Predicting customer subscription. User Inteface")

#####################################################################

age = st.text_input("Enter your age:", value="30")

#####################################################################

job = st.selectbox("Job:", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", 
                            "unemployed", "unknown"])
job_to_number = {'admin.': 0, 'blue-collar': 1, 'entrepreneur': 2, 'housemaid': 3, 'management': 4, 'retired': 5, 'self-employed': 6, 'services': 7, 
                 'student': 8, 'technician': 9, 'unemployed': 10, 'unknown': 11}
job = job_to_number.get(job, "Invalid status")

#####################################################################

marital = st.selectbox("Select your marital status:", ['divorced', 'married', 'single', 'unknown'])
marital_to_number = {'divorced': 0, 'married': 1, 'single': 2, 'unknown': 3}
marital = marital_to_number.get(marital, "Invalid status")


#####################################################################

education = st.selectbox("Select your education:", ['basic.4y', 'basic.6y', 'basic.9y', 'high.school','illiterate', 'professional.course', 'university.degree', 'unknown'])
education_to_number = {'basic.4y': 0, 'basic.6y': 1, 'basic.9y': 2, 'high.school': 3, 'illiterate': 4, 'professional.course': 5, 'university.degree': 6, 'unknown': 7}
education = education_to_number.get(education, "Invalid status")


#####################################################################

default = st.selectbox("Select your default:", ['no', 'unknown', 'yes'])
default_to_number = {'no': 0, 'unknown': 1, 'yes': 2}
default = default_to_number.get(default, "Invalid status")


#####################################################################

housing = st.selectbox("Select your housing:", ['no', 'unknown', 'yes'])
housing_to_number = {'no': 0, 'unknown': 1, 'yes': 2}
housing = housing_to_number.get(housing, "Invalid status")

####################################################################

loan = st.selectbox("Select your loan:", ['no', 'unknown', 'yes'])
loan_to_number = {'no': 0, 'unknown': 1, 'yes': 2}
loan = loan_to_number.get(loan, "Invalid status")

####################################################################

contact = st.selectbox("Select your contact:", ['cellular', 'telephone'])
contact_to_number = {'cellular': 0, 'telephone': 1}
contact = contact_to_number.get(contact, "Invalid status")


#####################################################################

month = st.selectbox("Select a month:", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])

#####################################################################

dayweek = st.selectbox("Select your dayweek:", ['mon', 'tue', 'wed', 'thu', 'fri'])
dayweek_to_number  = {'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5}
dayweek = dayweek_to_number.get(dayweek, "Invalid status")

#####################################################################

duration = st.text_input("Enter the duration of the call in minutes:", value="3")


#####################################################################

campaign = st.text_input("Enter the campaign number:", value="1")

#####################################################################

previous = st.selectbox("Select previous:", ["0", "1"])

#####################################################################

poutcome = st.selectbox("Select your poutcome:", ['failure', 'nonexistent', 'success'])
poutcome_to_number = {'failure': 0, 'nonexistent': 1, 'success': 2}
poutcome = loan_to_number.get(poutcome, "Invalid status")

#####################################################################


url = f"http://127.0.0.1:5000/prediction?age={age}&job={job}&marital={marital}&education={education}&default={default}&housing={housing}&loan={loan}&contact={contact}&month={month}&dayweek={dayweek}&duration={duration}&campaign={campaign}&previous={previous}&poutcome=1"
with urllib.request.urlopen(url) as url:
    Total_data = json.loads(url.read().decode())

    

# Show the message when the button is clicked
if st.button("Show Prediction"):

    st.write(f"age = {age}, job = {job}, marital = {marital}, education = {education}, default = {default}, housing = {housing}, loan = {loan},  \
               contact = {contact}, month = {month}, dayweek = {dayweek}, duration = {duration}, campaign = {campaign}, previous = {previous}, poutcome = {poutcome},")

    st.write('Prediction = ', Total_data)
