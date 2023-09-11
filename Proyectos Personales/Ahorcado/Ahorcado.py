import random


def elegir_palabra():
    palabras = ["hola", "caballo", "melon", "cerdo", "columpio", "aguacate"]

    palabra_elegida = random.choice(palabras)

    print(f"La palabra elegida es: ")

    for n in palabra_elegida:
        print("_", end=" ")

    return palabra_elegida


def lista_palabra(palabra):
    lista = []

    for letra in palabra:
        lista.append("_")

    return lista


def elegir_letra():
        letra = input("Introduzca una letra: ")
        while len(letra)>1:
            print("Eres mu tonto")
            letra = input("Introduzca una letra: ")
        else:
            return letra


def letra_correcta(letra, palabra):
    if letra in palabra:
        return True
    else:
        return False


def jugar():
    palabra_seleccionada = elegir_palabra()
    lista_palabra_seleccionada = list(palabra_seleccionada)
    lista_nueva = lista_palabra(lista_palabra_seleccionada)
    print("\n")
    letras_erroneas = []

    vidas = 6
    while vidas >= 1 and lista_nueva != lista_palabra_seleccionada:
        letra = elegir_letra()
        verificar_letra = letra_correcta(letra, palabra_seleccionada)

        if not verificar_letra:

            vidas = vidas - 1
            print(f"La letra {letra.upper()} no se encuentra en la palabra, te quedan {vidas} intentos")
            print(" ".join(lista_nueva))
            letras_erroneas.append(letra)
            print((", ".join(letras_erroneas)).upper())

        else:
            contador = 0
            while contador < len(lista_palabra_seleccionada):
                if letra == lista_palabra_seleccionada[contador]:
                    lista_nueva.pop(contador)
                    lista_nueva.insert(contador, letra)
                    print(f"La letra se encuentra en la posicion: {contador + 1}")
                    contador += 1
                else:
                    contador += 1
            print(" ".join(lista_nueva))

    if vidas > 0:

        print(f"\nHas ganado!!! la palabra es {palabra_seleccionada.upper()}")
    else:
        print(f"Has perdido... Te has quedado sin intentos. La palabra correcta era {palabra_seleccionada.upper()}")
    return


jugar()
