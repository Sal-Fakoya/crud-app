
import streamlit as st
import numpy as np
import pandas as pd
from db_funcs import *

def run_home():
    
    task_list = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])    
    choice = st.sidebar.selectbox("SubMenu", ["My Task", "Search"], key="select_submenu_home")
    
    with st.expander("View Results", expanded = True):
        st.dataframe(task_list, use_container_width=True)
        
    if choice == "My Task":
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.info("Task List")
            select_task = st.selectbox("Your Task", task_list["task_doer"], key="selectbox_task_list")
            
        with col2: 
            st.info("Details")
            task_result = get_task_by_task(select_task)
            
            try: 
                task_doer = task_result[0][0]
                st.write(f"Task Doer: {task_doer}")
                
                task = task_result[0][1]
                st.write(f"Task     : {task}")
                
                task_status = task_result[0][2]
                st.write(f"Task status: {task_status}")
                
                task_due_date = task_result[0][3]
                st.text(f"Task Due Date: {task_due_date}")
            except Exception as e:
                st.info("Please add a new task")
        
    elif choice == "Search":
        st.subheader("Search")
        search_term = st.text_input("Search Term")
        search_choice = st.radio("Field To Search:",
                                 ("Task Doer", "Task"),
                                 horizontal = True)
        
        if st.button("Search"):
            
            if search_choice == "Task":
                search_result = get_task_by_task_name(search_term)
                st.write(search_result)
            else:
                search_result = get_task_by_task(search_term)
                st.write(search_result)
    

















