#rading all file
path = "file/output.xml"
pathin = "file/inutput.xml"
with open(path, 'r') as fileread:
    content = fileread.read()
print(content)

#reading file line by line
with open(path, 'r') as fileread_l:
    count = 0
    for line in fileread_l:
        count +=1
        print(line)
print(count)

#Reading file into the list
with open(path, 'r') as filelist:
    content=filelist.readlines()
print(f"{content}")
for v in content:
    print(f"Booooom -> {v}")

#writing to file
with open(pathin, 'w') as filewrite:
    filewrite.write("Add some texts\n")

#append to file
with open(pathin, 'a') as filea:
    filea.write("Some contexts\n")

#odpczytanie z pliku do tabeli zmaina na text oraz zapsanie do pliku
pathex = "file/ex1.txt"
with open(pathex, 'r' ) as filesource:
    contentex = filesource.readlines()

print(contentex)
contentexjoin = ",".join(contentex)
print(contentexjoin)
