import streamlit as st

st.set_page_config(layout= "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Pic 6.jpg")

with col2:
    st.title("Brijesh Babu")
    content = """Hi, I am Brijesh Babu. I have done various projects in Python, javascript and React. 
    I am well versedin all these technologies. I have worked with various organisation. 
    One of them is UST Global, in which I had worked in Mainframe Technologies. 
    I love creating new apps using these skills and hope to do more."""
    st.info(content)

content2 = """Below you can find some of the app I have built in Python.
         Feel free to contact me!"""
st.write(content2)