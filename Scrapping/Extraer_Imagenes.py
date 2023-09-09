import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/courses")

sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

imagenes = sopa.select(".course-box-image")


url_imagen = imagenes[0]["src"]
descargar_imagen = requests.get(url_imagen)

f = open("mi_imagen.jpg", "wb")
f.write(descargar_imagen.content)
f.close()
