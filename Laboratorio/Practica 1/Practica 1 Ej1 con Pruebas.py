"""
Practica 1 Ejercicio 1 con Pruebas Automáticas
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
import unittest
import re
def ej1(txt):
    p = re.compile('((([1-2][0-9])|[1-9])?[0-9]\.){3}(([1-2][0-9])|[1-9])?[0-9]$')
    if re.match(p,txt):
        return "SI"
    else:
        return "NO"

class TestIPChecker(unittest.TestCase):
  def testCorrectos(self):
    tests = [
      '0.0.0.0',
      '255.255.255.255',
      '10.0.0.1',
      '192.178.0.1',
      '200.0.1.5',
      '1.2.3.4',
      '12.34.56.78',
      '78.59.65.213'
    ]
    for e in tests:
      self.assertEqual(ej1(e), 'SI', 'Falso Negativo')
    
  def testIncorrectos(self):
    tests = [
      '...',
      'as.ds.12.1w3',
      '15.21.31.300',
      '01.011.012.099',
      '.12.2.1',
      '1..12.5',
      'aa.aa.aa.aa',
      '0a.12.5a.12'
    ]
    for e in tests:
      self.assertEqual(ej1(e), 'NO', 'Falso Positivo')

if __name__ == '__main__':
    unittest.main()
