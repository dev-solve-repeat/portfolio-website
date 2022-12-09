import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email address: ")
    raw_message = st.text_area("Your message: ")
    message = f"""\
Subject: New mail received from : {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    print("1st time:", button)
    if button:
        send_mail(message)
        st.info("Your mail was send successfully.")