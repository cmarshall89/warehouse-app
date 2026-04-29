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
# Dashboard
st.header("Dashboard")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Items", len(st.session_state.inventory))
with col2:
    low_stock = len(st.session_state.inventory[st.session_state.inventory["Quantity"] < st.session_state.inventory ])
    st.metric("Low Stock", low_stock, "⚠️")
with col3:
    st.metric("Active Projects", len(st.session_state.projects))
with col4:
    st.metric("Users", len(st.session_state.users))

# Navigation
page = st.sidebar.selectbox("Go to", ["Inventory", "Projects", "Pick Lists", "Admin" if st.session_state.role == "admin" else ""])

if page == "Inventory":
    st.subheader("Inventory Management")
    st.dataframe(st.session_state.inventory, use_container_width=True)
    
    with st.expander("Add New Item"):
        item = st.text_input("Item Name")
        qty = st.number_input("Quantity", min_value=0)
        reorder = st.number_input("Reorder Point", min_value=1, value=50)
        if st.button("Add Item"):
            new_row = pd.DataFrame({"Item": , "Quantity": , "Reorder Point": })
            st.session_state.inventory = pd.concat( , ignore_index=True)
            st.success("Item added!")
            st.rerun()

elif page == "Projects":
    st.subheader("Projects")
    project_name = st.text_input("Project Name")
    if st.button("Create Project"):
        st.session_state.projects = pd.concat( })], ignore_index=True)
        st.success("Project created!")

    st.dataframe(st.session_state.projects)

elif page == "Pick Lists":
    st.subheader("Create Pick List")
    if not st.session_state.projects.empty:
        selected_project = st.selectbox("Select Project", st.session_state.projects )
        if st.button("Generate Pick List"):
            st.success(f"Pick list generated for {selected_project}!")
            st.info("Materials will be deducted from inventory here in final version")
    else:
        st.warning("Create a project first")

elif page == "Admin":
    st.subheader("Admin Panel - Manage Users")
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    if st.button("Add User"):
        if new_user and new_pass:
            st.session_state.users = {"password": new_pass, "role": "user"}
            st.success(f"User {new_user} added!")
            st.rerun()
