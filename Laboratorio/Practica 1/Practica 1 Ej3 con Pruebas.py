"""
Practica 1 Ejercicio 3 con Pruebas Automáticas
Estudiante : Guido Luis Tapia Oré
Correo : guido.tapia@ucsp.edu.pe
Curso : Compiladores - CCOMP 8-1
"""
import unittest
import re

def ej3(txt):
    p = re.compile('(((m|M)e gustaría pedirle)|((l|L)e pido)|((s|S)olicito))[^\.]*\.')
    result = p.search(txt)
    if result:
        return result.group(0)
    else:
        return "NO"

class TestSolicitudChecker(unittest.TestCase):
  def testCorrectos(self):
    tests = [
        'Estimado profesor, recientemente he estado preocupado por muchos aspectos de su curso y eso ha ocasionado que no me concentre correctamente en sus clases. Si es que no apruebo su curso tendré problemas en casa porque solo tengo este curso y no trabajo. Por ese motivo, me gustaría pedirle más información sobre los temas recientemente tocados . Estaría muy agradecido y en verdad le deseo una bonita tarde. Hasta luego.',
        'Estimado profesor, recientemente he estado preocupado por muchos aspectos de su curso y eso ha ocasionado que no me concentre correctamente en sus clases. Si es que no apruebo su curso tendré problemas en casa porque solo tengo este curso y no trabajo. Por ese motivo, le pido más información sobre los temas recientemente tocados . Estaría muy agradecido y en verdad le deseo una bonita tarde. Hasta luego.',
        'Estimado profesor, recientemente he estado preocupado por muchos aspectos de su curso y eso ha ocasionado que no me concentre correctamente en sus clases. Si es que no apruebo su curso tendré problemas en casa porque solo tengo este curso y no trabajo. Por ese motivo, solicito más información sobre los temas recientemente tocados . Estaría muy agradecido y en verdad le deseo una bonita tarde. Hasta luego.'
    ]
    resp = [
        'me gustaría pedirle más información sobre los temas recientemente tocados .',
        'le pido más información sobre los temas recientemente tocados .',
        'solicito más información sobre los temas recientemente tocados .',
    ]
    for i in range(3):
      self.assertEqual(ej3(tests[i]), resp[i], 'Falso Negativo')
    
  def testIncorrectos(self):
    tests = [
      'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,',
      'Estimado profesor, recientemente he estado preocupado por muchos aspectos de su curso y eso ha ocasionado que no me concentre correctamente en sus clases. Por ese motivo, le exijo más información sobre los temas recientemente tocados . Estaría muy agradecido y en verdad le deseo una bonita tarde. Hasta luego.',
      'Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio mientras que mira su diseño.'
    ]
    for e in tests:
      self.assertEqual(ej3(e), 'NO', 'Falso Positivo')

if __name__ == '__main__':
    unittest.main()

