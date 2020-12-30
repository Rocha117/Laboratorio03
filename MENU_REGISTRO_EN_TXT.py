import datetime
import time
import random

x = datetime.datetime.now()


class Tarjeta_bancaria:

    def __init__(self, No_tarjeta, estado_bloq=0):

        tarjeta = "4"+str(random.randint(100, 999))+"-" + \
            str(random.randint(1000, 9999))+"-" + \
            str(random.randint(1000, 9999))+"-"+str(random.randint(1000, 9999))
        self.No_tarjeta = No_tarjeta
        self.No_tarjeta = tarjeta
        self.estado_bloq = estado_bloq

    @property
    def estado(self):
        return self.estado_bloq

    @estado.setter
    def estado(self):
        # Si la cuenta está bloqueada, su estado será 1, caso contrario es 0
        self.estado_bloq = 1


class Cuenta_bancaria(object):

    def __init__(self, num_unic, cci, clave):
        num_cuenta = random.randint(10000000000, 99999999999)
        self.num_unic = num_unic
        self.num_unic = str(int(
            "193"+str(num_cuenta)))
        self.cci = cci
        self.cci = str(int('002'+'193'+'00'+str(num_cuenta) +
                           str(random.randint(10, 99))))
        self.clave = clave
        self.clave = str(random.randint(1000, 9999))

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


class Persona(Tarjeta_bancaria, Cuenta_bancaria):
    """
    Permite asignarle a las personas una cuenta y una tarjeta bancaria
    """

    def __init__(self, nombre="", apellido="", dni="", edad=0, No_tarjeta="", estado_bloq=0, num_unic="", cci="", clave="", dinero=0):
        """
        Constructor que nos permite inicializar a una persona
        """
        Tarjeta_bancaria.__init__(self, No_tarjeta, estado_bloq)
        Cuenta_bancaria.__init__(self, num_unic, cci, clave)
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._edad = edad
        self._dinero = dinero

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


class Cajero_automatico:
    usuarios = []
    usuarios_nro_cuenta = []

    def __init__(self, usuarios=[], usuarios_nro_cuenta=[]):
        self.usuarios = usuarios
        self.usuarios_nro_cuenta = usuarios_nro_cuenta

    def agregar_cliente(self, personita):
        existe = 0

        for usuario in self.usuarios:

            for key in usuario.keys():

                if personita._dni == key:
                    existe = 1
                    break

                else:
                    existe = 0

        if existe == 1:
            global num_exis
            num_exis = 1
            return num_exis
        elif existe == 0:
            self.usuarios.append({personita._dni: [
                personita._nombre, personita._edad, personita._dni, personita.num_unic, personita.clave, personita.estado_bloq, personita.No_tarjeta, personita.cci, personita._apellido, personita._dinero]})

    def agregar_cliente2(self, personita):
        existe = 0

        for usuario in self.usuarios_nro_cuenta:

            for key in usuario.keys():

                if personita.num_unic == key:
                    existe = 1
                    break

                else:
                    existe = 0

        if existe == 1:
            pass
        elif existe == 0:
            self.usuarios_nro_cuenta.append({personita.num_unic: [
                personita._nombre, personita._edad, personita._dni, personita.num_unic, personita.clave, personita.estado_bloq, personita.No_tarjeta, personita.cci, personita._apellido, personita._dinero]})

    def mostrar_cliente(self, dni):
        existe = 0
        for usuario in self.usuarios:
            for key in usuario.keys():

                if dni == key:
                    existe = 1
                    break

                else:
                    existe = 0
            if existe == 1:
                print("\nCUENTA BANCARIA:\n")
                print(f"NOMBRE       :            {usuario[dni][0]}")
                print(f"APELLIDO     :            {usuario[dni][8]}")
                print(f"DNI          :            {usuario[dni][2]}")
                print(f"NRO DE CUENTA:            {usuario[dni][3]}")
                print(f"CLAVE        :            {usuario[dni][4]}")
                print(f"NRO TARJETA  :            {usuario[dni][6]}")
                print(f"CCI:         :            {usuario[dni][7]}")
                print(f"MONTO:       :            S/. {usuario[dni][9]}")
                archivo=open("REGISTRO_USUARIOS.txt", "a")
                archivo.write(f"NOMBRE       :            {usuario[dni][0]} \n")
                archivo.write(f"APELLIDO     :            {usuario[dni][8]} \n")
                archivo.write(f"DNI          :            {usuario[dni][2]} \n")
                archivo.write(f"NRO DE CUENTA:            {usuario[dni][3]} \n")
                archivo.write(f"CLAVE        :            {usuario[dni][4]} \n")
                archivo.write(f"NRO TARJETA  :            {usuario[dni][6]} \n")
                archivo.write(f"CCI:         :            {usuario[dni][7]} \n\n")
                archivo.write("- - - - - - - - - - - - - - - - - - - - - - - - -  \n\n")
                archivo.close()

                if usuario[dni][5] == 1:
                    print("\nESTADO:      :            CUENTA BLOQUEADA")

                break
            elif existe == 0:

                print("\nNo existe un cliente con ese dni")

M1 = 50
M2 = 100
M3 = 200
i = 0
def main():
    CajeroBCP = Cajero_automatico()
    while i == 0:

        print("===============================================================================")
        print("                 BIENVENIDO A LA DE RED DE CAJEROS AUTOMATICOS                 \n\n                                   BANCO BCP")
        print("===============================================================================")
        print("1. Registrarse      2. Consultar datos de usuario       3. Ingresar Nº de cuenta")
        opcion_0 = int(input("Opcion: "))
        if opcion_0 == 1:
            global num_exis
            num_exis = 0
            persona1 = Persona()
            persona1.nombre = input(
                "\nDigite el nombre del usuario         (Menor a 12 letras)             :     ")
            persona1.apellido = input(
                "Digite el apellido del usuario       (Menor a 12 letras)             :     ")
            persona1.edad = int(
                input("Digite la edad del usuario:          (En el rango de 18 a 100 años)  :     "))
            persona1.dni = str(int(
                input("Digite el DNI del usuario:           (8 dígitos)                     :     ")))
            CajeroBCP.agregar_cliente(persona1)
            if num_exis == 1:
                print("\nYa existe un usuario con el mismo dni\n")
            else:
                CajeroBCP.agregar_cliente2(persona1)
        elif opcion_0 == 2:
            print("Ingrese su Nº de DNI")
            dni = str(int(input("DNI: ")))
            CajeroBCP.mostrar_cliente(dni)
            print()
            print("1. Cerrar sesion")
            cerrar_sesion = int(input("Opcion: "))
            if cerrar_sesion == 1:

                print()
            else:
                print("Opcion invalida")
        elif opcion_0 == 3:
            while i == 0:
                while True:
                    nº_cuenta_ahorro = str(
                        int(input("Ingresa tu Nº de cuenta: ")))
                    try:
                        if len(nº_cuenta_ahorro) == 14:
                            break
                    except ValueError:
                        print("\nNúmero de cuenta no válida\n")
                break

            ex = 0
            ex2 = 0
            for usuario in CajeroBCP.usuarios_nro_cuenta:
                operacion = ""
                NEWCLAVE = 0
                bloq = 0
                for key in usuario.keys():
                    if nº_cuenta_ahorro == key:
                        ex = 1
                        break

                    else:
                        ex = 0
                if ex == 1:
                    dni3 = usuario[nº_cuenta_ahorro][2]
                    if usuario[nº_cuenta_ahorro][5] == 0:

                        contador = 3

                        while contador <= 3 and contador > 0:
                            clave_escrita = str(
                                int(input("Ingrese su clave: ")))
                            if clave_escrita == usuario[nº_cuenta_ahorro][4]:
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
                                                depositar_a = str(int(
                                                    input("Nº cuenta: ")))
                                                try:
                                                    if len(depositar_a) == 14:
                                                        break
                                                except ValueError:
                                                    print()
                                            break
                                        print(
                                            f"\nMonto: \n1. s/. {M1}     2. s/. {M2}     3. s/. {M3}")
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
                                            print(
                                                "Se deposito a: \nNº cuenta: ", depositar_a)
                                            if cantidad == 1:
                                                MONTO = usuario[nº_cuenta_ahorro][9]
                                                usuario[nº_cuenta_ahorro][9] = MONTO+M1
                                                operacion = "D1"
                                                print("Monto: s/. ", M1)
                                            elif cantidad == 2:
                                                MONTO = usuario[nº_cuenta_ahorro][9]
                                                usuario[nº_cuenta_ahorro][9] = MONTO+M2
                                                operacion = "D2"
                                                print("Monto: s/. ", M2)
                                            elif cantidad == 3:
                                                MONTO = usuario[nº_cuenta_ahorro][9]
                                                usuario[nº_cuenta_ahorro][9] = MONTO+M3
                                                operacion = "D3"
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
                                            f"\nMonto: \n1. s/. {M1}     2. s/. {M2}     3. s/. {M3}")
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
                                                MONTO = usuario[nº_cuenta_ahorro][9]
                                                usuario[nº_cuenta_ahorro][9] = MONTO-M1
                                                operacion = "R1"
                                                print("Monto: s/. ", M1)
                                            elif retirar == 2:
                                                MONTO = usuario[nº_cuenta_ahorro][9]
                                                usuario[nº_cuenta_ahorro][9] = MONTO-M2
                                                operacion = "R2"
                                                print("Monto: s/. ", M2)
                                            elif retirar == 3:
                                                MONTO = usuario[nº_cuenta_ahorro][9]
                                                usuario[nº_cuenta_ahorro][9] = MONTO-M3
                                                operacion = "R3"
                                                print("Monto: s/. ", M3)
                                            else:
                                                print("opcion invalida")
                                                break
                                            print("Fecha: ", x)
                                            print(
                                                "===============================================================================")
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
                                        while i == 0:
                                            while True:
                                                nueva_clave = str(int(
                                                    input("Nueva clave (4 dígitos): ")))
                                                try:
                                                    if len(nueva_clave) == 4:
                                                        break
                                                except ValueError:
                                                    print()
                                            break

                                        usuario[nº_cuenta_ahorro][4] = nueva_clave
                                        NEWCLAVE = 1
                                        print("\nCLAVE CAMBIADA")
                                        break
                                    else:
                                        print("Opcion invalida")
                                        break
                                else:
                                    print("Opcion invalida")
                                    break
                                contador = 0

                            else:
                                contador = contador-1
                                if contador == 2:
                                    print("\nLe queda", contador, "intentos\n")
                                elif contador == 1:
                                    print("\nLe queda", contador, "intento")
                                    print("Si falla, se bloqueará la cuenta\n")
                                elif contador == 0:
                                    print(
                                        "\nCUENTA BLOQUEADA\nACÉRQUESE AL BANCO BCP")
                                    usuario[nº_cuenta_ahorro][5] = 1
                                    bloq = 1
                    else:
                        print("CUENTA BLOQUEADA\nACÉRQUESE AL BANCO BCP")
                        break
                elif ex == 0:
                    print("La cuenta no existe\n")
                    print(
                        "-------------------------       SESION FINALIZADA       ------------------------")
            if operacion != "":
                for usuario in CajeroBCP.usuarios:

                    for key in usuario.keys():
                        if dni3 == key:
                            ex2 = 1
                            break

                        else:
                            ex2 = 0
                    if ex2 == 1:
                        if operacion == "D1":
                            usuario[dni3][9] = MONTO+M1
                        elif operacion == "D2":
                            usuario[dni3][9] = MONTO+M2
                        elif operacion == "D3":
                            usuario[dni3][9] = MONTO+M3
                        elif operacion == "R1":
                            usuario[dni3][9] = MONTO-M1
                        elif operacion == "R2":
                            usuario[dni3][9] = MONTO-M2
                        elif operacion == "R3":
                            usuario[dni3][9] = MONTO-M3
            if NEWCLAVE == 1:
                for usuario in CajeroBCP.usuarios:
                    for key in usuario.keys():
                        if dni3 == key:
                            ex2 = 1
                            break

                        else:
                            ex2 = 0
                    if ex2 == 1:
                        usuario[dni3][4] = nueva_clave
            if bloq == 1:
                for usuario in CajeroBCP.usuarios:
                    for key in usuario.keys():
                        if dni3 == key:
                            ex2 = 1
                            break

                        else:
                            ex2 = 0
                    if ex2 == 1:
                        usuario[dni3][5] = 1
        else:
            print("Opcion inválida")

        print("\n\n\n")
        time.sleep(3)


if __name__ == '__main__':
    main()