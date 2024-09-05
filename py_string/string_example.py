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