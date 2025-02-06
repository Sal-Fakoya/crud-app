import streamlit as st

def run_about_page():
    st.markdown("""
    ## About This App

    Welcome to the **Task Management App**! This application is designed to help you efficiently manage your tasks, track their status, and stay organized. Whether you're working on personal projects or collaborating with a team, this app provides a simple and intuitive interface to handle all your task-related needs.

    ## Features

    ### 1. **Add Tasks**
    - Easily add new tasks by specifying the **Task Doer**, **Task Description**, **Task Status**, and **Due Date**.
    - Tasks are stored in a secure SQLite database for quick access and retrieval.

    ### 2. **Edit and Update Tasks**
    - Modify existing tasks to update their details, such as changing the task status or due date.
    - Keep your task list up-to-date with just a few clicks.

    ### 3. **Delete Tasks**
    - Remove tasks that are no longer needed.
    - Select multiple tasks to delete them in bulk.

    ### 4. **View and Search Tasks**
    - View all tasks in a clean, tabular format.
    - Search for specific tasks by **Task Doer** or **Task Description**.

    ### 5. **Task Analytics**
    - Gain insights into your tasks with visual analytics.
    - View pie charts showing the distribution of tasks by **Task Doer** and **Task Description**.

    ## How It Works
    - The app uses **SQLite** as its backend database to store and manage tasks.
    - The frontend is built using **Streamlit**, a powerful framework for creating web apps with Python.
    - Tasks can be added, updated, deleted, and searched seamlessly through an intuitive user interface.

    ## Why Use This App?
    - **Simple and User-Friendly**: No complicated setup or learning curve.
    - **Customizable**: Tailor tasks to your specific needs with flexible fields.
    - **Efficient**: Stay on top of your tasks with real-time updates and analytics.

    ## Get Started
    - Navigate to the **Task** section to add or edit tasks.
    - Use the **Manage** section to delete tasks or view analytics.
    - Explore the **Home** section to view all tasks and search for specific ones.

    """)
















