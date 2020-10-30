"""
Practica 0 Ejercicio 2 Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""

def ej2(txt):
    vocales=['a','e','i','o','u']
    reemplazos={'ar':'ando','ir':'iendo','er':'iendo'}
    i=txt.find(' ')
    verbo=txt[:i]
    gerundio=txt[i+1:]
    if verbo=="reir":
        if gerundio=="riendo":
            print("SI")
            return 1
        else:
            print("NO")
            return 0
    raiz=verbo[:-2]
    term=verbo[-2:]
    if raiz[-1] in vocales and (term=="ir" or term=="er"):
        if gerundio==raiz+"yendo":
            print("SI")
            return 1
        else:
            print("NO")
            return 0
    if term in reemplazos and gerundio==raiz+reemplazos[term]:
        print("SI")
        return 1
    else:
        print("NO")
        return 0

print ("Ingresa un verbo y su gerundio, separados por un espacio")
while(1):
    ej2(input())
    print ("Puedes ingresar otro ejemplo")
