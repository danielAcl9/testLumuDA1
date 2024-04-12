import requests
import time

from date_converter import convert_to_iso


# Step by step:
# 1. Read the file. -R
# 2. Format. -R
# 3. Send to endpoint in chunks of 500.
# 4. Use the endpoint response to make the statistics. -R
# 5. Print the statistics. -R

# Function to read the data from the file.
def read_data():
    file_path = 'queries'
    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Function to clean the line_list.
def clean_line_list(line_list):
    # Merge the first two elements (Datetime elements).
    first_two = " ".join(line_list[:2])
    line_list[:2] = [first_two]

    # Erase # in IP addresses
    for i in range(len(line_list)):
        if '#' in line_list[i]:
            line_list[i] = line_list[i].split('#')[0]

    return line_list

# Function to format the data to send to the endpoint.
def format_data(data):
    return_arr = []
    arr = data.split('\n')

    for line in arr:
        if line == '':
            continue

        line_list = list(line.split(" ")) 
        line_list = clean_line_list(line_list)

        # Create dictionary to append to the return_arr, the one that will be sent to the endpoint.
        my_object = {
             "timestamp": convert_to_iso(line_list[0]), # Pos = 0
             "name": line_list[8], # Pos = 8
             "client_ip": line_list[5], # Pos = 5
             "client_name": line_list[8], # Pos = 8
             "type": line_list[10] # Pos = 10
        }
        return_arr.append(my_object)
    return return_arr

# Function to print the statistics of the data.
def print_statistics(data, formatted_data_size):
    print("\nTotal records: ", formatted_data_size)
    print("\nClient IPs Rank")

    # Creates a dictionary with the frequency of each client_ip, counts the number of times each client_ip appears and stores it in the dictionary.
    frec_client_ip = {}
    for obj in data:
        client_ip = obj['client_ip']
        frec_client_ip[client_ip] = frec_client_ip.get(client_ip, 0) + 1

    # Sorts the dictionary by frequency from highest to lowest.
    frecuencia_client_ip_ordenada = sorted(frec_client_ip.items(), key=lambda x: x[1], reverse=True)

    # Prints the top 5 values, their frequencies and the percentage of the total in columns.
    print("-" * 40)
    for client_ip, frecuencia in frecuencia_client_ip_ordenada[:5]:
        print("{:<20} {:<10} {:<4.2f}%".format(client_ip, frecuencia, (frecuencia / formatted_data_size * 100)))
    print("-" * 40)

    print("\nHost Rank")
    print("-" * 70)

    # Creates a dictionary with the frequency of each client name, counts the number of times each client name appears and stores it in the dictionary.
    frec_name = {} 
    for obj in data:
        name = obj['name']
        frec_name[name] = frec_name.get(name, 0) + 1

    # Sorts the dictionary by frequency from highest to lowest.
    frecuencia_name_ordenada = sorted(frec_name.items(), key=lambda x: x[1], reverse=True)

    # Prints the top 5 values, their frequencies and the percentage of the total in columns.
    for name, frecuencia in frecuencia_name_ordenada[:5]:
        print("{:<50} {:<10} {:<4.2f}%".format(name, frecuencia, (frecuencia / formatted_data_size * 100)))
    print("-" * 70)


# Main function
if __name__ == '__main__':

    # Obtaining the data
    data = read_data()
    formatted_data = format_data(data)
    formatted_data_size = len(formatted_data)

    # Make a POST request to the endpoint
    # url = 'https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80'
    # response = requests.post(url, json=formatted_data)

    # Print the statistics
    print_statistics(formatted_data, formatted_data_size)
    
    chunk_size = 500

    # Iterates over the data in chunks of 500.
    count = 0
    for i in range(0, len(formatted_data), chunk_size):
        chunk = formatted_data[i:i+chunk_size] 
        current_data = min(i+chunk_size, formatted_data_size)
        
        # Sending data by chunks of 500 to the endpoint.
        url = 'https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80'
        response = requests.post(url, json=chunk)
        print(f'Sending chunk: {count+1} - {current_data}/{formatted_data_size} - Server Response: {response.status_code}')
        count += 1
        
        time.sleep(1)
