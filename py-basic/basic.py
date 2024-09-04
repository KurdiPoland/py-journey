#simple priint statement
somestr = " Hello, World! "
print(somestr)
print(somestr[2:5])
print(somestr[2:]) #prints from 2nd index to end
print(somestr * 2) #prints string twice
print(somestr + "TEST") #concatenates string
print(somestr.strip()) #removes leading and trailing whitespaces
print(type(somestr))

for x in somestr:
    print(x)


#Conditions
#if else
a = 10
b = 5

if a < b :
    print("Max=", b)
else:
    print("Max=", a)

#elseif
c = 5
d = 5   
if c > d:
    print("Max", c)
elif c==d:
    print("Equal", d) 
else: 
    print("Max", c) 

#Arrrays in python
cars = ["Ford", "Volvo", "BMW"]

for v in cars:
    print(v)

#loops
count=5
i=0
while i < count:
    i += 1
    print(i) 

#for loops
carsdict = {
    "Renault":["Megane", "Koleos", "Espase"],
    "BMW":["X3","X2","X1"],
    "Mercedes":["A Class","B Class","C Class"]
}

for i in carsdict:
    for v in carsdict:
        print(i,v)

#split the string
for i in "banana":
    print(i)

#for loop using range
for x in range(2,10,2):
    print(x)

language="python"
match language:
    case "python":
        print("you choose python")
    case "java":
        print("you choose java")
    case "golang":
        print("you choose golang")
    case default:
        print("No choose lang")