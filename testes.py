# Datos de ejemplo
columna1 = ["Manzanas", "Plátanos", "Naranjas", "Peras"]
columna2 = [10, 8, 15, 12]

# Imprimir en columnas
for item1, item2 in zip(columna1, columna2):
    print("{:<15} {:<5}".format(item1, item2))