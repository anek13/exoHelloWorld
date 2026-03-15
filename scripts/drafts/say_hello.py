"""
This script reads a list of people and their courses, and writes a greeting for each person who is taking a specific course to a text file.
"""
import json

# Load the list of people from the external JSON file
# PILLAR: Data (the file content), Environment (the file path 'data/raw/people.json'), Code (open/json.load)
with open('data/raw/people.json', 'r') as f:
    people = json.load(f)

# Course we are interested in - configuration to be put in config file as a json or yaml file
course = 'pSciComp'
# Declaration of the list to store greetings - Code
greetings = []
"""
Loop through the list of people and check if they are taking the specified course. If they are, add a greeting to the greetings list.
Could be moved as a function into srcs but is so simple
"""
# initating the loop to check if the person is taking the course and if so, add a greeting to the greetings list - Code
for person in people:
    # 'courses' is the key word from the config, need to replace it with the variable
    # if course in person[cfg.courses]:
    if course in person['courses']:
        # greetings.append(f"Hello {config.name}\n")
        greetings.append(f"Hello {person['name']}\n")
# Write the greetings to a text file
# Code instruct to open the file, what file to open is environment, 'w' is configuration 
with open('data/final/greeting.txt', 'w') as f:
    # Code
    f.writelines(greetings)