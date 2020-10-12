continuar = True
lista = [""]
while(continuar == True):
    print("ABCC EN PYTHON")
    print("")
    print("MENU")
    print("Presiona 1 para dar altas")
    print("presiona 2 para buscar")
    print("Presiona 3 para consultar")
    print("presiona 4 para dar bajas")
    print("presiona 5 para modificar")
    print("presiona 6 para salir")

    def agregar_nombre(nombre):
        lista.append(nombre)

    def buscar_nombre(b_nombre):
        convertidor = b_nombre in lista
        if(convertidor == True):
            indice = lista.index(b_nombre)
            print("Es este: ", b_nombre)
            print("Posicion: ", indice)
        else:
            print("No existe")

    def eliminar_nombre(e_nombre):
        convertidor2 = e_nombre in lista
        if(convertidor2 == True):
            indice2 = lista.index(e_nombre)
            print("Es este: ", e_nombre)
            print("Posicion: ", indice2)
            print("ELIMINAR? Escriba 's' para eliminarlo y 'n' para conservarlo")
            opcion_e = input()
            if(opcion_e == "s"):
                lista.remove(e_nombre)
                print("SE ELIMINO")
            else:
                print("NO SE ELIMINO")
        else:
            print("No existe")

    def modificar_nombre(m_nombre):
        convertidor3 = m_nombre in lista
        if(convertidor3 == True):
            indice3 = lista.index(m_nombre)
            print("Es este: ", m_nombre)
            print("Posicion: ", indice3)
            print("Modificar? Escriba 's' para modificarlo y 'n' para conservarlo")
            opcion_m = input()
            if(opcion_m == "s"):
                print("Escribe el nuevo nombre:")
                nuevo_nombre = input()
                lista.insert(indice3, nuevo_nombre)
                lista.remove(m_nombre)
                print("SE MODIFICO")
            else:
                print("NO SE MODIFICO")
        else:
            print("No existe")

    opcion = int(input())

    if(opcion == 1):
        print("ALTAS")
        print("Introduce el nombre:")
        nombre = input()
        agregar_nombre(nombre)
        print("Ir al menu? S/N")
        op1 = input()
        if(op1 == "s"):
            opcion = 1
            print("")
        else:
            break
    if(opcion == 2):
        print("BUSCAR")
        print("Introduce el nombre a buscar")
        b_nombre = input()
        buscar_nombre(b_nombre)
        print("Ir al menu? S/N")
        op2 = input()
        if(op2 == "s"):
            opcion = 1
            print("")
        else:
            break
    if(opcion == 3):
        print("CONSULTA")
        print(lista[:])
        print("Ir al menu? S/N")
        op3 = input()
        if(op3 == "s"):
            print("")
            opcion = 1
        else:
            break
    if(opcion == 4):
        print("Eliminar")
        print("Introduce el nombre a eliminar")
        e_nombre = input()
        eliminar_nombre(e_nombre)
        print("Ir al menu? S/N")
        op4 = input()
        if(op4 == "s"):
            print("")
            opcion = 1
        else:
            break
    if(opcion == 5):
        print("Modificar")
        print("Introduce el nombre a Modificar")
        m_nombre = input()
        modificar_nombre(m_nombre)
        print("Ir al menu? S/N")
        op5 = input()
        if(op5 == "s"):
            print("")
            opcion = 1
        else:
            break
    if(opcion == 6):
        break
print("Creado por Eduardo Alonso 01/09/2020")
1