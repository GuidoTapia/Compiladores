"""
Practica 3 Ejercicio con Pruebas Unitarias
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
import unittest
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
def TokensToStr(linea):
    tokens=analizadorLexico(linea)
    txt=""
    for e in tokens:
        txt+=e.toString()
    return txt

class TestAnalizadorLexico(unittest.TestCase):
  def testTokens(self):
    tests = [
      '1+2',
      '(4*3)-8',
      '60 / ( 5 + 3 ) - 0',
      'A=12',
      'variable1 =14',
      'C = A + variable1'
    ]
    respuestas=[
        "Token[1]: pos = 0, tipo =EToken[+]: pos = 1, tipo =OToken[2]: pos = 2, tipo =E"
        ,"Token[(]: pos = 0, tipo =OToken[4]: pos = 1, tipo =EToken[*]: pos = 2, tipo =OToken[3]: pos = 3, tipo =EToken[)]: pos = 4, tipo =OToken[-]: pos = 5, tipo =OToken[8]: pos = 6, tipo =E"
        ,"Token[60]: pos = 0, tipo =EToken[(]: pos = 5, tipo =OToken[5]: pos = 7, tipo =EToken[+]: pos = 9, tipo =OToken[3]: pos = 11, tipo =EToken[)]: pos = 13, tipo =OToken[-]: pos = 15, tipo =OToken[0]: pos = 17, tipo =E"
        ,"Token[A]: pos = 0, tipo =VToken[=]: pos = 1, tipo =OToken[12]: pos = 2, tipo =E"
        ,"Token[variable1]: pos = 0, tipo =VToken[=]: pos = 10, tipo =OToken[14]: pos = 11, tipo =E"
        ,"Token[C]: pos = 0, tipo =VToken[=]: pos = 2, tipo =OToken[A]: pos = 4, tipo =VToken[+]: pos = 6, tipo =OToken[variable1]: pos = 8, tipo =V"
    ]
    for i in range(len(tests)):
      self.assertEqual(TokensToStr(tests[i]), respuestas[i], 'Falso Negativo')
    

if __name__ == '__main__':
    unittest.main()
