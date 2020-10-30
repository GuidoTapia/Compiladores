"""
Practica 1 Ejercicio 1 Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""

import re
p = re.compile('[1|2]?[0-9]{1,2}\.[1|2]?[0-9]{1,2}\.[1|2]?[0-9]{1,2}')
txt=input("Ingresa una IP: ")
while(1):
    if re.match(p,txt):
        print( "SI ES UN IP" )
    else:
        print( "NO ES UN IP" )
    txt=input("Puedes ingresar otra IP: ")
