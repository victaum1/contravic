# coding: utf-8
# testing main: contras_cli
from unittest import main
from unittest import TestCase
from unittest.mock import patch, Mock
import sys
#import pdb


sys.path.append("../src")
import contras_cli as cli
from crypty import decrypt


# Testing cli
class TestMain(TestCase):

    def create_patch(self, name, obj=None):
        if obj is None:
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
              "N"]
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

        def input_f(val=None):
            ots.append(val)
            if len(ins) != 0:
                return ins.pop(0)
            return None

        def print_f(val='\n'):
            ots.append(val)
            return None

        with open('fixtures/'+spec_ofile) as f:
            spec_data = f.read()

        m_r_open = Mock()
        m_open = self.create_patch('open', obj=cli)
        m_open.side_effect = [m_r_open]
        m_input = self.create_patch('input', obj=cli)
        m_input.side_effect = input_f
        m_output = self.create_patch('print', obj=cli)
        m_output.side_effect = print_f
        m_getpass = self.create_patch('getpass', obj=cli.gpw)
        m_getpass.side_effect = input_f

        cli.main()

        self.assertEqual(ots, spec_ots)
        m_open.assert_called_with(ofile, 'w')
        m_r_open.write.assert_called_with(spec_data)
        m_r_open.close.assert_called()

    def test_user_happy_path_2(self):
        contra = "Contra 1"
        ins = [
            "C",
            "db",
            "S",
            "E",
            contra
              ]
        ots = []
        spec_ots = [
            "Crear nueva DB o cargarla? (N/C): ",
            "Nombre de archivo para DB: ",
            "- Cuenta 1",
            "- ...",
            "Extraer contra o salir? (E/S): ",
            "Encriptar DB? (S/N): ",
            "Contraseña: "
        ]
        spec_ifile = "spec_db.json"
        spec_ofile = "spec_db_enc.json"
        ifile = "db.json"
        ofile = "db_enc.json"

        def input_f(val=None):
            ots.append(val)
            if len(ins) != 0:
                return ins.pop(0)
            return None

        def print_f(val='\n'):
            ots.append(val)
            return None

        with open('fixtures/'+spec_ifile) as f:
            spec_idata = f.read()
        with open('fixtures/'+spec_ofile) as f:
            spec_odata = f.read()

        m_r_open = Mock()
        m_r_open.read.side_effect = [spec_idata]
        m_open = self.create_patch('open', obj=cli)
        m_open.return_value = m_r_open
        m_input = self.create_patch('input', obj=cli)
        m_input.side_effect = input_f
        m_output = self.create_patch('print', obj=cli)
        m_output.side_effect = print_f
        m_getpass = self.create_patch('getpass', obj=cli.gpw)
        m_getpass.side_effect = input_f

        cli.main()

        data = m_r_open.write.call_args.args
        data = decrypt(contra, data)
        spec_odata = decrypt(contra, spec_odata)

        m_open.assert_called_with(ifile)
        m_open.assert_called_with(ofile)
        self.assertEqual(ots, spec_ots)
        self.assertEqual(data, spec_odata)

    def test_user_happy_path_3(self):
        contra = "Contra 1"
        ins = [
            "C",
            "db_enc",
            contra,
            "E",
            "S"]
        ots = []
        spec_ots = [
            "Crear nueva DB o cargarla? (N/C): ",
            "La BD está encriptada.",
            "Contra para desbloquar: ",
            "- Cuenta 1 ...",
            "- ...",
            "Contra 1",
            "Continuar o salir (C/S): "]
        spec_ifile = "spec_db_enc.json"
        ifile = "db_enc.json"

        def input_f(val=None):
            ots.append(val)
            if len(ins) != 0:
                return ins.pop(0)
            return None

        def print_f(val='\n'):
            ots.append(val)
            return None

        with open('fixtures/'+spec_ifile) as f:
            spec_idata = f.read()

        m_r_open = Mock()

        m_r_open.read.side_effect = [spec_idata]
        m_open = self.create_patch('open', obj=cli)
        m_open.side_effect = [m_r_open]
        m_input = self.create_patch('input', obj=cli)
        m_input.side_effect = input_f
        m_output = self.create_patch('print', obj=cli)
        m_output.side_effect = print_f
        m_getpass = self.create_patch('getpass', obj=cli.gpw)
        m_getpass.side_effect = input_f

        cli.main()

        m_open.assert_called_with(ifile)
        m_r_open.read.assert_called()
        self.assertEqual(ots, spec_ots)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == "__main__":
    main()
