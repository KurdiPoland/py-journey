from typing import Dict, List
def add( a: int, b: int) -> int:
    return  a +b

def to_substract (a: int, b: int) -> int:
    return a - b

def to_devide(a: int, b: int) -> int: 
    if b == 0:
        print("Cannot devide by 0")
        return 0
    return a /b

def get_car_list( cars: Dict[str, List[str]] ) -> None:
    for x in cars:
        for v in cars[x]:
         print (f"Brand {x} -> model {v}")

def get_fruits( fruit: List[str]) -> None:
    for x in fruit:
        print(x)

def getfuits_with_index( fruit: List[str]) -> None:
    for index in range(len(fruit)):
        print(f"Index: {index} Value: { fruit[index] }")

def getfuits_with_index_enumerate(fruit: List[int]):
    for index, value in enumerate(fruit):
        print(f"Index enumerate {index}, value {value}")

def matchex (lang: str) -> int:
    match lang:
        case "python":
            return 1
        case "golang":
            return 2
        case "java":
            return 3
        case default:
            return 0

def main():
    a: int = 10
    b: int = 0
    print(add(a,b))
    print(int(to_devide(a,b)))

    carsdict = {
        "Renault":["Megane", "Koleos", "Espase"],
        "BMW":["X3","X2","X1"],
        "Mercedes":["A Class","B Class","C Class"]
    }
    get_car_list(carsdict)

    fruitslist = ["apple", "ananas", "banana"]
    get_fruits(fruitslist)
    getfuits_with_index(fruitslist)
    getfuits_with_index_enumerate(fruitslist)

    setnence_texts = "Samochody jezdza po ulicy"
    setnence_texts = setnence_texts.split(' ')
    for s in enumerate(setnence_texts):
        print(s)

    language="golang"
    print(matchex(language))

if __name__ == "__main__":
    main()

