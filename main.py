import requests
import time

from dotenv import load_dotenv
from os import environ

from utils import format_data, print_statistics, read_data

# Main function
if __name__ == '__main__':
    # Load the environment variables
    load_dotenv()
    lumu_client_key = environ.get('LUMU_CLIENT_KEY')
    collector_id = environ.get('COLLECTOR_ID')

    if lumu_client_key is None or collector_id is None:
        raise ValueError('Please provide the LUMU_CLIENT_KEY and COLLECTOR_ID environment variables.')

    # Obtaining the data
    file_path = 'queries'
    data = read_data(file_path)
    
    formatted_data = format_data(data)
    formatted_data_size = len(formatted_data)
    
    chunk_size = 500
    # Iterates over the data in chunks of 500.
    count = 0
    for i in range(0, len(formatted_data), chunk_size):
        chunk = formatted_data[i:i+chunk_size] 
        current_data = min(i+chunk_size, formatted_data_size)
        
        # Sending data by chunks of 500 to the endpoint.
        url = f'https://api.lumu.io/collectors/{collector_id}/dns/queries?key={lumu_client_key}'
        response = requests.post(url, json=chunk)
        print(f'Sending chunk: {count+1} - {current_data}/{formatted_data_size} - Server Response: {response.status_code}')
        count += 1
        
        time.sleep(0.2)

    # Print the statistics
    print_statistics(formatted_data, formatted_data_size)