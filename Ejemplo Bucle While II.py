# Sintaxis Básica Curso Phyton
edad = int(input("Introduce tu edad por favor: "))

while (edad <= 18 or edad > 100):
    print("Has introducido una edad negativa, vuelve a intentarlo")
    edad = int(input("Introduce tu edad por favor: "))
print("Gracias por colaborar, Puedes pasar")
print("Edad del aspirante " + str(edad))    