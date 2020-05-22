from PaymentData import PaymentData
from Bank import Bank 
from Viaje import Viaje

class User:

    def __init__(self, nom, dni, telefon, direccio, email):
        self.nom = nom
        self.dni = dni
        self.telefon = telefon
        self.direccio = direccio
        self.email = email

    def validateInput(self):
        return type(self.nom) == str and type(self.dni) == str and type(self.telefon) == str and type(self.direccio) == str and type(self.email) == str

    def pagament(self, viaje:Viaje,payment_data:PaymentData):
        preu = viaje.precio
        self.dades_pagament = payment_data
        if (Bank.do_payment(self,self.dades_pagament)):
            return True
        else:
            print("Error: Pagament no realitzat correctament")
            return False

        
        

