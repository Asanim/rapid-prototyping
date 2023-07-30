

print("v3")

'''
list individual ids
'''
def sort_list_indiviudal_ids
    my_set = { 5, 5, 5, 5, 5, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4}

    # Convert the set to a list
    my_list = list(my_set)

    # Sort the list based on the frequency of elements
    sorted_list = sorted(my_list, key=my_list.count, reverse=True)

    for element in sorted_list:
        print(element, ":", my_list.count(element))


'''
parset the anki database
'''

def copy_and_clear_database(original_db_path, copy_db_path):
    shutil.copy(original_db_path, copy_db_path)
    conn.commit()
    conn.close()

def copy_entries(original_db_path, copy_db_path, entry_count):
    conn_original = sqlite3.connect(original_db_path)
    conn_copy = sqlite3.connect(copy_db_path)
    cursor_original = conn_original.cursor()
    cursor_copy = conn_copy.cursor()

    # Copy specific entries from the original database to the copy
    cursor_original.execute("SELECT * FROM your_table_name LIMIT ?;", (entry_count,))
    entries = cursor_original.fetchall()
    for entry in entries:
        # Modify the logic here to select and copy specific entries based on your requirements
        cursor_copy.execute("INSERT INTO your_table_name VALUES (?, ?);", entry)

    conn_copy.commit()
    conn_copy.close()
    conn_original.close()

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

def print_all_tables_and_values(original_db_path):
    conn = sqlite3.connect(original_db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        print(table_name)

        # cursor.execute("SELECT * FROM cards;")
        cursor.execute(f"SELECT * FROM {table_name};")

        cards = cursor.fetchall()

        for card in cards:
            print(card)

def sanity_check1():
    arr1 = ['id', 'guid', 'mid', 'mod', 'usn', 'tags', 'flds', 'sfld', 'csum', 'flags', 'data']
    print(len(arr1))
    arr2 = [1453219106197, 'o_4h`pop|W', 1453218888792, 1457014305, 0, '', '人\x1f人\x1f亻&nbsp;\x1f\x1fhuman, person, people\x1frén\x1fNote similarity to 八, which means eight.&nbsp;\x1f今仁休位他\x1f[sound:pronunciation_zh_人.mp3]', '人', 1225946906, 0, '']
    print(len(arr2))