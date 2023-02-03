import face_recognition as fr
from cv2 import cv2

# Cargar imagenes
foto_control = fr.load_image_file("fotoA.jpg")
foto_prueba = fr.load_image_file("fotoB.jpg")
foto_Brad = fr.load_image_file("fotoC.jpg")

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)
foto_Brad = cv2.cvtColor(foto_Brad, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_control = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar cara Brad Pitt
lugar_cara_brad = fr.face_locations(foto_Brad)[0]
cara_codificada_Brad = fr.face_encodings(foto_Brad)[0]


# Localizar cara prueba
lugar_cara_prueba = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Mostar rectangulo de la cara obtenida en localizar cara
cv2.rectangle(foto_control,
              (lugar_cara_control[3],lugar_cara_control[0]),
              (lugar_cara_control[1], lugar_cara_control[2]),
              (0, 255, 0),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_prueba[3], lugar_cara_prueba[0]),
              (lugar_cara_prueba[1], lugar_cara_prueba[2]),
              (0, 255, 0),
              2)


# Realizar comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)
profe_brad = fr.compare_faces([cara_codificada_A, cara_codificada_Brad], cara_codificada_B,
                              tolerance= 0.9) # Se utiliza tolerance para cambiar el margen al comparar dos caras.
print(resultado)
print(profe_brad)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
print(distancia)

# Mostrar resultados
cv2.putText(foto_prueba,
            f"{resultado} {distancia.round(2)}",
            (50, 50),
            cv2.FONT_ITALIC,
            1,
            (0, 255, 0),
            2)

# Mostar imagenes
cv2.imshow("foto_control", foto_control)
cv2.imshow("Foto_prueba", foto_prueba)

# Mantener el programa abiero
cv2.waitKey()


