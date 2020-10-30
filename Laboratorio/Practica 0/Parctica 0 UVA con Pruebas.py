"""
Practica 0 Ejercicio 3 con Pruebas
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curson : Compiladores - CCOMP 8-1
"""
import unittest

mult={'m':0.001,'k':1000,'M':1000000}
def ej3(txt):
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
    if pI==-1:
        iFloat*=float(txt[iI+2:iF])
        uFloat*=float(txt[uI+2:uF])
        return "P=%.2fW" % (uFloat*iFloat)
    elif uI==-1:
        pFloat*=float(txt[pI+2:pF])
        iFloat*=float(txt[iI+2:iF])
        return "U=%.2fV" % (pFloat/iFloat)
    else:
        pFloat*=float(txt[pI+2:pF])
        uFloat*=float(txt[uI+2:uF])
        return "I=%.2fA" % (pFloat/uFloat)


class TestEjercicioUVA(unittest.TestCase):
  def testCorrectos(self):
    tests = [
        'If the voltage is U=200V and the current is I=4.5A, which power is generated?',
        'A light-bulb yields P=100W and the voltage is U=220V. Compute the current, please.',
        'bla bla bla lightning strike I=2A bla bla bla P=2.5MW bla bla voltage?'
    ]
    answers=[
        'P=900.00W',
        'I=0.45A',
        'U=1250000.00V'
    ]
    for i in range(len(tests)):
      self.assertEqual(ej3(tests[i]), answers[i], 'Falso Negativo')


if __name__ == '__main__':
    unittest.main()
