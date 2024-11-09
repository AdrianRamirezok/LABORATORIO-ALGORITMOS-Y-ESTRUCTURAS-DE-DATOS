class persona():
   def __init__(self,nombre,apellido):
      self.nombre=nombre
      self.apellido=apellido

class cliente(persona):
   def __init__(self,numero_cuenta,balance):
      self.numero_cuenta= numero_cuenta
      self.balance=balance
   def __str__(self):
      return (f"cliente: {self.nombre} {self.apellido} numero de cuenta:{self.numero_cuenta} balance: {self.balance}")
   def Depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Has depositado ${monto}. Nuevo balance: ${self.balance}")
   
   def Retirar(self, monto):
        if monto > 0 and monto <= self.balance:
            self.balance -= monto
            print(f"Has retirado ${monto}. Nuevo balance: ${self.balance}")
        else:
            print("No tienes suficiente saldo para realizar el retiro.")

def crear_cliente():
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    num_cuenta=input("Ingrese su numero de cuenta: ")
    balance=input("Ingrese el monto que desea ingresar en su nueva cuenta: ")
    cliente1=(nombre,apellido,num_cuenta,balance)
    return cliente1

def menu():
      cliente=crear_cliente()
      while True:
        print("\n¿Qué deseas hacer?")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Ver balance")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")
        
        if opcion == "1":
           
            monto = float(input("¿Cuánto dinero deseas depositar? $"))
            cliente.Depositar(monto)
        
        elif opcion == "2":
           
            monto = float(input("¿Cuánto dinero deseas retirar? $"))
            cliente.Retirar(monto)
        
        elif opcion == "3":
           
            print(cliente)  
        
        elif opcion == "4":
            print("¡Gracias por usar nuestro sistema! Adiós.")
            break
        
        else:
            print("Opción no válida. Por favor selecciona una opción correcta.")
menu()
      
