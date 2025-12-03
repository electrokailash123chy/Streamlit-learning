import streamlit as st  
import pandas as pd
import numpy as np
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
uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.write("uploaded file:",uploaded_file.name)  
  #  st.text(uploaded_file.getvalue().decode("utf-8"))
st.write("sample data visualization:")
data = pd.DataFrame(
    np.random.randn(10, 3),
   columns=["A", "B", "C"]
)
st.line_chart(data)