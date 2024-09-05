import random
#Dodanie dwh liczb 
num1=random.randint(1,60)
num2=random.randint(5,50)
print(f"sum {num1+num2} of num1={ num1} and num2={num2}")
#policzenie slow w zdaniu
sentance = "Ala ma kota a kot ma ale"
print(sentance.count(' ')+1)

#policzenie ilości dużych liter w zdaniu
sentanceStr :str = "Ala ma kota Ktory posZeld" 
upperl=0
lowerl=0
for w in  sentanceStr:
    if w.isupper():
        upperl+=1
    elif w.islower():
        lowerl+=1
print(f"uper {upperl} and lower {lowerl}")

#Zmianna wszyskit liter na duże
sentance = "Ala ma kota a kot ma ale"
print(sentance.upper())

#Zamian malych liter na duże i dużych na małe
sentance = "Ala ma kota a Kot ma ale"
print(sentance.swapcase())

#Zmianna  a na e
sentance = "Ala ma kota a kot ma ale"
print(sentance.replace('a', 'e'))
#Sortowanie slów
sentance = "Ala ma kota a kot ma ale"

#odwrócenie zdania
sentanceTest = "Ala ma kota a kot ma ale"

#zawieranie stringu w zdaniu
sentanceTest = "Ala ma kota a kot ma ale"
word = "Ala"

#Print separate words from sentace

sentanceTest = "Ala ma kota a kot ma ale"
words = sentanceTest.split(" ")


#longes word in sentence
sentanceTest = "Ala ma kota a kot ma aleasdsad"


#reverse of words in sentence
splittowords2 = sentanceTest.split(" ")

#wyswietlenie tablicy odraz indexów
# Use the enumerate() function to list elements with their indices

#wylistowanie owoców od którejś zaczynajac indexowanie 2
fruits = ["apple", "orange", "ananas"]

#dane struktury
carsdict = {
    "Renault":["Megane", "Koleos", "Espase"],
    "BMW":["X3","X2","X1"],
    "Mercedes":["A Class","B Class","C Class"]
}
#wylistować strukturę

#join function
cities = ["Amsterdam", "Tokyo", "Rio de Janeiro", "Los Angeles"]

#print len of array

#print len of word

#String end with some str .endswith()
emails = ['john.doe@gmail.com', 'mark.twain@company.com', 'mrwonderful@outlook.com']
postfix = "company.com"

#String end with some str .endswith()
postfix = "star"
packages = ["com.package.main", "com.package.car", "eu.package.star"] 
