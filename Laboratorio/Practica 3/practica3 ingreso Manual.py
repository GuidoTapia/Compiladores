"""
Practica 3 Ejercicio Ingreso Manual
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
operadores="*()-+="

class Token:
    palabra = "" #almacena una copia de la palabra
    indice = -1 #en donde apareció en la sentencia
    tipo = '' #E (entero), V (variable), O (operador)
    def __init__(self,cadena, i, t):
        self.palabra=cadena
        self.indice=i
        self.tipo=t
    def toString(self):
        return "Token["+self.palabra+"]: pos = "+str(self.indice)+", tipo ="+self.tipo

def reconoceNumero(linea,idx):
    iAux=idx
    palabra=""
    while(iAux<len(linea) and linea[iAux]!=' ' and linea[iAux] not in operadores):
        palabra+=linea[iAux]
        iAux=iAux+1
    if(palabra.isnumeric()):
        return Token(palabra,idx,'E'),iAux
    else:
        return iAux,0
def reconoceVariable(linea,idx):
    iAux=idx
    palabra=""
    while(iAux<len(linea) and linea[iAux]!=' ' and linea[iAux] not in operadores):
        palabra+=linea[iAux]
        iAux=iAux+1
    if(palabra.isalnum()):
        return Token(palabra,idx,'V'),iAux
    else:
        return iAux,0

def analizadorLexico(linea):
    tokens=[]
    idx=0
    while idx<len(linea):
        if linea[idx].isnumeric():
            token,idx=reconoceNumero(linea,idx)
            if token !=0:
                tokens.append(token)
        elif linea[idx].isalpha():
            token,idx=reconoceVariable(linea,idx)
            if token !=0:
                tokens.append(token)
        elif linea[idx] in operadores:
            tokens.append(Token(linea[idx],idx,'O'))
            idx=idx+1
        else:
            idx=idx+1
    return tokens

while True:
    linea = input("Ingresa un línea de código para analizar: ")
    tokens = analizadorLexico( linea )
    for token in tokens:
        print( token.toString() )
