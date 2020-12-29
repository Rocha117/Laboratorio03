def generar_pares(limite):
    numero=1
    while numero<limite:
        yield numero*2
        numero=numero+1
devuelve_pares=generar_pares(10)
print(next(devuelve_pares))
print("Aqui puede ir mas codigo ...")
print(next(devuelve_pares))
print("Aqui puede ir mas codigo ...")
print(next(devuelve_pares))
print("Aqui puede ir mas codigo ...")
print(next(devuelve_pares))



