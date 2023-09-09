import bs4
import requests


lista_libros = []
contador_libros = 0
url_base = "http://books.toscrape.com/catalogue/page-{}.html"


for i in range(1, 51):
    resultado = requests.get(url_base.format(i))
    sopa = bs4.BeautifulSoup(resultado.text, "html.parser")

    libros = sopa.select(".product_pod")

    for e in libros:

        cuatro_estrellas = e.select(".star-rating.Four")
        cinco_estrellas = e.select(".star-rating.Five")
        if len(cuatro_estrellas) or len(cinco_estrellas) == 1:
            libro = e.select("a")[1]["title"]
            contador_libros += 1
            lista_libros.append(libro)


print(f"En total hay {contador_libros} con cuatro ó más estrellas en toda la página web.\nLos libros son los siguientes:\n")
for i in range(contador_libros):
    print(lista_libros[i])









