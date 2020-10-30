"""
Practica 1 Ejercicio 2 Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""

import re
p = re.compile('[a-zA-Z]+[a-zA-Z0-9]*$')
txt=input("Ingresa el nombre de una variable: ")
while(1):
    if re.match(p,txt):
        print( "Válido" )
    else:
        print( "Inválido" )
    txt=input("Puedes ingresar otro nombre de una variable: ")
