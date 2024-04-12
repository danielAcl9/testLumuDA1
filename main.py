from date_converter import convert_to_iso

# Step by step:
# 1. Read the file. -R
# 2. Format.
# 3. Send to endpoint in chunks of 500.
# 4. Use the endpoint response to make the statistics.
# 5. Print the statistics.
# Variables de entorno

def read_data():
    file_path = 'queries'
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def format_data(data):
    
    return_arr = []

    arr = data.split('\n')
    for line in arr:
        if line == '':
            continue
        # -------------------------------------------

        line_list = list(line.split(" ")) 

        # Unir los dos primeros elementos
        primeros_dos = " ".join(line_list[:2])

        # Sobreescribir los dos primeros elementos en la lista original
        line_list[:2] = [primeros_dos]


        # -------------------------------------------
        #Crear el diccionario para enviar al endpoint
        # my_object = {
        #     "timestamp": convert_to_iso(line[:23]), #Funciona
        #     "name": "www.example.com",
        #     "client_ip": "192.168.0.103",
        #     "client_name": "MACHINE-0987",
        #     "type": "A"
        # }
        #return_arr.append(my_object)
    return line_list

if __name__ == '__main__':
    data = read_data()
    # data = '7-Jul-2022 16:34:13.003 queries: info: client @0x55adcc672cc0 45.231.61.2#80 (pizzaseo.com): query: pizzaseo.com IN ANY +E(0) (172.20.101.44)'
    # timestamp = convert_to_iso(data[:23])
    formatted_data = format_data(data)
    print(formatted_data)