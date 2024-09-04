import os
def create_file (namef: str) -> None:
    with open(namef, 'w') as file:
        file.write("Some content to file")
    print(f"File {namef} created")

def renamefile (names: str, namet: str) -> None:
    try:
        os.rename(names, namet)
    except FileNotFoundError:
        print(f"Nie ma takiego pliku")

def deletefile (namef: str) -> None:
    try:
        os.remove(namef)
        print(f"File {namef} removed")
    except FileNotFoundError:
        print(f"File {namef} not found")

def main(): 
    filename = "files/content_file.txt"
    create_file(filename)

    sourcefile = "content_file.txt"
    targetfile = "targetfile.txt"
    renamefile(sourcefile,targetfile)
    deletefile(targetfile)

if __name__ == "__main__":
    main()