"""
Practica 0 Ejercicio 1 con Pruebas Automáticas
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
import unittest
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
                return 'NO'
    if len(pila):
        return 'NO'
    else:
        return 'SI'

class TestParenthesesChecker(unittest.TestCase):
  def testCorrectos(self):
    tests = [
      '()()',
      '[ [ ( ) ] ]',
      '[[[[[[[[[[( )]]]]]]]]]]',
      '{[() ()]([() ]())}',
      '({[( {[]})] })',
      '[][][ ]{ }{}{}( )()()',
      '[{[( )()() ]}]',
      '{ [][() ][ ][ ()][] }'
    ]
    for e in tests:
      self.assertEqual(ej1(e), 'SI', 'Falso Negativo')
    
  def testIncorrectos(self):
    tests = [
      '(',
      '(((',
      ')))',
      '[ )',
      ')]',
      '( )  [',
      '[ (   )',
      '[ (   [)]  ]',
      '{[() )](() ]()}',
      '({[( {[]}] })',
      '[][( ]{ }{}{}( )()()',
      '[{[( )(() ]}]',
      '{ [][() ][ ] ()][] }'
    ]
    for e in tests:
      self.assertEqual(ej1(e), 'NO', 'Falso Positivo')

if __name__ == '__main__':
    unittest.main()
