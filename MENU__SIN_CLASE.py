import datetime
x=datetime.datetime.now()
import time
class Tarjeta_bancaria:
    def _init_(self, tarjeta_bloqueada):
        self.nº_cuenta=nº_cuenta
        self.tarjeta_bloqueada=tarjeta_bloqueada
    def estado(self, tarjeta_bloqueada):
        print(f"AVISO\n {self.tarjeta_bloqueada}")

       
i=0
cuentas_ahorro={11111111111111:1111}#14digitos
cuentas_bloqueadas=[]
M1=50
M2=100
M3=200

while i==0:
    print("===============================================================================")
    print("                 BIENVENIDO A LA DE RED DE CAJEROS AUTOMATICOS                 \n\n                                   BANCO BCP")
    print("===============================================================================")
    print("1. Registrarse      2. Consultar datos de usuario       3. Ingresar Nº de cuenta")
    opcion_0=int(input("Opcion: "))
    if opcion_0==1:
        print()
    elif opcion_0==2:
        print("Ingrese su Nº de DNI")
        dni=int(input("DNI: "))
        print()
        print("1. Cerrar sesion")
        cerrar_sesion=int(input("Opcion: "))
        if cerrar_sesion==1:
            #break
            print()
        else:
            print("Opcion invalida")
    elif opcion_0==3:
        while i==0:
            while True:
                nº_cuenta_ahorro=int(input("Ingresa tu Nº de cuenta: "))
                try:
                    if len(str(nº_cuenta_ahorro))==14:
                        break
                except ValueError:
                    print()
            break
        if nº_cuenta_ahorro in cuentas_ahorro or (nº_cuenta_ahorro in cuentas_bloqueadas):
            contador = 3
            clave_sistema=cuentas_ahorro[nº_cuenta_ahorro]
            if nº_cuenta_ahorro in cuentas_ahorro and nº_cuenta_ahorro in cuentas_bloqueadas:
                print("CUENTA BLOQUEADA\nACERQUESE AL BANCO INTERBANK")
                break
            while contador <=3 and contador >0 :
                clave_escrita=int(input("Ingrese su clave: "))
                if clave_escrita==clave_sistema:
                    print("===============================================================================")
                    print("                                      MENU                                     ")
                    print("===============================================================================")
                    print(" 1. OPERACIONES BANCARIAS")
                    print(" 2. CONFIGURAR CUENTA")
                    menuprincipal= int(input("Opcion: "))
                    if menuprincipal == 1:
                        print("===============================================================================")
                        print("                             OPERACIONES BANCARIAS                             ")
                        print("===============================================================================")
                        print(" 1. DEPOSITO")
                        print(" 2. RETIRO") 
                        menu1= int(input("Opcion: "))
                        if menu1==1:
                            print("Depositar a:")
                            while i==0:
                                while True:
                                    depositar_a=int(input("Nº cuenta: "))
                                    try:
                                        if 12<len(str(depositar_a))<15:
                                            break
                                    except ValueError:
                                        print()
                                break
                            print("Monto: \n1. s/. 50     2. s/. 100     3. s/. 200")
                            cantidad=int(input("Opcion: "))
                            print("1. Depositar        2. Cancelar")
                            opcion1=int(input("Opcion: "))
                            if opcion1==1:
                                print("===============================================================================")
                                print("                                     DEPOSITO                                   ")
                                print("===============================================================================")
                                print("Se deposito a: \n", "Nº cuenta: ", depositar_a)
                                if cantidad==1:
                                    print("Monto: s/. ", M1)
                                elif cantidad==2:
                                    print("Monto: s/. ", M2)
                                elif cantidad==2:
                                    print("Monto: s/. ", M3)
                                else:
                                    print("opcion invalida")
                                print("Fecha: ", x)
                                print("===============================================================================")
                                break 
                            elif opcion1==2:
                                break
                            else:
                                print("Opcion invalida")
                                break
                        elif menu1==2:
                            print("Monto: \n1. s/. 50     2. s/. 100     3. s/. 200")
                            retirar=int(input("Opcion: "))
                            print("1. Retirar        2. Cancelar")
                            opcion2=int(input("Opcion: "))
                            if opcion2==1:
                                print("=====================================================================================")
                                print("                                   RETIRO           ")
                                print("=====================================================================================")
                                print("Se retiro de: \n", "Nº cuenta: ", nº_cuenta_ahorro)
                                if retirar==1:
                                    print("Monto: s/. ", M1)
                                elif retirar==2:
                                    print("Monto: s/. ", M2)
                                elif retirar==3:
                                    print("Monto: s/. ", M3)
                                else:
                                    print("opcion invalida")
                                    break
                                print("Fecha: ", x)
                            elif opcion2==2:
                                break
                            else:
                                print("opcion invalida")
                                break
                        else:
                            print("Opcion invalida")
                            break
                    elif menuprincipal == 2:
                        print("===============================================================================")
                        print("                                     CUENTA                                    ")
                        print("===============================================================================")
                        print("1. Cambiar clave") 
                        menu1= int(input("Opcion: "))
                        if menu1==1:
                            nueva_clave=int(input("Nueva clave: "))
                            cuentas_ahorro[nº_cuenta_ahorro]=nueva_clave
                            break
                        else:
                            print("Opcion invalida")
                            break
                    else:
                        print("Opcion invalida")
                        break
                else:
                    contador= contador-1
                    if contador==2:
                        print("Le queda", contador, "intentos")
                    elif contador ==1:
                        print("Le queda", contador, "intento")
                        print("Si falla, se bloqueara la cuenta")
                    elif contador ==0:
                        print("CUENTA BLOQUEADA\nACERQUESE AL BANCO INTERBANK")
                        cuentas_bloqueadas.append(nº_cuenta_ahorro)      
        else:
            print("La cuenta no existe\n")
            print("-------------------------       SESION FINALIZADA       ------------------------")
    else:
        print("Opcion invalida")
        
    print("\n\n\n")
    time.sleep(3)
