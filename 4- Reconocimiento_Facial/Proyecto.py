from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime


# Crear base de datos
ruta = "Empleados"
imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}\\{nombre}")
    imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# Codificar imagenes
def codificar_imagenes(imagen):

    lista_codificada = []

    for foto in imagen:
        foto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)

        codificado = fr.face_encodings(foto)[0]
        lista_codificada.append(codificado)

    return lista_codificada

lista_empleados_codificada = codificar_imagenes(imagenes)

# Registrar ingresos
def ingresos(persona):
    f = open("registro.csv", "r+")
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",")
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        fecha_actual = datetime.now()
        str_hora_actual = fecha_actual.strftime("%H:%M")
        f.writelines(f"\n{persona}, {str_hora_actual}")

# Hacer una foto con Webcam
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la camara
exito, imagen =  captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    cara_captura_cod = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias

    for caracod, caraubic in zip(cara_captura_cod, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracod)
        distancias = fr.face_distance(lista_empleados_codificada, caracod)

        # Mostrar coincidencias
        indice_coincidencia = numpy.argmin(distancias)

        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de los empleados")
        else:
            nombre = nombres_empleados[indice_coincidencia]
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)

            ingresos(nombre)

            # mostrar la imagen obtenida
            cv2.imshow('Imagen webcam', imagen)

            # mantener ventana abierta
            cv2.waitKey(0)


