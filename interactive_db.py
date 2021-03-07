"""
all the functions needed to interact with the database
"""
import sqlite3 as sql
import datetime


def add_listing(input_string):
    
    positionName, employer, location, postingLink, employerLink, dueDate = input_string.split("; ")

    conn = sql.connect("positions.db")
    cur = conn.cursor()
    
    cur.execute(f"""
                  INSERT INTO POSITIONS 
                  (ID, positionName, employer, location, postingLink, employerLink, dueDate)
                  VALUES 
                  ({_new_ID()}, '{positionName}', '{employer}', '{location}', '{postingLink}', '{employerLink}', '{dueDate}')""")
    conn.commit()
    conn.close()

def remove_listing(ID):

    conn = sql.connect("positions.db")
    cur = conn.cursor()
    
    cur.execute(f"DELETE FROM POSITIONS WHERE ID = {ID}")
    
    conn.commit()
    
    conn.close()

def purge():

    conn = sql.connect("positions.db")
    cur = conn.cursor()
    
    cur.execute("""
                DELETE FROM POSITIONS WHERE ID IN (
                    SELECT ID FROM POSITIONS
                        WHERE dueDate < date('now')
                    )
                """)
    conn.commit()
    conn.close()

def _is_redundant():

    pass

def modify_listing():

    pass

def show_listing(ID):
    
    try:

        return next(sql.connect("positions.db").cursor().execute(f"SELECT * FROM POSITIONS WHERE ID = {ID}"))
    
    except StopIteration:
        print("Invalid ID")
        
def show_all_listings():
    return "\n".join([str(x) for x in sql.connect("positions.db").cursor().execute("SELECT * FROM POSITIONS")])


def _new_ID():
    max_ID = next(sql.connect("positions.db").cursor().execute("""SELECT MAX(ID) FROM POSITIONS"""))[0]
    if type(max_ID) == int:
        return max_ID + 1
    else:
        return 1
