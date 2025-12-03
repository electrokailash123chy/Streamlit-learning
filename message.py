import streamlit as st  
st.title("Message Component Example")
user_message = st.text_input("Enter your message:")
if user_message:
    st.write(f"You entered: {user_message}")    