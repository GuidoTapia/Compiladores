"""
Practica 0 Ejercicio 3 Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curson : Compiladores - CCOMP 8-1

Resultado de envio en UVA
25427147    537	Artificial Intelligence?    Accepted	PYTH3	0.010	2020-08-28 22:26:06
"""


mult={'m':0.001,'k':1000,'M':1000000}
n=int(input())
for j in range(n):
    txt=input()
    pI=txt.find("P=")
    pF=txt.find("W",pI)
    uI=txt.find("U=")
    uF=txt.find("V",uI)
    iI=txt.find("I=")
    iF=txt.find("A",iI)
    pFloat=1
    uFloat=1
    iFloat=1
    if(txt[pF-1] in mult):
        pFloat=mult[txt[pF-1]]
        pF-=1
    if(txt[uF-1] in mult):
        uFloat=mult[txt[uF-1]]
        uF-=1
    if(txt[iF-1] in mult):
        iFloat=mult[txt[iF-1]]
        iF-=1
    print("Problem #"+ str(j+1))
    if pI==-1:
        iFloat*=float(txt[iI+2:iF])
        uFloat*=float(txt[uI+2:uF])
        print("P=%.2fW\n" % (uFloat*iFloat))
    elif uI==-1:
        pFloat*=float(txt[pI+2:pF])
        iFloat*=float(txt[iI+2:iF])
        print("U=%.2fV\n" % (pFloat/iFloat))
    else:
        pFloat*=float(txt[pI+2:pF])
        uFloat*=float(txt[uI+2:uF])
        print("I=%.2fA\n" % (pFloat/uFloat))
