from datetime import datetime

def convert_to_iso(date_str):
    input_format = '%d-%b-%Y %H:%M:%S.%f'  # b representa el mes como texto
    
    dt = datetime.strptime(date_str, input_format)
    
    iso_format = dt.isoformat()
    
    return iso_format