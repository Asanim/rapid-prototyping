#!/usr/bin/env python3

# python code to unzip an anki apkg file like Chinese_Radicals_100.apkg, 
# then parse the sqlite database in anki version 2 format. I want to create a 
# copy of the sqlitedb, delete all items in the copy, keeping only the tables then sort 
# through the original database and copy a few entires in one by one. Please provide example code to do this

import os
import shutil
import sqlite3
from ankisync2.apkg import Apkg
#!/usr/bin/env python3
from collections import defaultdict
import re

def count_duplicates(string):
    char_counts = defaultdict(int)

    # Count the occurrences of each character
    for char in string:
        char_counts[char] += 1

    duplicates = []  # List for characters with duplicates
    uniques = []  # List for characters without duplicates

    # Separate characters into duplicates and uniques
    for char, count in char_counts.items():
        if count > 1:
            duplicates.append((char, count))
        else:
            uniques.append(char)

    # Sort the duplicates list by the number of duplicates in descending order
    duplicates.sort(key=lambda x: x[1], reverse=True)

    return duplicates, uniques

def keep_chinese_characters(string):
    chinese_chars = re.findall(r'[\u4e00-\u9fff]+', string)
    cleaned_string = ''.join(chinese_chars)
    return cleaned_string

def unzip_apkg(apkg_path):
    apkg = Apkg(apkg_path)
    apkg.close()

def get_sfld_to_id_map(database_path, key_value="sfld"):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT {key_value}, id FROM notes;")
    results = cursor.fetchall()

    # sfld_to_id_map = {sfld: id for sfld, id in results}
    
    sfld_to_id_map = {}

    for sfld, id in results:
        sfld_extracted = sfld.split("<img")[0]
        parsed_sfld = sfld_extracted.replace('\x1f', '')
        
        sfld_to_id_map[parsed_sfld] = id


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

def get_character_dictionary(database_path, original_db_path):
    # Unzip the APKG file
    unzip_apkg(database_path)

    #DEBUG
    print_table_headings_and_first_entry(original_db_path, "notes")

    print("get_sfld_to_id_map")
    sfld_to_id = get_sfld_to_id_map(original_db_path, "flds")

    return sfld_to_id

def detelete_all_entries_except(database_path, unique_ids):
    # Connect to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # List of unique key IDs to keep
    # unique_ids = [1, 2, 3]  # Replace with your actual list of IDs

    # Delete items from the notes table with IDs not in the unique_ids list
    cursor.execute(f"DELETE FROM notes WHERE id NOT IN ({','.join(map(str, unique_ids))})")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()



# Example usage
my_string = """
这个错误提示表明在调用DeleteThingGroup操作时请求中包含的安全令牌无效。

通常情况下这个错误是由于使用了无效或过期的安全令牌导致的。安全令牌通常用于验证和授权对AWS亚马逊网络服务资源的访问权限。

要解决这个问题你可以尝试以下步骤

检查令牌有效性确保你使用的安全令牌是有效的并且没有过期。如果你是使用AWS Identity and Access Management (IAM) 创建的访问密钥可以在AWS控制台的IAM部分进行验证和更新。

检查令牌权限确保你的安全令牌具有执行DeleteThingGroup操作所需的必要权限。你可以通过IAM角色或用户策略来管理权限。检查相关策略是否正确配置并包含DeleteThingGroup操作的权限。

检查网络连接确保你的应用程序能够与AWS服务进行通信没有任何网络连接问题。检查网络设置、防火墙或代理配置确保可以正常访问AWS服务。

如果你仍然遇到问题建议参考AWS官方文档、开发者论坛或联系AWS支持以获取更详细的帮助和指导。
"""
apkg_path = "Most_Common_3000_Chinese_Hanzi_Characters.apkg"
if os.path.exists(apkg_path):
    print("File path is valid.")
else:
    print("File path is invalid.")

print("keep_chinese_characters")
cleaned_string = keep_chinese_characters(my_string)

print("count_duplicates")
duplicates, uniques = count_duplicates(cleaned_string)


extraction_dir = "./"+os.path.splitext(apkg_path)[0]+"/"
print(extraction_dir)
original_db_path = os.path.join(extraction_dir, "collection.anki2")

print("get_character_dictionary")
sfld_to_id =  get_character_dictionary(apkg_path, original_db_path)


print("Map of sfld to id:")
for sfld, id in sfld_to_id.items():
    print(f"sfld: {sfld}, id: {id}")


# Print the duplicates and uniques
# extract the duplicates from the count
duplicates_list = []
for char, count in duplicates:
    print(f"Character: {char}, Duplicates: {count}")
    duplicates_list.append(char)

print("\nCharacters without duplicates:")
for char in uniques:
    print(f"Character: {char}")

print("duplicates_list")
print(duplicates_list)
# discard the number of 
total_characters = uniques + duplicates_list

# print("keys")
# print(sfld_to_id.keys())

equal_entries = [entry for entry in total_characters if entry in sfld_to_id.keys()]

# Print the matched characters and their corresponding numbers
print("\nMatched characters and their corresponding numbers:")
for entry in equal_entries:
    number = sfld_to_id[entry]
    print(f"Character: {entry}, Number: {number}")

