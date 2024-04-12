import requests
from date_converter import convert_to_iso

# Step by step:
# 1. Read the file. -R
# 2. Format. -R
# 3. Send to endpoint in chunks of 500.
# 4. Use the endpoint response to make the statistics.
# 5. Print the statistics.
# Variables de entorno

def read_data():
    file_path = 'queries'
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def clean_line_list(line_list):
    
    # Merge the first two elements (Datetime elements)
    first_two = " ".join(line_list[:2])
    line_list[:2] = [first_two]

    for i in range(len(line_list)):
        if '#' in line_list[i]:
            line_list[i] = line_list[i].split('#')[0]

    return line_list


def format_data(data):
    
    return_arr = []

    arr = data.split('\n')
    for line in arr:
        if line == '':
            continue

        line_list = list(line.split(" ")) 
        line_list = clean_line_list(line_list)

        #Crear el diccionario para enviar al endpoint
        my_object = {
             "timestamp": convert_to_iso(line_list[0]), # Pos = 0
             "name": line_list[8], # Pos = 8
             "client_ip": line_list[5], # Pos = 5
            #  "client_name": line_list[8], # Pos = 8
            #  "type": line_list[10] # Pos = 10
        }
        return_arr.append(my_object)
    return return_arr

if __name__ == '__main__':

    # Obtaining the data
    data = read_data()
    formatted_data = format_data(data)

    # print(formatted_data)

    # Make a POST request to the endpoint

    url = 'https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80'

    x = requests.post(url, json=formatted_data)

    print(x)