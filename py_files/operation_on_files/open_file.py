
from typing import List
#rading all file
path = "file/output.xml"
with open(path, 'r') as file:
    content = file.read()

print(content)

#reading file line by line
with open(path, 'r') as file:
    count=0
    for line in file:
        count+=1
        print(f"{ count } Line -> {line} -> { type(count)}")

a: List[str] = [1,2,4]
print(a)

