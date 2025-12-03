import streamlit as st  
import pandas as pd
import numpy as np
import time
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
st.write("Adjust the slider:")
slider_value = st.slider("Select a value:", 0, 100, 50)
st.write("Slider value is :", slider_value) 
st.write("progress bar example:")
progress_bar = st.progress(0)
for percent_complete in range(101):
    time.sleep(0.05)
    progress_bar.progress(percent_complete) 
st.write("progress complete")
st.write("checkbox example:")
if st.checkbox("show/hide"):
    st.write("Checkbox is checked!")
else:
    st.write("Checkbox is unchecked!")
st.write("radio button example:")
radio_choice = st.radio("Select an option:", options)
st.write("You selected:", radio_choice) 
st.write("date input example:")
selected_date = st.date_input("Select a date:")
st.write("You selected:", selected_date)
st.write("time input example:")
selected_time = st.time_input("Select a time:")
st.write("You selected:", selected_time)
st.write("number input example:")
number_input = st.number_input("Enter a number:")
st.write("You entered:", number_input)