# coding: utf-8
# testin main: contras_cli


from unittest import TestCase, skip
from unittest.mock import patch
import sys

sys.path.append("../src")
import contras_cli as cli


# Testing cli
class TestMain(TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    @skip("Not ready")
    def test_input_file_found():
        pass

    def test_imput_file_not_found(self):
        patch_input = patch.object(cli,'input')
        patch_input.start()
        patch_isfile = patch('os.path.isfile',
          return_value=False)
        patch_isfile.start()
        self.assertRaises(SystemExit, cli.main)
        patch_isfile.stop()
        patch_input.stop()

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
        pass

    @classmethod
    def tearDownClass(self):
        pass
