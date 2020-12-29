import datetime
import time
import random
import copy
x = datetime.datetime.now()


class Tarjeta_bancaria(object):

    def __init__(self, estado_bloq=0):
        self.No_tarjeta = [{}, {CCI: }]
        self.estado_bloq = estado_bloq

    @property
    def estado(self):
        return self.estado_bloq

    @estado.setter
    def estado(self):
        # Si la cuenta está bloqueada, su estado será 1, caso contrario es 0
        self.estado_bloq = 1


class Cuenta_bancaria(object):

    def __init__(self):
        num_cuenta = random.randint(1000000000, 9999999999)
        self.num_unic = int(
            "193"+str(num_cuenta))
        self.cci = int('002'+'193'+'00'+str(num_cuenta) +
                       random.randint(10, 99))

        self.clave = random.randint(1000, 9999)

    @property
    def cambiar_clave(self):
        return self.clave

    @cambiar_clave.setter
    def cambiar_clave(self, new_clave):
        if (len(str(new_clave)) == 4) and (new_clave/1 == new_clave):
            self.clave = new_clave
            print(f"Su nueva clave es: {self.clave}")
        else:
            print("Su clave es incorrecta")
    # print(f"su numero de cuenta es: {self.num_unic}")


class Persona(Tarjeta_bancaria, Cuenta_bancaria):
    """
    Permite asignarle a las personas una cuenta y una tarjeta bancaria
    """

    def __init__(self, nombre, apellido, dni, edad, No_tarjeta=None, estado_bloq=None, num_unic=None, cci=None, clave=None):
        """
        Constructor que nos permite inicializar a una persona
        """
        Tarjeta_bancaria.__init__(No_tarjeta, estado_bloq)
        Cuenta_bancaria.__init__(num_unic, cci, clave)
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._edad = edad

    @property
    def nombre(self):
        """
        Permite editar la propiedad de nombre a la persona
        """
        return self._nombre

    @nombre.setter
    def nombre(self, n):  # Establece un límite de 12 letras para el nombre
        assert (len(n) < 12), "El nombre debe ser menor a 12 letras"
        self._nombre = n

    @property
    def apellido(self):
        """
        Permite editar la propiedad de apellido a la persona
        """
        return self._apellido

    @apellido.setter
    def apellido(self, n):  # Establece un límite de 12 letras para el apellido
        assert (len(n) < 12), "El apellido debe ser menor a 12 letras"
        self._apellido = n

    @property
    def dni(self):
        """
        Permite editar la propiedad de DNI a la persona
        """
        return self._dni

    @dni.setter
    def dni(self, n):  # Establece un límite de 8 dígitos para el DNI
        assert (len(n) == 8), "El número de DNI debe ser de 8 dígitos"
        self._dni = n

    @property
    def edad(self):
        """
        Permite editar la propiedad de edad a la persona
        """
        return self._edad

    @edad.setter
    def edad(self, n):  # Establece un rango para la edad entre 18 y 100 años
        assert (n >= 18 and n <=
                100), "La edad de la persona debe ser entre 18 y 100 años"
        self._edad = n


class Banco:
    usuarios = []
    usuarios_nro_cuenta = []

    def __init__(self, usuarios=[], usuarios_nro_cuenta=[]):
        self.usuarios = usuarios
        self.usuarios_nro_cuenta = usuarios_nro_cuenta

    @property
    def usuar(self):
        return self.usuarios

    @usuar.setter
    def agregar_cliente(self, personita):
        for usuario in self.usuarios:
            if usuario.has_key(personita._dni):
                print("Ya existe un usuario con el mismo dni")

            else:
                self.usuarios.append({personita._dni: [
                                     personita._nombre, personita._edad, personita._dni, personita.num_unic, personita.clave, personita.estado_bloq]})

    @property
    def usuar2(self):
        return self.usuarios_nro_cuenta

    @usuar2.setter
    def agregar_cliente2(self, personita):
        for usuario in self.usuarios_nro_cuenta:
            if usuario.has_key(personita._dni):
                print("Ya existe un usuario con el mismo dni")

            else:
                self.usuarios_nro_cuenta.append({personita.num_unic: [
                    personita._nombre, personita._edad, personita._dni, personita.num_unic, personita.clave, personita.estado_bloq]})

    def mostrar_cliente(self, dni):

        for usuario in self.usuarios:
            if usuario.has_key(dni):
                print("\n", usuario)

            else:
                print("\nNo existe un cliente con ese dni")


class Cajero_automatico(Banco):
    """
    Permite almacenar y autenticar a las personas registradas en el banco
    """

    personas = []  # Esta lista contendrá objetos de la clase Persona

    def __init__(self, dinero, personas=[]):
        """
        Constructor que nos permite inicializar al cajero automático
        """
        self.personas = personas
        self.dinero = dinero

    @property
    def dinero(self):
        """
        Permite editar la propiedad de cantidad total de dinero almacenada en la tarjeta bancaria de la persona
        """
        return self.dinero

    @dinero.setter
    # Ejecuta la operacion de depositar (1) o retirar (2) dinero de la tarjeta bancaria de la persona
    def dinero(self, operacion, n):
        if operacion == 1:
            self.dinero = self.dinero+int(n)
        elif operacion == 2:
            self.dinero = self.dinero-int(n)

    @property
    def person(self):
        return self.personas

    @person.setter
    def person(self, p):  # p será un objeto Persona
        self.personas.append(p)

    @property
    def cuenta(self):
        return self.personas


cuentas_ahorro = {11111111111111: 1111}  # 14digitos
cuentas_bloqueadas = []
M1 = 50
M2 = 100
M3 = 200

i = 0


def main():
    BancoBCP = Banco({})
    while i == 0:
        print("===============================================================================")
        print("                 BIENVENIDO A LA DE RED DE CAJEROS AUTOMATICOS                 \n\n                                   BANCO BCP")
        print("===============================================================================")
        print("1. Registrarse      2. Consultar datos de usuario       3. Ingresar Nº de cuenta")
        opcion_0 = int(input("Opcion: "))
        if opcion_0 == 1:
            nombre = input("\nDigite el nombre del usuario: ")
            apellido = input("Digite el apellido del usuario: ")
            edad = int(input("Digite la edad del usuario: "))
            DNi = int(input("Digite el DNI del usuario: "))
            persona1 = Persona(nombre, apellido, DNi, edad)

            BancoBCP.agregar_cliente(persona1)
            BancoBCP.agregar_cliente2(persona1)
        elif opcion_0 == 2:
            print("Ingrese su Nº de DNI")
            dni = int(input("DNI: "))
            BancoBCP.mostrar_cliente(dni)
            print()
            print("1. Cerrar sesion")
            cerrar_sesion = int(input("Opcion: "))
            if cerrar_sesion == 1:
                # break
                print()
            else:
                print("Opcion invalida")
        elif opcion_0 == 3:
            while i == 0:
                while True:
                    nº_cuenta_ahorro = int(input("Ingresa tu Nº de cuenta: "))
                    try:
                        if len(str(nº_cuenta_ahorro)) == 14:
                            break
                    except ValueError:
                        print("\nNúmero de cuenta no válida\n")
                break
            for usuario in BancoBCP.usuarios_nro_cuenta:
                if usuario.has_key(nº_cuenta_ahorro):
                    if usuario[nº_cuenta_ahorro][5] == 0:
                        contador = 3

                        while contador <= 3 and contador > 0:
                            clave_escrita = int(input("Ingrese su clave: "))
                            if clave_escrita == clave_sistema:
                                print(
                                    "===============================================================================")
                                print(
                                    "                                      MENU                                     ")
                                print(
                                    "===============================================================================")
                                print(" 1. OPERACIONES BANCARIAS")
                                print(" 2. CONFIGURAR CUENTA")
                                menuprincipal = int(input("Opcion: "))
                                if menuprincipal == 1:
                                    print(
                                        "===============================================================================")
                                    print(
                                        "                             OPERACIONES BANCARIAS                             ")
                                    print(
                                        "===============================================================================")
                                    print(" 1. DEPOSITO")
                                    print(" 2. RETIRO")
                                    menu1 = int(input("Opcion: "))
                                    if menu1 == 1:
                                        print("Depositar a:")
                                        while i == 0:
                                            while True:
                                                depositar_a = int(
                                                    input("Nº cuenta: "))
                                                try:
                                                    if 12 < len(str(depositar_a)) < 15:
                                                        break
                                                except ValueError:
                                                    print()
                                            break
                                        print(
                                            "Monto: \n1. s/. 50     2. s/. 100     3. s/. 200")
                                        cantidad = int(input("Opcion: "))
                                        print("1. Depositar        2. Cancelar")
                                        opcion1 = int(input("Opcion: "))
                                        if opcion1 == 1:
                                            print(
                                                "===============================================================================")
                                            print(
                                                "                                     DEPOSITO                                   ")
                                            print(
                                                "===============================================================================")
                                            print("Se deposito a: \n",
                                                  "Nº cuenta: ", depositar_a)
                                            if cantidad == 1:
                                                print("Monto: s/. ", M1)
                                            elif cantidad == 2:
                                                print("Monto: s/. ", M2)
                                            elif cantidad == 2:
                                                print("Monto: s/. ", M3)
                                            else:
                                                print("opcion invalida")
                                            print("Fecha: ", x)
                                            print(
                                                "===============================================================================")
                                            break
                                        elif opcion1 == 2:
                                            break
                                        else:
                                            print("Opcion invalida")
                                            break
                                    elif menu1 == 2:
                                        print(
                                            "Monto: \n1. s/. 50     2. s/. 100     3. s/. 200")
                                        retirar = int(input("Opcion: "))
                                        print("1. Retirar        2. Cancelar")
                                        opcion2 = int(input("Opcion: "))
                                        if opcion2 == 1:
                                            print(
                                                "=====================================================================================")
                                            print(
                                                "                                   RETIRO           ")
                                            print(
                                                "=====================================================================================")
                                            print("Se retiro de: \n",
                                                  "Nº cuenta: ", nº_cuenta_ahorro)
                                            if retirar == 1:
                                                print("Monto: s/. ", M1)
                                            elif retirar == 2:
                                                print("Monto: s/. ", M2)
                                            elif retirar == 3:
                                                print("Monto: s/. ", M3)
                                            else:
                                                print("opcion invalida")
                                                break
                                            print("Fecha: ", x)
                                        elif opcion2 == 2:
                                            break
                                        else:
                                            print("opcion invalida")
                                            break
                                    else:
                                        print("Opcion invalida")
                                        break
                                elif menuprincipal == 2:
                                    print(
                                        "===============================================================================")
                                    print(
                                        "                                     CUENTA                                    ")
                                    print(
                                        "===============================================================================")
                                    print("1. Cambiar clave")
                                    menu1 = int(input("Opcion: "))
                                    if menu1 == 1:
                                        nueva_clave = int(
                                            input("Nueva clave: "))
                                        cuentas_ahorro[nº_cuenta_ahorro] = nueva_clave
                                        break
                                    else:
                                        print("Opcion invalida")
                                        break
                                else:
                                    print("Opcion invalida")
                                    break
                            else:
                                contador = contador-1
                                if contador == 2:
                                    print("Le queda", contador, "intentos")
                                elif contador == 1:
                                    print("Le queda", contador, "intento")
                                    print("Si falla, se bloqueara la cuenta")
                                elif contador == 0:
                                    print(
                                        "CUENTA BLOQUEADA\nACERQUESE AL BANCO BCP")
                                    cuentas_bloqueadas.append(nº_cuenta_ahorro)
                    else:
                        print("CUENTA BLOQUEADA\nACERQUESE AL BANCO BCP")
                        break
                else:
                    print("La cuenta no existe\n")
                    print(
                        "-------------------------       SESION FINALIZADA       ------------------------")
        else:
            print("Opcion invalida")

        print("\n\n\n")
        time.sleep(3)


if __name__ == '__main__':
    main()
