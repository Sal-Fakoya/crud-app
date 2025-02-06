import streamlit as st
import pandas as pd
from db_funcs import *


def get_submenu(submenu):
    if submenu == "Add Task":
        st.subheader("Add Task")
        col1, col2 = st.columns(2)
    
        with col1:
            task_doer = st.text_input("Task Doer", key="task_doer")
            task = st.text_area("Task", key="task")
            
        with col2:
            task_status = st.selectbox("Task Status", ["ToDo", "In Progress", "Completed", "Uncertain"], key = "select_boxAdd")
            task_due_date = st.date_input("Due Date")
        
        add_task = st.button("Add", key="submit_add")
        
        if add_task and len(task.strip()) > 0:
            add_data(task_doer, task, task_status, task_due_date)
            st.success(f"Added: {task}")
        elif add_task and len(task.strip()) == 0:
            st.info("Please add a task to continue")
        
        results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
        with st.expander("View Tasks"):
            st.dataframe(results, use_container_width=True)
    
    elif submenu == "Edit Task":
        st.subheader("Update | Edit Task")
        
        results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
        
            
        with st.expander("Update Task", expanded = True):
            select_task = st.selectbox("Select Task", results["task_doer"], key="selectbox_upp")
            task_result = get_task_by_task(select_task)
            
            if task_result:
                col1, col2 = st.columns(2)
                task_doer = task_result[0][0]
                task = task_result[0][1]
                task_status = task_result[0][2]
                task_due_date = task_result[0][3]
                
                with col1:
                    edit_task_doer = st.text_input("Task Doer", key="update_task_doer", value=task_doer)
                    edit_task = st.text_area("Task", key="update_task", value=task)
                    
                with col2:
                    task_status_opt = ["ToDo", "In Progress", "Completed", "Uncertain"]
                    edit_task_status = st.selectbox("Task Status", task_status_opt, index=task_status_opt.index(task_status), key = "selectbox_stat")
                    edit_task_due_date = st.date_input("Due Date", value=pd.to_datetime(task_due_date))
                
                update_task = st.button("Update", key="submit_update")
                
                if update_task and len(edit_task.strip()) > 0:
                    update_tasks(edit_task_doer, edit_task, edit_task_status, edit_task_due_date,
                                 task_doer, task, task_status, task_due_date)
                    st.success(f"Updated: {edit_task}")
                    results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
                    st.table(results)
                elif update_task and len(edit_task.strip()) == 0:
                    st.info("Please add a task to continue")


def run_post_page():
    create_table()
    submenu = st.sidebar.selectbox("SubMenu", ["Add Task", "Edit Task"], key="select_btn_yes")
    get_submenu(submenu)




# import streamlit as st
# import pandas as pd
# from db_funcs import *


# def get_submenu(submenu):
#     if submenu == "Add Task":
#         st.subheader("Add Task")
#         col1, col2 = st.columns(2)
    
#         with col1:
#             task_doer = st.text_input("Task Doer", key = "task_doer")
#             task = st.text_area("Task", key="task")
            
#         with col2:
#             task_status = st.selectbox("Task Status", ["ToDo", "In Progress", "Completed", "Uncertain"])
            
#             task_due_date = st.date_input("Due Date")
        
#         add_task = st.button("Add")
        
#         if add_task and len(task.strip(" ")) > 0:
#             add_data(task_doer, task, task_status, task_due_date)
#             st.success(f"Added: {task}")
            
#         elif add_task and len(task.strip(" ")) == 0:
#             st.info("Please add a task to continue")
        
        
#         results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
#         with st.expander("View Tasks"):
#             st.dataframe(results, use_container_width = True)
    
#     elif submenu == "Edit Task":
#         st.subheader("Update | Edit Task")
        
#         distinct_results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
#         results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
#         with st.expander("View Tasks"):
#             st.table(distinct_results)
            
#         with st.expander("Select Task"):
#             select_task = st.selectbox("Select task", results["task"])
#             task_result = get_task_by_task(select_task)
#             # st.write(task_result)
            
#             if task_result:
#                 col1, col2 = st.columns(2)
#                 task_doer = task_result[0][0]
#                 task = task_result[0][1]
#                 task_status = task_result[0][2]
#                 task_due_date = task_result[0][3]
                
#                 with col1:
#                     edit_task_doer = st.text_input("Task Doer", key = "update_task_doer", value = task_doer)
#                     edit_task = st.text_area("Task", key="update_task", value = task)
                    
#                 with col2:
#                     task_status_opt = ["ToDo", "In Progress", "Completed", "Uncertain"]
#                     edit_task_status = st.selectbox("Task Status", task_status_opt, index = task_status_opt.index(task_status))
                    
#                     edit_task_due_date = st.date_input(task_due_date)
                
#                 update_task = st.button("Update")
                
#                 if update_task:
#                     updated_tasks =  pd.DataFrame(update_tasks(edit_task_doer, edit_task,
#                                                                edit_task_status, edit_task_due_date,
#                                                                task_doer, task, task_status, task_due_date), 
#                                                   columns=["task_doer", "task", "task_status", "task_due_date"])
#                     results = pd.DataFrame(view_tasks(), columns=["task_doer", "task", "task_status", "task_due_date"])
#                     st.table(distinct_results)
            
#                 if update_task and len(edit_task.strip(" ")) > 0:
#                     add_data(task_doer, task, task_status, task_due_date)
#                     st.success(f"Updated: {task}")
                    
#                 elif update_task and len(edit_task.strip(" ")) == 0:
#                     st.info("Please add a task to continue")
        
                

           
                
        
        
        

# # Create edit and update
# def run_post_page():
        
#     # drop_table()
#     create_table()
    
#     submenu = st.sidebar.selectbox("SubMenu", ["Add Task", "Edit Task"])
#     get_submenu(submenu)
    
    
    











