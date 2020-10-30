"""
Practica 0 Ejercicio 2 con Pruebas
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curson : Compiladores - CCOMP 8-1
"""
import unittest
def ej2(txt):
    vocales=['a','e','i','o','u']
    reemplazos={'ar':'ando','ir':'iendo','er':'iendo'}
    i=txt.find(' ')
    verbo=txt[:i]
    gerundio=txt[i+1:]
    if verbo=="reir":
        if gerundio=="riendo":
            return 'SI'
        else:
            return 'NO'
    raiz=verbo[:-2]
    term=verbo[-2:]
    if raiz[-1] in vocales and (term=="ir" or term=="er"):
        if gerundio==raiz+"yendo":
            return 'SI'
        else:
            return 'NO'
    if term in reemplazos and gerundio==raiz+reemplazos[term]:
        return 'SI'
    else:
        return 'NO'

class TestGerundio(unittest.TestCase):
  def testCorrectos(self):
    tests = [
      'amar amando',
      'llover lloviendo',
      'reir riendo',
      'abatir abatiendo',
      'cantar cantando',
      'correr corriendo',
      'salir saliendo',
      'caer cayendo',
      'huir huyendo'
    ]
    for e in tests:
      self.assertEqual(ej2(e), 'SI', 'Falso Negativo')
    
  def testIncorrectos(self):
    tests = [
      'caer caindo',
      'correr correndo',
      'salir salendo',
      'amar amrndo',
      'llover llovendo',
      'reir rindo',
      'abatir abatindo',
      'cantar cantendo',
      'correr corrando',
      'salir salindo',
      'caer caiendo',
      'huir huiendo'
    ]
    for e in tests:
      self.assertEqual(ej2(e), 'NO', 'Falso Positivo')

if __name__ == '__main__':
    unittest.main()
