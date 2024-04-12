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
             "client_name": line_list[8], # Pos = 8
             "type": line_list[10] # Pos = 10
        }
        return_arr.append(my_object)
    return return_arr

def print_statistics(data):
    print("\nTotal records: ", len(data))
    print("\nClient IPs Rank")

    frec_client_ip = {}
    
    for obj in data:
        client_ip = obj['client_ip']
        frec_client_ip[client_ip] = frec_client_ip.get(client_ip, 0) + 1

    # Ordena el diccionario por frecuencia de mayor a menor
    frecuencia_client_ip_ordenada = sorted(frec_client_ip.items(), key=lambda x: x[1], reverse=True)

    # Imprime los 5 principales valores y sus frecuencias en columnas
    print("-" * 40)
    for client_ip, frecuencia in frecuencia_client_ip_ordenada[:5]:
        print("{:<20} {:<10} {:<4.2f}%".format(client_ip, frecuencia, (frecuencia / len(data) * 100)))

    print("-" * 40)

    print("\nHost Rank")
    print("-" * 70)

    frec_name = {}
    
    for obj in data:
        name = obj['name']
        frec_name[name] = frec_name.get(name, 0) + 1

    # Ordena el diccionario por frecuencia de mayor a menor
    frecuencia_name_ordenada = sorted(frec_name.items(), key=lambda x: x[1], reverse=True)

    # Imprime los 5 principales valores y sus frecuencias en columnas
    for name, frecuencia in frecuencia_name_ordenada[:5]:
        print("{:<50} {:<10} {:<4.2f}%".format(name, frecuencia, (frecuencia / len(data) * 100)))

    print("-" * 70)


if __name__ == '__main__':

    # Obtaining the data
    data = read_data()
    formatted_data = format_data(data)


    # Make a POST request to the endpoint
    # url = 'https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80'
    # response = requests.post(url, json=formatted_data)

    # print(formatted_data[:100])


    # Print the statistics
    print_statistics(formatted_data)