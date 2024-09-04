import requests
import xml.etree.ElementTree as ET

def write_to_file( xml_data :str) -> None:
    root = ET.fromstring(xml_data)
    tree = ET.ElementTree(root)
    with open("output.xml", "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)

def fetch_the_data (url :str, format_output: str) -> None:
    headers = {
        "json" : { "Accept" : "application/json" },
        "xml" : { "Accept" : "application/xml" }
    }
    response = requests.get(url, headers=headers[format_output])
    write_to_file(response.text)

def main():
    print("Run the request")
    url = "https://api.nbp.pl/api/exchangerates/tables/A/"
    format_output = "xml"
    fetch_the_data(url,format_output)

if __name__ == "__main__":
    main()