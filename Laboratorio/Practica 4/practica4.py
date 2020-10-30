"""
Practica 4 - El ingreso de la gramatica es mediente el archivo gramatica.txt
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
class Produccion:
    izq=""
    der=[]
    def __init__(self,i,d):
        self.izq=i
        self.der=d
    def getString(self):
        return self.izq+" -> "+' '.join(map(str, self.der))
class Gramatica:
    produccion = [] #Lista de producciones
    terminales = set() #Conjunto de terminales
    noterminales = set() #no terminales
    def print(self): #Crear una función para imprimir
        for p in self.produccion:
            print (p.getString())
    def cargar(self,texto):
        for linea in texto:
            izqProdTemp =""
            strTemp = ""
            derProdTemp =[]
            idx=0
            while idx<len(linea):
                if (linea[idx]==':' and linea[idx+1]=='='):
                    izqProdTemp = strTemp
                    self.noterminales.add(strTemp)
                    strTemp=""
                    idx+=1
                elif (linea[idx]=='|'):
                    if(len(strTemp)):
                        derProdTemp.append(strTemp)
                    self.produccion.append(Produccion(izqProdTemp,derProdTemp))
                    derProdTemp =[]
                elif (linea[idx]==' ' or linea[idx]=='\t' or linea[idx]=='\n'):
                    if (len(izqProdTemp) and len(strTemp)):
                        derProdTemp.append(strTemp)
                        self.terminales.add(strTemp)
                        strTemp=""
                else:
                    strTemp+=linea[idx]
                idx+=1
            if(len(strTemp)):
                derProdTemp.append(strTemp)
                self.terminales.add(strTemp)
            self.produccion.append(Produccion(izqProdTemp,derProdTemp))
            izqProdTemp =""
            derProdTemp =[]
        for e in self.noterminales:
            self.terminales.remove(e)
        print(self.terminales)
        print(self.noterminales)
    def getProduccion(self,izq):
        aux=""
        for p in self.produccion:
            if (p.izq==izq):
                aux+=" | "*(len(aux)>0)+ p.der

class TAS:
    tablaSintactica={}
    terminales=[]
    noterminales=[]
    def llenarEstaticamente(self,gram):
        self.terminales=list(gram.terminales)
        self.noterminales=list(gram.noterminales)
        for nT in gram.noterminales:
            self.tablaSintactica[nT]={}
            for t in gram.terminales:
                self.tablaSintactica[nT][t]=[]
        for p in gram.produccion:
            self.tablaSintactica[p.izq][p.der[0]]=p.der
        self.terminales.sort()
        self.noterminales.sort()
        #print(self.tablaSintactica)
    def print(self):
        aux='\t|'
        for t in self.terminales:
            aux+=t+'\t|'
        print (aux)
        for nT in self.noterminales:
            aux=nT+'\t|'
            for t in self.terminales:
                aux+=' '.join(map(str, self.tablaSintactica[nT][t]))
                aux+='\t|'
            print (aux)
algo=Gramatica()
algo.cargar(open("gramatica.txt","r"))
algo.print()
tabla=TAS()
tabla.llenarEstaticamente(algo)
tabla.print()
