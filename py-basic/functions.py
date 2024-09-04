def add( a: int, b: int) -> int:
    return  a +b

def to_substract (a: int, b: int) -> int:
    return a - b

def to_devide(a: int, b: int) -> int: 
    if b == 0:
        print("Cannot devide by 0")
        return 0
    return a /b



def main():
    a: int = 10
    b: int = 0
    print(add(a,b))
    print(int(to_devide(a,b)))

if __name__ == "__main__":
    main()