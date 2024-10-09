import streamlit as st
import re


#a basic form by clubs


#title
st.title("Induction Form")

#name
name = st.text_input("Enter your full name:")
if name:
    st.write(f"Your name is {name}")


#roll
def valid_roll(roll):
    if len(roll)==7:
        return True
    else:
        return False
    
roll = st.text_input("Enter your roll no")
if roll:
    if  valid_roll(roll):
        st.success("Your roll is valide")
    else:
        st.error("Enter correct roll")
#branch
branchs=["CSE","ECE","EE","ME","CE","ARCHI","MnC"]

branch = st.selectbox("Choose your branch",branchs)
if branch:
    st.write(f"Your branch is {branch}")

#year of study
years=["1st","2st","3rd","4th"]
year = st.selectbox("In which  year are you studying",years)

#email
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False
    
email = st.text_input("Enter your email:")

# Check if the email format is valid
if email:
    if validate_email(email):
        st.success(f"Thank you, your email '{email}' is valid.")
    else:
        st.error("Please enter a valid email address.")


#phone number
# Function to check if input has exactly 10 digits
def validate_mob(input_value):
    if len(input_value) != 10 or not input_value.isdigit():
        st.error("Please enter exactly 10 digits.")
        return False
    return True

# Streamlit input field
mob = st.text_input("Enter a 10-digit number:")

if mob:
    # Validate the input when the user submits
    if validate_mob(mob):
        st.success(f"Valid input: {mob}")


#linkedin profile
linkedin = st.text_input("Enter your LinkedIn profile:")
if linkedin:
    st.write(f"Your linkedin profile is {linkedin}")


#choose between the domains
domains = ["Competitive Programming", 
            "Data Structures and Algorithm", 
            "Machine Learning",
            "Web Development",
            "Public Relation"]
chosed_doamin = st.selectbox(f"Choose your domain",domains)
if chosed_doamin:
    st.write(f"You have chosen {chosed_doamin}")


##resume
resume = st.file_uploader("Upload your resume", type=["pdf","docx"])