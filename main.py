import requests
import time

from utils import format_data, print_statistics, read_data

# Main function
if __name__ == '__main__':

    # Obtaining the data
    file_path = 'queries'
    data = read_data(file_path)
    
    formatted_data = format_data(data)
    formatted_data_size = len(formatted_data)

    # Make a POST request to the endpoint
    # url = 'https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80'
    # response = requests.post(url, json=formatted_data)
    
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
        
        time.sleep(0.2)

    # Print the statistics
    print_statistics(formatted_data, formatted_data_size)