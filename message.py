import streamlit as st  
st.title("Message Component Example")
user_message = st.text_input("Enter your message:")
if st.button("Submit"): 
    if user_message:
        st.write("You entered:", user_message)
    else:
        st.write("Please enter a message.")
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an option:", options)
st.write("You selected:", selected_option)