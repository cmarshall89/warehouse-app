import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Warehouse Manager", layout="wide")
st.title("🏗️ Warehouse Inventory System")

# Initialize data
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {"password": "admin123", "role": "admin"},
        "chad": {"password": "password", "role": "user"}
    }

if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame({
        "Item": ["Concrete", "Rebar", "Lumber", "Cement" 500, 200, 1000, 300],
        "Unit": ,
        "Reorder Point": [50, 20, 100, 30]
    })

if "projects" not in st.session_state:
    st.session_state.projects = pd.DataFrame(columns= )

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "role" not in st.session_state:
    st.session_state.role = None

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users  == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.session_state.role = st.session_state.users ["role"]
            st.success(f"Welcome, {username}!")
            st.rerun()
        else:
            st.error("Invalid username or password")

if not st.session_state.logged_in:
    login()
    st.stop()

st.sidebar.success(f"Logged in as: {st.session_state.current_user} ({st.session_state.role})")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()
