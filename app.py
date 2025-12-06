import streamlit as st
import sqlite3
from datetime import datetime

# -----------------------------
# DATABASE
# -----------------------------
def init_db():
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            writer TEXT,
            description TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_project(title, writer, description):
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO projects (title, writer, description, date) VALUES (?, ?, ?, ?)",
        (title, writer, description, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()

def get_projects():
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("SELECT * FROM projects ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data

def delete_project(pid):
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("DELETE FROM projects WHERE id=?", (pid,))
    conn.commit()
    conn.close()


# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Portfolio", page_icon="⚡⚡⚡")
init_db()

st.title("💕My Project Portfolio ❤️")

page = st.sidebar.selectbox("Menu", ["Add Project", "View Projects", "About"])

# Add Project
if page == "Add Project":
    st.subheader("Add New Project")

    title = st.text_input("Title")
    writer = st.text_input("Writer Name")  # NEW FIELD
    desc = st.text_area("Description")

    if st.button("Save"):
        if title and writer and desc:
            add_project(title, writer, desc)
            st.success("Project saved!")
        else:
            st.error("Please fill all fields.")

# View Projects
elif page == "View Projects":
    st.subheader("Saved Projects")

    # -------------------------------
    # PASSWORD CHECK
    # -------------------------------
    password = st.text_input("Enter Password to View Projects", type="password")

    if password != "" and password != "kailash":
        st.error("Incorrect Password ")

    if password == "kailash":
        projects = get_projects()

        if not projects:
            st.info("No projects yet.")
        else:
            for p in projects:
                pid, title, writer, desc, date = p

                with st.expander(f"{title}  —  (Writer: {writer})"):
                    st.write(desc)
                    st.caption("Saved on: " + date)

                    if st.button("Delete", key=pid):
                        delete_project(pid)
                        st.warning("Deleted. Refreshing...")
                        st.experimental_rerun()

# About
else:
    st.subheader("About")
    st.write(
        "I am student of Electronic Communication and Automation Engineering at "
        "Khwopa Engineering College under Purbanchal University. "
        "This is my project portfolio website where I showcase my projects."
    )
    
    st.image("electrokailash.jpeg", caption="Me", width=400)

    st.write("""
    **Skills & Interests:**  
    - Arduino, ESP32, ESP8266  
    - IoT and Home Automation  
    - PCB Design and Simulation  
    - Web Development: HTML, PHP, Python  
    - MicroPython programming  
    - DIY projects and Proteus simulation
    """)
