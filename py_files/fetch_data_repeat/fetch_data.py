import requests
import json

def write_to_f( content: str) -> None:
    with open("testfile.txt", 'w') as file:
        file.write(content)

def get_currencies ( nameurl: str) -> None:
    headers = {
        "json" : { "Accept" : "application/json" },
        "xml" : { "Accept" : "application/xml" }
    }
    response = requests.get(nameurl, headers=headers["json"])
    write_to_f(response.text)
    print(type(response.text))
    
def write_to_json_file(json_data: list) -> None:
    with open("json_file.json", 'w') as jsonf:
        json.dump(json_data, jsonf, indent=4)

def get_currencies_json(url: str) -> None:
    headers = {
        "json" : { "Accept" : "application/json" },
        "xml" : { "Accept" : "application/xml" }
    }
    response = requests.get(url, headers=headers["json"])
    json_data = response.json()
    print(type(response.json()))
    write_to_json_file(json_data)

def main():
    print("Run the request")
    url = "https://api.nbp.pl/api/exchangerates/tables/A/"
    get_currencies(url)
    get_currencies_json(url)


if __name__ == "__main__":
    main()