#rading all file
locationfile = "file/output.xml"
with open(locationfile, 'r') as fileread:
    content = fileread.read()
print(content)

#reading file line by line
with open(locationfile, 'r') as filereadline:
    count=0
    for line in filereadline:
        count+=1
        print(line)
print(f"Line in files {count}")

#Reading file into the list
with open(locationfile, 'r') as fileasarr:
    contentlist = fileasarr.readlines()
print(contentlist)

#writing to file
targetfile = "file/targetfile.xml"
contentarray = ','.join(contentlist)
contentarray = contentarray.replace(",","")
with open(targetfile, 'w' ) as filetowrite:
    filetowrite.write(contentarray)
