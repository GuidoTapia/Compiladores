"""
Practica 0 Ejercicio 1 Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""

def ej1(txt):
    pila=[]
    signos={')':'(','}':'{',']':'['}
    for e in txt:
        if e in signos.values():
            pila+=e
        elif e in signos:
            if len(pila) and pila[-1]==signos[e]:
                pila.pop(-1)
            else:
                print("NO")
                return 0
    if len(pila):
        print("NO")
        return 0
    else:
        print("SI")
        return 1

    
print("Ingresar una cadena compuesta solamente por parentesis, corchetes, llaves y espacios")
while(1):    
    ej1(input())
    print("Puedes ingresar otra cadena")
