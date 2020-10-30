"""
Practica 1 Ejercicio 3 Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""

import re
p = re.compile('(((m|M)e gustaría pedirle)|((l|L)e pido)|((s|S)olicito))[^\.]*\.')
txt=input("Ingresa el texto a analizar: ")
while(1):
    result = p.search(txt)
    if result:
        print("Solicitud:",result.group(0))
    else:
        print("Solicitud no encontrada")
    txt=input("Puedes ingresar otro texto: ")
