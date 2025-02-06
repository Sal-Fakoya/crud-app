import sqlite3

    
# Function to drop the existing table (optional, only use during development)
def drop_table():
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS task_table")
    connection.commit()
    connection.close()

# Function to create a new table
def create_table():
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS task_table(task_doer TEXT, task TEXT, task_status TEXT, task_due_date DATE);')
    connection.commit()
    connection.close()

# Function to add data to the table
def add_data(task_doer, task, task_status, task_due_date):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    # query = """
    # INSERT INTO task_table(task_doer, task, task_status, task_due_date) VALUES (?, ?, ?, ?);
    # """
    c.execute('INSERT INTO task_table(task_doer, task, task_status, task_due_date) VALUES (?, ?, ?, ?);', (task_doer, task, task_status, task_due_date))
    connection.commit()
    connection.close()

# Function to view tasks
def view_tasks():
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    query = """
    SELECT * FROM task_table;
    """
    c.execute(query)
    data = c.fetchall()
    connection.close()
    return data


def view_distinct_tasks():
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute("""
              SELECT DISTINCT task from task_table;
              """)
    data = c.fetchall()
    connection.close()
    return data
    
    
def get_task_by_task(task_doer):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute(f"""
              SELECT * FROM task_table 
              WHERE task_doer = "{task_doer}";
              """)
    data = c.fetchall()
    connection.close()
    return data

def get_task_by_task_name(task):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute(f"""
              SELECT * FROM task_table 
              WHERE task = "{task}";
              """)
    data = c.fetchall()
    connection.close()
    return data


def update_tasks(edit_task_doer, edit_task, edit_task_status, edit_task_due_date,
                 task_doer, task, task_status, task_due_date):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    c.execute("""
              UPDATE task_table 
              SET task_doer = ?, task = ?, task_status = ?, task_due_date = ? 
              WHERE task_doer = ? AND task = ? AND task_status = ? AND task_due_date = ?
              ;
              """, (edit_task_doer, edit_task, 
                    edit_task_status, edit_task_due_date, 
                    task_doer, task, task_status, task_due_date))
    connection.commit()  # commit the changes
    # data = c.fetchall()
    connection.close()
    # return data
    
    
def delete_tasks(task_doers):
    connection = sqlite3.connect("data.db")
    c = connection.cursor()
    for task_doer in task_doers:
        c.execute("""
                  DELETE FROM task_table WHERE task_doer = ?;
                  """, (task_doer,))
    connection.commit()  # commit the changes
    connection.close()
