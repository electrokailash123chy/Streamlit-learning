import streamlit as st
import sqlite3
from datetime import datetime

# -----------------------------
# DATABASE SETUP
# -----------------------------
def init_db():
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_project(title, description):
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("INSERT INTO projects (title, description, date) VALUES (?, ?, ?)",
              (title, description, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()

def get_projects():
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("SELECT * FROM projects ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_project(project_id):
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit()
    conn.close()


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Project Portfolio", page_icon="📁", layout="wide")

init_db()

st.title("📁 My Project Portfolio Website")
st.write("Create, store and display your projects like a BlogSpot website!")

menu = st.sidebar.selectbox("Menu", ["Add Project", "View Projects", "About"])

# -----------------------------
# ADD PROJECT PAGE
# -----------------------------
if menu == "Add Project":
    st.subheader("➕ Add New Project")

    title = st.text_input("Project Title")
    desc = st.text_area("Project Description")

    if st.button("Save Project"):
        if title.strip() == "" or desc.strip() == "":
            st.error("Please fill all fields!")
        else:
            add_project(title, desc)
            st.success("Project added successfully!")

# -----------------------------
# VIEW PROJECTS PAGE
# -----------------------------
elif menu == "View Projects":
    st.subheader("📄 Your Saved Projects")

    projects = get_projects()

    if len(projects) == 0:
        st.info("No projects found. Add a project from the left menu.")
    else:
        for p in projects:
            with st.expander(f"📌 {p[1]}"):
                st.write(p[2])
                st.caption(f"🕒 Saved on: {p[3]}")
                if st.button("Delete", key=p[0]):
                    delete_project(p[0])
                    st.warning("Project deleted. Refresh the page.")
                    st.experimental_rerun()

# -----------------------------
# ABOUT PAGE
# -----------------------------
elif menu == "About":
    st.subheader("ℹ️ About This Website")
    st.write("""
    This is a simple Portfolio/Blog website built using **Streamlit + SQLite**.  
    You can:
    - Add your projects  
    - Save them in a database  
    - View and delete projects anytime  
    - Deploy online (Streamlit Cloud / GitHub)
    """)

