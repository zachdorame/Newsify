# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:39:36 2021

@author: Jacob's PC
"""

import sqlite3 as sql

def initialize():
	conn = sql.connect("positions.db")

	cur = conn.cursor()

	cur.execute('''
					CREATE TABLE POSITIONS
                        (ID integer PRIMARY KEY, positionName text, employer text, 
                         postingLink text, deadlineExists integer, dueDate text)
				''')

	conn.close()

    
    
if __name__ == "__main__":
    initialize()
    
    print("Server Initialized")