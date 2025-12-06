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
st.write("File Uploader Example:")
file = st.file_uploader("Upload CSV", type="csv")
if file:
    st.dataframe(pd.read_csv(file))
import streamlit as st

st.write("Select Slider Example:")
choice = st.select_slider("Choose:", ["Low", "Medium", "High"], "Medium")
st.write("You selected:", choice)
st.write("Expander Example:")
with st.expander("More Info"):
    st.write("This is hidden content.")
    st.write("You can add details here.")
st.write("Progress Spinner Example:")
with st.spinner("Processing..."):
    time.sleep(2)  # Simulate a long-running process
st.success("Done!")  
st.write("Session State Example:")
if "counter" not in st.session_state:
    st.session_state.counter = 0
if st.button("Increment"):
    st.session_state.counter += 1
st.write("Counter:", st.session_state.counter)
st.write("Markdown Example:")
st.markdown("""
### This is a Markdown Header
You can use **bold text**, *italic text*, or `inline code`.
Create lists
1. [Google](https://google.com)
2. [Streamlit](https://streamlit.io)
3. [GitHub](https://github.com)
""")
# Add a file download example
st.write("File Download Example:")
text_content = "This is a sample text file for download."
st.download_button("Download Text File", text_content, file_name="sample.txt")

st.title("Column Layout Example")

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Column 1
with col1:
    st.header("📌 Column 1")
    st.write("This column can contain text, buttons, or images.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    if st.button("Click Me"):
        st.success("Button in Column 1 clicked!")

# Column 2
with col2:
    st.header("📊 Column 2")
    st.write("You can display charts or metrics here.")
    st.metric(label="Visitors Today", value="1,245", delta="+12%")
    st.metric(label="Active Users", value="87", delta="-5")

# Column 3
with col3:
    st.header("⚙️ Column 3")
    st.write("Useful for inputs or settings.")
    selected = st.selectbox("Choose an option:", ["Option A", "Option B", "Option C"])
    st.write("You selected:", selected)
# Add a sidebar input example
st.write("Sidebar Input Example:")
sidebar_text = st.sidebar.text_input("Enter text in the sidebar:")
st.sidebar.write("You entered:", sidebar_text)
# Add a file uploader in the sidebar
st.write("Sidebar File Uploader Example:")
uploaded_sidebar_file = st.sidebar.file_uploader("Upload a file in the sidebar")
if uploaded_sidebar_file is not None:
    st.sidebar.write("Uploaded file name:", uploaded_sidebar_file.name)
# Add a multi-select example
st.write("Multi-Select Example:")
multi_select_options = st.multiselect(
    "Select multiple options:",
    ["Option 1", "Option 2", "Option 3", "Option 4"],
    default=["Option 1"]
)
st.write("You selected:", multi_select_options)   