# coding: utf-8
# testin main: contras_cli

from unittest import TestCase, skip
from unittest.mock import patch
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
      if len(ots) != 0:
        return ins.pop(0)
      return None

#      def print_f(val=''):
#        TestMain.outputs.append(val)
#        return None

    @classmethod
    def setUpClass(self):
      self.inputs = TestMain.inputs
      self.outputs = TestMain.outputs

    def setUp(self):
        pass

    @skip("Not ready")
    def test_input_file_found():
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
    
    @skip("Not ready")
    def test_encrypting_ok():
        pass
    @skip("Not ready")
    def test_decrypting_ok():
        pass
    @skip("Not ready")
    def test_en_or_de_crypting_not_ok():
        pass

    def tearDown(self):
        self.inputs.clear()
        self.outputs.clear()


    @classmethod
    def tearDownClass(self):
        pass
