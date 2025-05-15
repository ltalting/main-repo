import os
current_path = os.getcwd()
filePath = current_path + "\\data.lnk\\pokemon-info-ht-wt.json"
with open(filePath) as file:
    for line in file:
        print(line.rstrip())  # Remove extra newline characters