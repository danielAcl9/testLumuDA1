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

        # -------------------------------------------
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

if __name__ == '__main__':
    data = read_data()
    # data = '7-Jul-2022 16:34:13.003 queries: info: client @0x55adcc672cc0 45.231.61.2#80 (pizzaseo.com): query: pizzaseo.com IN ANY +E(0) (172.20.101.44)'
    # timestamp = convert_to_iso(data[:23])
    formatted_data = format_data(data)
    print(formatted_data[0])