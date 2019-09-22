# coding: utf-8
# testin main: contras_cli
import unittest
from unittest import TestCase, skip
from unittest.mock import patch, Mock, call
import sys

sys.path.append("../src")
import contras_cli as cli

#ins = []
#ots = []

# Testing cli
class TestMain(TestCase):

    def create_patch(self, name, obj=None):
      if obj == None:
        patcher = patch(name)
      else:
        patcher = patch.object(obj, name)
      thing = patcher.start()
      self.addCleanup(patcher.stop)
      return thing

    @classmethod
    def setUpClass(self):
      pass

    def setUp(self):
      pass

    def test_user_history_1(self):
      ins = [
              "C",
              "Cuenta 1"
              "Usuario 1",
              "Contra 1",
              "S",
              "N",
              ]
      ots = []
      spec_ots = [
              "Crear nueva DB o cargarla?: ",
              "Nombre de la cuenta: ",
              "Nombre de usuario: ",
              "Contraseña: ",
              "Nueva cuenta y/o usuario?: ",
              "Encryptar DB?: ",
              ]

      spec_ofile = "db.json"
      
      def input_f(val=None):
        ots.append(val)
        if len(ins) != 0:
          return ins.pop(0)
        return None

      def print_f(val='\n'):
        ots.append(val)
        return None

      m_input = self.create_patch('input',obj=cli)
      m_input.side_effect = input_f
      m_output = self.create_patch('print',obj=cli)
      m_output.side_effect = print_f

      cli.main()

      self.assertEqual(ots,spec_ots) 
      self.assertEqual(open(spec_ofile).read(),open('fixtures/'+spec_ofile)
        .read())

    def tearDown(self):
      pass

    @classmethod
    def tearDownClass(self):
        pass

