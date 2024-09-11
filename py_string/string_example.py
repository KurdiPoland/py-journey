import random
#czy literna znajduje się w słowie
voles = ['a', 'b', 'c', 'd', 'i', 'o', 'u']
word = "Milliard"

for letter in voles:
    if letter in word:
        print(f"The letter {letter} is in word {word}")

#dodaj do tablicy
found=[]
for i in range(2,20,2):
    print(i)
    found.append(random.randint(1,60))
print(found)

#czy obiejst jest czy nie
voles = ['a', 'b', 'c', 'd', 'i', 'o', 'u']
word = "Milliard"

for letter in word:
    if letter not in voles:
        print(f"{letter} is not in {voles}")
        voles.append(letter)
print(voles)

#opracje na tablicy
volesexam = ['a', 'b', 'c', 'd', 'i', 'o', 'u']

print(volesexam)
volesexam.pop()
print(volesexam)
volesexam.extend(['z','i'])
print(volesexam)
volesexam.insert(5,'a')
print(volesexam)