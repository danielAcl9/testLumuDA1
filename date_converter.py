from datetime import datetime

def convert_to_iso(date_str):
    input_format = '%d-%b-%Y %H:%M:%S.%f'  # b representa el mes como texto
    
    dt = datetime.strptime(date_str, input_format)
    
    iso_format = dt.isoformat()
    
    return iso_format

date_str = "7-Jul-2022 16:34:13.003"
iso_date = convert_to_iso(date_str)
print("Fecha y hora en formato ISO:", iso_date)

