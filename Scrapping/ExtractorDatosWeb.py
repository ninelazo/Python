import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2022/11/trucos-de-formato-de-cadenas-en-python.html")

sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

#Obtenemos el titulo del articulo
titulo = sopa.select("title")
print(f"Titulo: {titulo[0].getText()}")

#Obtenemos todos los parrafos que aparece en la pagina web
parrafo = sopa.select("p")
longitud_parrafos = len(parrafo)

for i in range(longitud_parrafos):
    print(f"Parrafo {i}: {parrafo[i].getText()}")

barra_lateral = sopa.select(".snippet-item")
long_barra = len(barra_lateral)

for i in range(long_barra):
    print(barra_lateral[i].getText())



