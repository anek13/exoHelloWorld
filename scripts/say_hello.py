"""
This script reads a list of people and their courses, and writes a greeting for each person who is taking a specific course to a text file.
"""
from exohw.utils import load_json_file
from types import SimpleNamespace

# Load the list of people using the reusable function
people = load_json_file('../../data/raw/people.json')

# Load the configuration data using the reusable function
config_data = load_json_file('../../config/config.json')

# Parametrise JSON keys and variables using SimpleNamespace
cfg = SimpleNamespace(**config_data)

# Declaration of the list to store greetings - Code
greetings = []
"""
Loop through the list of people and check if they are taking the specified course. If they are, add a greeting to the greetings list.
Could be moved as a function into srcs but is so simple
"""
# initating the loop to check if the person is taking the course and if so, add a greeting to the greetings list - Code
for person in people:
    # cfg.course is the target value ('pSciComp')
    # cfg.courses is the key ('courses')
    if cfg.course in person[cfg.courses]:
        # cfg.name is the key ('name')
        greetings.append(f"Hello {person[cfg.name]}\n")

# Write the greetings to a text file
# Code instruct to open the file, what file to open is environment, 'w' is configuration 
with open('data/final/greeting.txt', 'w') as f:
    # Code
    f.writelines(greetings)