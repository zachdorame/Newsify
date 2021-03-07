# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:56:44 2021

@author: Jacob's PC
"""

import pandas as pd
import sqlite3 as sql


def generate_output_csv():
    
    conn = sql.connect("positions.db")
    
    query = pd.read_sql_query("SELECT * FROM POSITIONS", conn)
    
    df = pd.DataFrame(query)
    
    df["Job Title"] = '=HYPERLINK("' + df['postingLink'] + '","' + df['positionName']+ '")'
    df["Employer"] = '=HYPERLINK("' + df['employerLink'] + '","' + df['employer']+ '")'
    
    df = df.drop(["ID", "positionName", "postingLink", "employerLink"], axis=1)
    
    df = df[["Job Title", "Employer", "location", "dueDate"]]
    
    df.rename(columns = {"location": "Location", "dueDate": "Application Deadline"}, inplace=True)
    
    print(df)
    
    df.to_csv("test.csv", index=False)
    

if __name__ == "__main__":
    generate_output_csv()

