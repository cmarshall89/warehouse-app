import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Warehouse Manager", layout="wide")
st.title("🏗️ Warehouse Inventory System")

if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame({
        "Item": ["Concrete", "Rebar", "Lumber", "Cement" 500, 200, 1000, 300 "bags", "pieces", "boards", "bags" 50, 20, 100, 30]
    })

if "projects" not in st.session_state:
    st.session_state.projects = pd.DataFrame(columns= )

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Logged in as Admin!")
            st.rerun()
        elif username == "user" and password == "password":
            st.session_state.logged_in = True
            st.success("Logged in!")
            st.rerun()
        else:
            st.error("Wrong username or password")

if not st.session_state.logged_in:
    login()
    st.stop()

st.sidebar.success("Logged in successfully")

page = st.sidebar.selectbox("Menu", ["Dashboard", "Inventory", "Projects", "Pick Lists"])

if page == "Dashboard":
    st.header("Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Items", len(st.session_state.inventory))
    with col2:
        low = (st.session_state.inventory < st.session_state.inventory["Reorder Point"]).sum()
        st.metric("Low Stock Alerts", int(low))
    with col3:
        st.metric("Active Projects", len(st.session_state.projects))

elif page == "Inventory":
    st.header("Inventory")
    st.dataframe(st.session_state.inventory, use_container_width=True)
    
    with st.expander("Add New Item"):
        item = st.text_input("Item Name")
        qty = st.number_input("Quantity", min_value=0, value=100)
        reorder = st.number_input("Reorder Point", min_value=1, value=50)
        if st.button("Add Item"):
            new_row = pd.DataFrame({"Item": , "Quantity": , "Unit": , "Reorder Point": })
            st.session_state.inventory = pd.concat( , ignore_index=True)
            st.success("Item added!")
            st.rerun()

elif page == "Projects":
    st.header("Projects")
    project_name = st.text_input("New Project Name")
    if st.button("Create Project"):
        new_p = pd.DataFrame([{"Project Name": project_name, "Date Created": datetime.now().strftime("%Y-%m-%d")}])
        st.session_state.projects = pd.concat( , ignore_index=True)
        st.success(f"Project {project_name} created!")
        st.rerun()
    st.dataframe(st.session_state.projects, use_container_width=True)

elif page == "Pick Lists":
    st.header("Create Pick List")
    if not st.session_state.projects.empty:
        proj = st.selectbox("Select Project", st.session_state.projects )
        if st.button("Generate Pick List"):
            st.success(f"Pick list ready for {proj}!")
            st.info("In full version this would print a list and deduct from inventory.")
    else:
        st.warning("Create some projects first.")

st.sidebar.button("Logout", on_click=lambda: st.session_state.update(logged_in=False))
