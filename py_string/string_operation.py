#Dodanie dwóch liczb 
# num1 = int(input("Enter first number"))
# num2 = int(input("Enter secound number"))
# print("sum of numbers", num1+num2)

#policzenie slow w zdaniu
# sentence = input("Input sentance")
# print("Sentenace have the words", sentence.count(' ')+1)

#policzenie ilości dużych liter w zdaniu
sentanceStr :str = "Ala ma kota Ktory poszeld" 
upper=0
lower=0
for x in sentanceStr:
    print(x)
    if x.isupper():
        upper+=1
    elif x.islower():
        lower+=1
    else :
        print("Some other later", x)

print("Upper ", upper , "lower", lower)

#Zmianna wszyskit liter na duże
sentance = "Ala ma kota a kot ma ale"
print(sentance.upper())

#Zmianna  a na e
sentance = "Ala ma kota a kot ma ale"
print(sentance.replace('a','e'))

#Sortowanie slów
sentance = "Ala ma kota a kot ma ale"
print(sorted(sentance.replace(' ','').lower()))

#odwrócenie zdania
sentanceTest = "Ala ma kota a kot ma ale"
print(sentanceTest[::-1].replace(' ',''))

#zawieranie stringu w zdaniu
sentanceTest = "Ala ma kota a kot ma ale"
word = "Ala"

if word in sentanceTest:
    print("the ", word, "is in santance",sentanceTest )

#Print only a words from sentace

sentanceTest = "Ala ma kota a kot ma ale"
words = sentanceTest.split(" ")

for w in words:
    print(w)

#longes word in sentence
sentanceTest = "Ala ma kota a kot ma aleasdsad"
splittowords = sentanceTest.split(" ")
print(max(splittowords, key=len))

#reverse of words in sentence
splittowords2 = sentanceTest.split(" ")
reversesplit = splittowords2[::-1]  #zmienia kolejność ale bez zmiany oryginału
print(" ".join(reversesplit))
print(splittowords2.reverse()) #reverse funkcja zmienia ogryginalną listę
print(splittowords2)

#wyswietlenie tablicy odraz indexów
# Use the enumerate() function to list elements with their indices
for i, v in enumerate(splittowords2):
    print("index", i , "wartosc" , v)

#wylistowanie owoców od którejś zaczynajac indexowanie 2
fruits = ["apple", "orange", "ananas"]

for i, v in enumerate(fruits, start = 2):
    print(f"Index: {i}, Value {v}")

#dane struktury
carsdict = {
    "Renault":["Megane", "Koleos", "Espase"],
    "BMW":["X3","X2","X1"],
    "Mercedes":["A Class","B Class","C Class"]
}

for x in carsdict:
    print(f"Brand {x}")
    for v in carsdict[x]:
        print(f"Model {v}")

#join function
cities = ["Amsterdam", "Tokyo", "Rio de Janeiro", "Los Angeles"]
allcities = ",".join(cities)
print(f"All cities {allcities}")

#print len of array
print(len(cities))

#print len of word
print(len(allcities))
#String end with some str .endswith()
emails = ['john.doe@gmail.com', 'mark.twain@company.com', 'mrwonderful@outlook.com']
postfix = "company.com"
for x in emails:
    print(x)
    if x.endswith("company.com"):
        print(f"the {x} should be blocked")
    else:
        print(f"the {x} allow")
prefix = "com"
postfix = "star"
packages = ["com.package.main", "com.package.car", "eu.package.star"] 
for x in packages:
    if x.startswith(prefix):
        print(f"the { x } String starts with { prefix }")
    elif x.endswith(postfix):
        print(f"the { x } String starts with { postfix }")
    else:
        print(f"the {x} No patterns found")