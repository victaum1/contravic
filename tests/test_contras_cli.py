# coding: utf-8
# testin main: contras_cli
import os
import os.path as path
import unittest
from unittest import TestCase, skip
from unittest.mock import patch, Mock, call
import sys

sys.path.append("../src")
import contras_cli as cli

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

    def test_user_happy_path_1(self):
        ins = [
              "N",
              "Cuenta 1",
              "Usuario 1",
              "Contra 1",
              "N",
              "N",
              ]
        ots = []
        spec_ots = [
              "Crear nueva DB o cargarla? (N/C): ",
              "Creando nueva DB...",
              "Creando nueva entrada...",
              "Nombre de la cuenta: ",
              "Nombre de usuario: ",
              "Contraseña: ",
              "Crear otra cuenta? (S/N): ",
              "Encriptar DB? (S/N): ",
              ]
        spec_ofile = "spec_db.json"
        ofile = "db.json"
        data = ""
        
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
        m_getpass = self.create_patch('getpass', obj=cli.gpw)
        m_getpass.side_effect = input_f

        cli.main()

        with open('fixtures/'+spec_ofile) as f:
            spec_data = f.read()

        if path.isfile(ofile):
          with open(ofile) as f:
              data = f.read()

        self.assertEqual(ots,spec_ots)
        self.assertEqual(spec_data, data)

    def tearDown(self):
        os.system("rm db.json")

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == "__main__":
    unittest.main()
