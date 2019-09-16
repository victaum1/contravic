# coding: utf-8
# testin main: contras_cli

from unittest import TestCase, skip
from unittest.mock import patch, Mock
import sys

sys.path.append("../src")
import contras_cli as cli

# Testing cli
class TestMain(TestCase):
    inputs = []
    outputs = []

    def input_f(val=''):
      ins = TestMain.inputs
      ots = TestMain.outputs
      ots.append(val)
      if len(ins) != 0:
        return ins.pop(0)
      return None

    def print_f(val=''):
      TestMain.outputs.append(val)
      return None

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
      self.inputs = TestMain.inputs
      self.outputs = TestMain.outputs

    def setUp(self):
        pass

    @patch.object(cli,'input', side_effect = input_f)
    @patch('os.path.isfile', return_value=False)
    def test_input_file_not_found(self, mock_isfile, mock_input):
        infile = "somefile.txt"
        self.inputs.append(infile)
        self.inputs.append('')
        with self.assertRaises(SystemExit) as cm:
          cli.main()
        self.assertEqual("File not found!",str(cm.exception))
        mock_isfile.assert_called_with(infile)
        self.assertEqual(self.outputs, ['Input file name to process it: ',
            ''])
    
    @patch("builtins.input", side_effect = input_f)
    @patch("builtins.print", side_effect = print_f)
    def test_encrypting_ok(self, m_print, m_input):
        infile   = "somefile.txt"
        outfile  = "scrambled.txt"
        key      = "some key!"
        out_cont = "oooooooooooo"
        in_cont  = "iiiiiiiiiiii"
        i_f = Mock()
        i_f.read.return_value = in_cont
        o_f = Mock()
        self.inputs.append(infile)
        self.inputs.append("e")
        m_open = self.create_patch("open", obj=cli)
        m_open.side_efect = [i_f, o_f]
        m_gpw = self.create_patch("gpw.getpass", obj=cli)
        m_gpw.return_value = key
        m_cpt = self.create_patch("cpt.encrypt", obj=cli)
        m_cpt.return_value = out_cont

        cli.main()

        self.assertEqual(self.outputs, ["Input file name to process it: ",
            "Do you want to encrypt or decrypt: ",
            "Encrypting file somefile.txt ---","Done!"])

        m_open.assert_called_with(infile,"r")
        m_open.assert_called_with(outfile+".txt","wb")
        i_f.read.assert_called()
        m_gpw.getpasss.assert_called_with("Enter passfrase: ")
        m_cpt.encrypt.assert_called_with(key,in_cont)
        o_f.write.assert_called_with(out_cont)
        o_f.close.assert_called()

    @patch("builtins.input", side_effect = input_f)
    @patch("builtins.print", side_effect = print_f)
    def test_decrypting_ok(self, m_print, m_input):
        infile   = "scrambled.txt"
        outfile  = "out_put.txt"
        key      = "some key!"
        out_cont = "iiiiiiiiiiii"
        in_cont  = "oooooooooooo"
        i_f = Mock()
        i_f.read.return_value = in_cont
        o_f = Mock()
        self.inputs.append(infile)
        self.inputs.append("d")
        m_open = self.create_patch("open", obj=cli)
        m_open.side_efect = [i_f, o_f]
        m_gpw = self.create_patch("gpw.getpass", obj=cli)
        m_gpw.return_value = key
        m_cpt = self.create_patch("cpt.decrypt", obj=cli)
        m_cpt.return_value = out_cont

        cli.main()

        self.assertEqual(self.outputs, ["Input file name to process it: ",
            "Do you want to encrypt or decrypt: ",
            "Decrypting file scrambled.txt ---","Done!"])

        m_open.assert_called_with(infile,"r")
        m_open.assert_called_with(outfile,"wb")
        i_f.read.assert_called()
        m_gpw.getpasss.assert_called_with("Enter passfrase: ")
        m_cpt.encrypt.assert_called_with(key,in_cont)
        o_f.write.assert_called_with(out_cont)
        o_f.close.assert_called()

    @skip("Not ready")
    def test_en_or_de_crypting_not_ok():
        pass

    def tearDown(self):
        self.inputs.clear()
        self.outputs.clear()

    @classmethod
    def tearDownClass(self):
        pass
