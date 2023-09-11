import random
from random import randint
from typing import List

lista_clientes = []

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return \
            (
                f"{self.nombre} {self.apellido}, con numero de cuenta ({self.numero_cuenta}), su balance es de: {self.balance}€")

    def depositar(self):
        numero = float(input(f"¿Cúanto dinero quieres depositar de tu cuenta?\n"
                             f"Balance actual: {self.balance}\n"))
        deposito = self.balance + numero
        return deposito

    def retirar(self):
        numero = float(input(f"¿Cúanto dinero quieres retirar de tu cuenta?\n"
                             f"Balance actual: {self.balance}\n"))

        while numero > self.balance:
            print("No puedes retirar una cantidad superior a la que tienes disponible.")
            numero = float(input(f"¿Cúanto dinero quieres retirar de tu cuenta?\n"
                                 f"Balance actual: {self.balance}\n"))

        retiro = self.balance - numero
        return retiro



nombre = input("¿Cúal es tu nombre\n")
apellido = input(("Cual es tu apellido?"))
numero_cuenta = random.randint(100000000, 999999999)
balance = float(input("\n¿De cuanto va a ser su primer depósito?\n"))




insertar = int(input("[1] - Ver balance actual\n"
                    "[2] - Hacer un deposito\n"
                        "[3] - Hacer un retiro\n"
                        "[4] - Salir\n\n"))
while insertar < 4:
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    if insertar == 1:
        print(cliente.balance)
    elif insertar == 2:
        balance = cliente.depositar()
        print(balance)
    elif insertar == 3:
        balance = cliente.retirar()
        print(balance)
    else:
        break
    insertar = int(input("[1] - Ver balance actual\n"
                             "[2] - Hacer un deposito\n"
                             "[3] - Hacer un retiro\n"
                             "[4] - Salir\n\n"))

