def generaPares(limite):
    num = 1
    while(num < limite):
        yield num*2
        num = num + 1

devuelve_pares = generaPares(10)

print(next(devuelve_pares))

print("Aqui podria ir más codigo...")

print(next(devuelve_pares))

print("Aqui podria ir más codigo...")

print(next(devuelve_pares))
