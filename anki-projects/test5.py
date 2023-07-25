#!/usr/bin/env python3

# python code to unzip an anki apkg file like Chinese_Radicals_100.apkg, 
# then parse the sqlite database in anki version 2 format. I want to create a 
# copy of the sqlitedb, delete all items in the copy, keeping only the tables then sort 
# through the original database and copy a few entires in one by one. Please provide example code to do this

import os
import shutil
import sqlite3
# import ankisync2 as anki
from ankisync2 import Apkg
from peewee import *

def get_sfld_to_id_map(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT sfld, id FROM notes;")
    results = cursor.fetchall()

    sfld_to_id_map = {sfld: id for sfld, id in results}

    conn.close()

    return sfld_to_id_map

def print_table_headings_and_first_entry(database_path, table_name):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Get the table columns (headings)
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    headings = [column[1] for column in columns]

    # Print the headings
    print("Table Headings:")
    print(headings)

    # Get the first entry in the table
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 1;")
    first_entry = cursor.fetchone()

    # Print the values of the first entry
    print("\nFirst Entry Values:")
    print(first_entry)

    conn.close()



# Example usage
apkg_path = "Chinese_Radicals_100.apkg"
extraction_dir = "./"+os.path.splitext(apkg_path)[0]+"/"
print(extraction_dir)
original_db_path = os.path.join(extraction_dir, "collection.anki2")

# extraction_dir = "./Chinese_Radicals_100"
# copy_db_path = "copy_collection.anki2"
# original_db_path = os.path.join(extraction_dir, "collection.anki2")

# Unzip the APKG file
apkg = Apkg(apkg_path)  # Create example folder





# Connect to the SQLite database
conn = sqlite3.connect(original_db_path)  # Replace with your actual database

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Define the update query
update_query = '''
    UPDATE notes
    SET tags = ?
'''

# Set the new value for tags
new_tags = 'New Tags'  # Replace 'New Tags' with the new value you want to assign

# Execute the update query with the new value
cursor.execute(update_query, (new_tags,))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()



# def export(self, filename: Union[str, Path]):
# apkg.export("extracted_apkg.apkg")
apkg.close()
