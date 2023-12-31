import sqlite3
import streamlit as st
import time
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if 'otp_pass' not in st.session_state:
    st.session_state.otp_pass = None
    
conn = sqlite3.connect('sgpa.db')
cursor = conn.cursor()

st.subheader('GECA SGPA calculator')
st.text('Developed By Saad and Team')
branches = ['Civil', 'Electrical', 'Mechanical', 'EnTC', 'CSE', 'IT']
semesters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
operation = st.sidebar.radio("Select", ['student','admin'])

def sgpa(branch, semester):
        st.subheader('hold on we are working!!')
        
def send_otp():
    smtp_server = 'smtp-relay.brevo.com'
    smtp_port = 587 
    smtp_username = 'saadiqbal1921@geca.ac.in'  
    smtp_password = 'VEDM3Qg7mnC2qz4H'  
    sender_email = 'otp@geca.in'
    recipient_email = 'saadiqbal1921@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'otp'
    length = 4
    characters = string.ascii_uppercase + string.ascii_lowercase
    random_text = ''.join(random.choice(characters) for _ in range(length))
    email_content = random_text
    st.session_state.otp_pass = random_text  # Store the OTP in session_state
    msg.attach(MIMEText(email_content, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    succ = st.success('otp sent')
    time.sleep(3)
    succ.empty()
    #st.header(random_text)
    return random_text

if operation == 'student':
    col1,col2 = st.columns(2)
    branch = col1.selectbox('Branch', [''] + branches)
    semester = col2.selectbox('Semester', [''] + semesters)
    st.markdown('---')
    if branch == '' or semester == '':
        st.header('SELECT BRANCH AND SEM')
    else:
        sgpa(branch,semester)

def admin_login():
    st.subheader('LOGGED IN as admin')
    
    
if operation == 'admin':
    st.subheader('Welcome to admin panel')

    a, b = st.columns(2)
    c, d, e, f, g, h, i = st.columns(7)
    username = a.text_input("Username")
    otp = b.text_input('OTP')
    get_otp = c.button('Get OTP')
    login = d.button("Login")

    if get_otp and username == 'admin@geca':
        st.session_state.otp_pass = send_otp()
    
    elif get_otp:
        st.error('Incorrect Username')
    if login:
        if st.session_state.otp_pass is not None and otp == st.session_state.otp_pass:
            admin_login()
        else:
            st.error('Incorrect OTP')
        

#added a comment to check
