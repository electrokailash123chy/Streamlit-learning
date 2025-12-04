import streamlit as st  
import pandas as pd
import numpy as np
import time
from PIL import Image
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
st.write("color picker example:")
color = st.color_picker("Pick a color:", "#00f900")
st.write("You selected:", color)
st.write("file downloader example:")    
text_file = " this is a sample text file for download."
st.download_button("Download text file", text_file, file_name="sample.txt")
st.write("You can download the above text file.")
st.sidebar.write("This is the sidebar.")    
sidebar_option = st.sidebar.selectbox("Sidebar option:", options)
st.sidebar.write("You selected in sidebar:", sidebar_option)
st.write("metric example:")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
st.write("You can see the temperature metric above.")   
st.write("data table example:")
data_table = pd.DataFrame(
    {
        "column 1": [1, 2, 3, 4],
        "column 2": [10, 20, 30, 40],
        "column 3": ["A", "B", "C", "D"]
    }
)
st.table(data_table)
st.write("Line Chart Example:")
bar_chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Column A", "Column B", "Column C"]
)
st.bar_chart(bar_chart_data)
st.write("Area Chart Example:")
area_chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Column X", "Column Y", "Column Z"]
)
st.area_chart(area_chart_data)
st.write("Khwopa engineering college locations on map:")
map_data = pd.DataFrame(
    [[27.67088, 85.43969],
     [27.67104, 85.42982]],
    columns=["lat", "lon"]
)

st.map(map_data)
img = Image.open("kailash.jpg")
st.image(img, caption="My Image", use_container_width=True)
st.write("simple pcd design example:")
st.video("led ckt.mp4")
st.write("Audio Example:")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.write("Code Snippet Example:")
st.code("import streamlit as st\n\nst.title('Hello, Streamlit!')", language="python")
import streamlit as st

st.write("Form Example:")

with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    if st.form_submit_button("Submit"):
        st.write(f"Hello {name}, you are {age} years old!")
