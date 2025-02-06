import streamlit as st
import pandas as pd
from db_funcs import *

import plotly.express as px

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("Agg")

def run_delete():
    st.subheader("Manage Tasks")
    results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])    
    
    with st.expander("Delete Task", expanded=True):
        select_task_doers = st.multiselect("Select Task Doers to Delete", 
                                           results["task_doer"], 
                                           key="select_multi_delete_" + str(len(results)))
        
    
        delete = st.button("Delete", key="delete_tasks_btn_" + str(len(results))) 
    
    if delete and select_task_doers:
        delete_tasks(select_task_doers)
        st.success(f"Deleted tasks for: {', '.join(select_task_doers)}")
        
        # Refresh the DataFrame after deletion
        results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])    
    
    with st.expander("View Results"):
        st.dataframe(results, use_container_width=True)


def run_analytics():
    st.subheader("Analytics")
    results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])    
        
    with st.expander("Task Doer Analytics", expanded = False):
        
        # Create value counts:
        task_doer_count = results['task_doer'].value_counts()
        # st.dataframe(task_doer_count)
        
        task_doer_count = task_doer_count.reset_index()
        st.table(task_doer_count)
       
        p1 = px.pie(task_doer_count, names="task_doer", values = "count")
        st.plotly_chart(p1)
        
    with st.expander("Task Analytics", expanded = False):
      
        # Create value counts:
        task_count = results['task'].value_counts()
        # st.dataframe(task_doer_count)
        
        task_count = task_count.reset_index()
        st.table(task_count)
       
        
        p2 = px.pie(task_count, names="task", values = "count")
        st.plotly_chart(p2)

def run_manage_page():
    tabs = ["Delete Task", "Analytics"]
    tab1, tab2 = st.tabs(tabs)
    
    with tab1:
        run_delete()
    
    with tab2:
        run_analytics()