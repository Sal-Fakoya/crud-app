import streamlit as st
from home import *
from post import *
from manage import *
from about import *

def select_menu():
    menu = ["Home", "Task", "Manage", "About"]
    choice = st.sidebar.selectbox("Menu", menu, key = "sidebar_selectbox")
    
    if choice == "Home":
        st.subheader("Home")
        run_home()
        
    elif choice == "Task":
        run_post_page()
        
    elif choice == "Manage":
       run_manage_page()
       
    elif choice == "About":
        run_about_page()
    


def main():
    st.title("CRUD APP (Tasklist)")
    select_menu()
    
    
    
    


if __name__ == "__main__":
    main()