import os
current_path = os.getcwd()
filePath = current_path + "\\javascript\\pokemon-api\\package.json"
with open(filePath) as file:
    for line in file:
        print(line.rstrip())  # Remove extra newline characters