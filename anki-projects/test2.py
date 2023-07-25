#!/usr/bin/env python3

# python code to unzip an anki apkg file like Chinese_Radicals_100.apkg, 
# then parse the sqlite database in anki version 2 format. I want to create a 
# copy of the sqlitedb, delete all items in the copy, keeping only the tables then sort 
# through the original database and copy a few entires in one by one. Please provide example code to do this

import os
import shutil
import sqlite3
from ankisync2.apkg import Apkg

def unzip_apkg(apkg_path):
    apkg = Apkg(apkg_path)
    apkg.close()

def get_sfld_to_id_map(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT sfld, id FROM notes;")
    results = cursor.fetchall()

    sfld_to_id_map = {sfld: id for sfld, id in results}

    conn.close()

    return sfld_to_id_map


# Example usage
apkg_path = "Chinese_Radicals_100.apkg"
extraction_dir = "./Chinese_Radicals_100"
copy_db_path = "copy_collection.anki2"

original_db_path = os.path.join(extraction_dir, "collection.anki2")

# Unzip the APKG file
unzip_apkg(apkg_path)

# print_table_headings_and_first_entry(original_db_path, "notes")
sfld_to_id = get_sfld_to_id_map(original_db_path)

print("Map of sfld to id:")
for sfld, id in sfld_to_id.items():
    print(f"sfld: {sfld}, id: {id}")


print("Process completed.")
