#!/usr/bin/env python3

# finding equal entires between a python map and a list example

map_entries = {'A': 5, 'B': 12, 'C': 323, 'D': 4}
list_entries = ['B', 'C', 'E', 'F']

# Find the equal entries between the map and the list
equal_entries = [entry for entry in list_entries if entry in map_entries]

# Print the matched characters and their corresponding numbers
for entry in equal_entries:
    number = map_entries[entry]
    print(f"Character: {entry}, Number: {number}")
