from datetime import datetime

def convert_to_iso(date_str: str) -> str:
    """
    Converts a date string to ISOformat.

    Parameters
    -----------
    date_str : str
        The date of the query in the format 'dd-MMM-YYYY HH:MM:SS.SSS'

    Returns
    -----------
    str
        The formated query date content in ISOformat.
    """

    input_format = '%d-%b-%Y %H:%M:%S.%f'  # b representa el mes como texto
    
    dt = datetime.strptime(date_str, input_format)
    
    iso_format = dt.isoformat()
    
    return iso_format

# Function to read the data from the file.
def read_data(file_path: str) -> str:
    """
    Reads the data from the file.

    Parameters
    -----------
    file_path : str
        The path to the file.

    Returns
    -----------
    str
        The content of the file.
    """
    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Function to clean the line_list.
def clean_line_list(line_list: list) -> list:
    """
    Cleans the list recieved into specific parameters.
        - Merges the first two elements (Datetime elements).
        - Erases # in IP addresses.

    Parameters
    -----------
    line_list : list
        The list of the current line in the data array.

    Returns
    -----------
    list
        The cleaned list.
    """
    # Merge the first two elements (Datetime elements).
    first_two = " ".join(line_list[:2])
    line_list[:2] = [first_two]

    # Erase # in IP addresses
    for i in range(len(line_list)):
        if '#' in line_list[i]:
            line_list[i] = line_list[i].split('#')[0]

    return line_list

# Function to format the data to send to the endpoint.
def format_data(data: str) -> list:
    """
    Formats the data from a string to a list to send to the endpoint.

    Parameters
    -----------
    data : str
        The content of the file.

    Returns
    -----------
    list
        The formatted data.
    """
    return_list = []
    data_list = data.split('\n')

    for line in data_list:
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
        return_list.append(my_object)
    return return_list

# Function to print the statistics of the data.
def print_statistics(data: list, formatted_data_size: int) -> None:
    """
    Prints the statistics of the data.

    Parameters
    -----------
    data : list
        The formatted data.
        
    formatted_data_size : int
        The size of the formatted data.
    """
    print("\n--- Data Summary & Statistics ---")
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