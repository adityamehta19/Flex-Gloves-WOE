import requests
import xml.etree.ElementTree as ET
import time

# Send an HTTP GET request

while True:
    B0=[]
    V0=[]
    B1=[]
    V1=[]
    for i in range(100):
        response = requests.get('http://192.168.17.17/xml')

        if response.status_code == 200:
            # Parse the XML data
            xml_data = response.text
            root = ET.fromstring(xml_data)
            
            # Access elements in the XML tree
            for child in root:
                if child.tag == 'B0':
                    B0.append(child.text)
                elif child.tag == 'V0':
                    V0.append(child.text)
                elif child.tag == 'B1':
                    B1.append(child.text)
                elif child.tag == 'V1':
                    V1.append(child.text)
        else:
            print('Request failed with status code', response.status_code)

        time.sleep(1)
    csv = open("data.csv", "w")
    columnTitleRow = "B0, V0, B1, V1\n"
    csv.write(columnTitleRow)
    for i in range(100):
        row = B0[i] + "," + V0[i] + "," + B1[i] + "," + V1[i] + "\n"
        csv.write(row)
    csv.close()
    print("Done")
    time.sleep(3)