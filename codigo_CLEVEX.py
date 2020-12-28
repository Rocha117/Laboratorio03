
import random
class Banco:
    def __init__(self):
        self.usuarios = []

    def agregar_cliente(self):
        nombre = input("\nDigite el nombre del usuario: ")
        apellido = input("Digite el apellido del usuario: ")
        dni = int(input("Digite el DNI del usuario: "))

        if self.buscar_por_dni(dni):
            print("Ya existe un usuario con el mismo dni")
        else:
            self.usuarios.append(Cuenta_bancaria(nombre, apellido, dni))

    def buscar_por_dni(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario

    def mostrar_cliente(self, dni):
        cliente = self.buscar_por_dni(dni)
        if cliente:
            print("\n", cliente)
        else:
            print("\nNo existe un cliente con ese dni")

class Cuenta_bancaria:
  def __init__(self, nombre, apellido, dni):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.num_unic = []

  def crear_cuenta(self):
    self.num_unic = random.randint(1000000000000, 9999999999999)
    print(f"su numero de cuenta es: {self.num_unic}")

  def __str__(self):
    self.crear_cuenta()
    return(f"\nNombre: {self.nombre}\n"
           f"Apellido: {self.apellido}\n"
           f"DNI: {self.dni}\n"
           f"Numero de cuenta: {self.num_unic}"
           )

i=0
def main():
    banco = Banco()
    while i==0:

        print("===============================================================================")
        print("                 BIENVENIDO A LA DE RED DE CAJEROS AUTOMATICOS                 \n\n                                   BANCO BCP")
        print("===============================================================================")
        print("1. Registrarse      2. Consultar datos de usuario       3. Ingresar Nº de cuenta")
        opcion_0=int(input("Opcion: "))
        if opcion_0==1:
            print()
            banco.agregar_cliente()
        elif opcion_0==2:
            print("Ingrese su Nº de DNI")
            dni=int(input("DNI: "))
            banco.mostrar_cliente(dni)

#-------------------------------------------------------------------
    #while True:
        #try:
            #print("\nDigite una opcion: \n\n"
                  #"  1) Agregar usuario\n"
                  #"  2) Buscar usuario\n"
                  #)

            #opcion = input("\nDigite una opcion: ")

            #if opcion == "1":
                #banco.agregar_cliente()

            #elif opcion == "2":
                #dni = int(input("Digite el dni del usuario que desea buscar: "))
                #banco.mostrar_cliente(dni)

        #except ValueError:
            #print("\nOpción incorrecta, intentelo nuevamente")
#-------------------------------------------------------------------

if __name__=='__main__':
    main()