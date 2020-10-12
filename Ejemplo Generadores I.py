def generaPares(limite):
    num = 1
    while(num < limite):
        yield num*2
        num = num + 1

devuelve_pares = generaPares(10)
print(generaPares(10)) 

for i in devuelve_pares:
    print(i)