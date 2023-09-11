import os
from pathlib import Path
import re
import datetime
import time
import math





fecha_actual = datetime.date.today()

print(f"Fecha de búsqueda: {fecha_actual}")

encabezado = (f"ARVHIVO\t\t\tCLAVE\n"
              f"_______\t\t\t_____\n")
print(encabezado)

inicio = time.time()
contador = 0
ruta = ("C:\\Users\\ninel\\Desktop\\python\\Dia9_Proyecto\\Mi_Gran_Directorio")

for carpeta, subcarpeta, archivo in os.walk(ruta):



    for arc in archivo:
        abrir_archivo = open(Path(ruta,carpeta, arc))
        leer_archivo = abrir_archivo.read()


        formato = (r"N\D{3}-\d{5}")

        buscar_formato = re.search(formato, leer_archivo)

        if buscar_formato:
            print(f"{arc}\t{buscar_formato.group()}")
            contador += 1
        else:
            pass

print(f"\nNúmeros encontrados: {contador}")


fin = time.time()

tiempo_ejec = fin - inicio

print(f"Duración de la busqueda: {math.ceil(tiempo_ejec)}s")


