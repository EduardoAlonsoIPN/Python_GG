#Cálculo de la distancia entre dos puntos
#Autor: Luis Eduardo Alonso Ramírez 06/09/2020

import math as m
import sys
continuar = True

def distancia_entre_dos_puntos(var_a_x, var_a_y, var_b_x, var_b_y):
    sumando1 = (var_b_x - var_a_x)**2
    sumando2 = (var_b_y - var_a_y)**2
    discriminante = (sumando1 + sumando2)
    #print(sumando1)
    #print(sumando2)
    #print(discriminante)
    if(discriminante < 0):
        error = 1
    else:    
        resultado1 = m.sqrt(discriminante)  
    return resultado1

def coordenadas_del_punto_p(var_p_y, var_c_x, var_c_y, var_dis_p_c):
    producto1 = -(var_c_x)**2 - (var_c_y)**2 - (var_p_y)**2 + (var_dis_p_c)**2 + (2*var_c_y*var_p_y)
    co_a = 1
    co_b = (-2*var_c_x)
    co_c = -producto1
    print(co_c)
    discriminante2 = ((co_b**2) - (4*co_a*co_c))
    print(discriminante2)
    #res_x_1 = 0
    #res_x_2 = 0
    if(discriminante2 < 0):
        error = 1
        codigos_de_error(error)
    else:
        res_x_1 = (-co_b + m.sqrt(discriminante2))/(2*co_a)
        res_x_2 = (-co_b - m.sqrt(discriminante2))/(2*co_a)
        resultado2 = [res_x_1, res_x_2]
    return resultado2

def codigos_de_error(error):
    m_type = ["ERROR, SE GENERAN RAICES NEGATIVAS, INTENTA CON OTROS VALORES", "ERROR, NO INTRODUCISTE NINGUN DATO"]
    if(error == 1):
        print(m_type[0])
    if(error == 2):
        print(m_type[2])
    sys.exit()            

while(continuar == True):
    print("DISTANCIA ENTRE DOS PUNTOS \n")
    print("PRESIONE 1 PARA CALCULAR LA DISTANCIA ENTRE\nDOS PUNTOS 'A' Y 'B' \n")
    print("PRESIONE 2 PARA ENCONTRAR LAS CORDENADA 'X' DE UN PUNTO 'P'\nCONOCIENDO LA COORDENADA 'Y' DEL PUNTO 'P',\nLAS CORDENADAS DE UN PUNTO 'C' Y SU DISTANCIA AL PUNTO P\n")
    print("PRESIONE CUALQUIER OTRA TECLA PARA SALIR")
    opcion = int(input())
    if(opcion == 1):
        var_a_x = float(input("INTRODUCE LA COORDENADA 'X' DEL PUNTO 'A': \n"))
        var_a_y = float(input("INTRODUCE LA COORDENADA 'Y' DEL PUNTO 'A': \n"))
        var_b_x = float(input("INTRODUCE LA COORDENADA 'X' DEL PUNTO 'B': \n"))
        var_b_y = float(input("INTRODUCE LA COORDENADA 'Y' DEL PUNTO 'B': \n"))
        distancia_a_b = distancia_entre_dos_puntos(var_a_x, var_a_y, var_b_x, var_b_y)
        print("LA DISTANCIA ES DE: ", distancia_a_b, " UNIDADES")
        print("\nHACER OTRO CALCULO? S/N")
        opn = input()
        if(opn == "s"):
            continuar = True
        else:
            break    

    if(opcion == 2):
        var_p_y = float(input("INTRODUCE LA COORDENADA 'Y' DEL PUNTO 'P': \n"))
        var_c_x = float(input("INTRODUCE LA COORDENADA 'X' DEL PUNTO 'C': \n"))
        var_c_y = float(input("INTRODUCE LA COORDENADA 'Y' DEL PUNTO 'C': \n"))
        var_dis_p_c = float(input("INTRODUCE LA DISTANCIA ENTRE EL PUNTO 'P' Y EL PUNTO 'C': \n"))
        coordenada_p_x = coordenadas_del_punto_p(var_p_y, var_c_x, var_c_y, var_dis_p_c)
        print("LOS DOS POSIBLES VALORES DE LA COORDENADA X DEL PUNTO P \n SON: ", coordenada_p_x)    
        print("\nHACER OTRO CALCULO? S/N")
        opn = input()
        if(opn == "s"):
            continuar = True
        else:
            break    
print("Terminado")    
print("Creado por Eduardo Alonso 06/09/2020")     