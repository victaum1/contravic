# coding: utf-8
# testin main: contras_cli
import unittest
from unittest import TestCase, skip
from unittest.mock import patch, Mock, call
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
      self.m_if = Mock()
      self.m_of = Mock()

    def setUp(self):
      pass

    def test_input_file_not_found(self):
        m_input = self.create_patch('input', obj=cli)
        m_input.side_effect = TestMain.input_f
        m_isfile = self.create_patch('os.path.isfile')
        m_isfile.return_value=False
        infile = "somefile.txt"
        self.inputs.append(infile)
        with self.assertRaises(SystemExit) as cm:
          cli.main()
        self.assertEqual("File not found!",str(cm.exception))
        m_isfile.assert_called_with(infile)
        self.assertEqual(self.outputs, ['Input file name to process it: '])
   
    @patch.object(cli,'open')
    @patch('os.path.isfile', return_value=True)
    @patch.object(cli,'input', side_effect = input_f)
    @patch.object(cli,'print', side_effect = print_f)
    def test_encrypting_ok(self, m_print, m_input, m_isfile, m_open):
        infile   = "somefile.txt"
        outfile  = "scrambled.txt"
        key      = "some key!"
        out_cont = "oooooooooooo"
        in_cont  = "iiiiiiiiiiii"
        self.m_if.read.return_value = in_cont
        self.inputs.append(infile)
        self.inputs.append("e")
        m_open.side_effect = [self.m_if, self.m_of]
        m_gpw = self.create_patch("getpass", obj=cli.gpw)
        m_gpw.return_value = key
        m_cpt = self.create_patch("encrypt", obj=cli.cpt)
        m_cpt.return_value = out_cont
        
        cli.main()
        
        self.assertEqual(self.outputs, ["Input file name to process it: ",
            "Do you want to encrypt or decrypt: ",
            "Encrypting file somefile.txt ---","Done!"])

        expected_calls = [call(infile), call(outfile,"w")]
        
        self.assertEqual(expected_calls, m_open.mock_calls)

        m_isfile.assert_called()
        self.m_if.read.assert_called()
        m_gpw.assert_called_with("Enter passfrase: ")
        m_cpt.assert_called_with(key,in_cont)
        self.m_of.write.assert_called_with(out_cont)
        self.m_of.close.assert_called()

    @patch('os.path.isfile', return_value=True)
    @patch.object(cli,"input", side_effect = input_f)
    @patch.object(cli,"print", side_effect = print_f)
    def test_decrypting_ok(self, m_print, m_input, m_isfile):
        infile   = "scrambled.txt"
        outfile  = "out_put.txt"
        key      = "some key!"
        out_cont = "iiiiiiiiiiii"
        in_cont  = "oooooooooooo"
        self.m_if.read.return_value = in_cont
        self.inputs.append(infile)
        self.inputs.append("d")
        m_open = self.create_patch("open", obj=cli)
        m_open.side_effect = [self.m_if, self.m_of]
        m_gpw = self.create_patch("getpass", obj=cli.gpw)
        m_gpw.return_value = key
        m_cpt = self.create_patch("decrypt", obj=cli.cpt)
        m_cpt.return_value = out_cont

        cli.main()

        self.assertEqual(self.outputs, ["Input file name to process it: ",
            "Do you want to encrypt or decrypt: ",
            "Decrypting file scrambled.txt ---","Done!"])

        expected_calls = [call(infile), call(outfile,"w")]
        self.assertEqual(expected_calls, m_open.mock_calls)

        m_isfile.assert_called()
        self.m_if.read.assert_called()
        
        m_gpw.assert_called_with("Enter passfrase: ")
        m_cpt.assert_called_with(key,in_cont)
        self.m_of.write.assert_called_with(out_cont)
        self.m_of.close.assert_called()

    @skip("Not ready")
    def test_en_or_de_crypting_not_ok():
        pass

    def tearDown(self):
        self.inputs.clear()
        self.outputs.clear()
        self.m_if.mock_reset()
        self.m_of.mock_reset()

    @classmethod
    def tearDownClass(self):
        pass

