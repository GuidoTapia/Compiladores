"""
Practica 1 Ejercicio 2 con Pruebas Automáticas
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
import unittest
import re
def ej2(txt):
    p = re.compile('[a-zA-Z]+[a-zA-Z0-9]*$')
    if re.match(p,txt):
        return "SI"
    else:
        return "NO"

class TestVariablesChecker(unittest.TestCase):
  def testCorrectos(self):
    tests = [
      'hola',
      'variable',
      'variable1',
      'var12213asda',
      'VaRiAble123',
      'holaMundo',
      'abc123ABC',
      'posicion'
    ]
    for e in tests:
      self.assertEqual(ej2(e), 'SI', 'Falso Negativo')
    
  def testIncorrectos(self):
    tests = [
      '1hola',
      'var.iable',
      '1234',
      'var!123',
      '.algo',
      '10holaMundo',
      '123abcABC',
      '!posicion'
    ]
    for e in tests:
      self.assertEqual(ej2(e), 'NO', 'Falso Positivo')

if __name__ == '__main__':
    unittest.main()
