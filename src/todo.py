import json
import os
from os.path import expanduser
import platform


home = os.path.expanduser('~')
print(home)


folder_name = ".todo"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists:", folder_name)




folder_path = os.path.join(os.path.expanduser("~"), folder_name)
file_path = os.path.join(folder_path, "tasks.json")



# Write the JSON data to the file
data = {"test": "Hi","age":30}
with open(file_path, "w") as f:
    json.dump(data, f)



