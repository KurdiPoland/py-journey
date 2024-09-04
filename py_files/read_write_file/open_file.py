
from typing import List
#rading all file
path = "file/output.xml"
with open(path, 'r') as file:
    content = file.read()

print(content)

#reading file line by line
with open(path, 'r') as file: # r mode automaticaly close the the file
    count=0
    for line in file:
        count+=1
        line=line.replace(' ','')
        print(f"{ count } Line -> {line} -> { type(count)} -> {len(line)}")
print("\n")
#Reading file into the list
with open(path, 'r') as filexml:
    lines = filexml.readlines()

print(f"{lines} are length { len(lines) }")

#writing to file
pathtowrite="file/double_file.xml"
with open(pathtowrite, 'w') as filetowrite: #mode to write if file will not be exsisted it will be created, but if it's existed, will be overwrite
    filetowrite.write("Add some texts\n")
    filetowrite.write("Add some other texts\n")

print(f"The written successfully")

with open(pathtowrite, 'a') as filetoappend: #append mode can be use to append information to file without overwite
    filetoappend.write("Append line")

# #binary read 
# image_path="some.jpg"
# jpg_out=""
# with open(path, 'rb') as binfile: #read binary data and write to variable
#     binary_data = binfile.read()

# print(type(binary_data))

# with open(jpg_out, 'wb') as binfile: #write binnary data from variable to file
#     binfile.write(binary_data) 

# print(f"Binary file written successfully ")