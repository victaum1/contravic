# coding utf-8
# testin main: contras_cli

import pytest
import sys
# import pdb

sys.path.append("../src")
import contras_cli as cli
from crypty import encrypt, decrypt

@pytest.mark.happy
def test_usr_happy_path_1(inputs, out_fn, out_db, spec_out_es):
    outputs = []
    open_args = []
    open_was_called = [False]
    write_was_called = [False]
    close_was_called = [False]
    write_cads = []
    ocad=[]


    def mock_open(fileName,readMode=None):
        open_was_called.pop(0)
        open_was_called.append(True)

        def write(cad):
            write_was_called.pop(0)
            write_was_called.append(True)
            write_cads.append(cad)

        def close():
            close_was_called.pop(0)
            close_was_called.append(True)

        class FD:
            def write(self,cad):
                return write(cad)
            def close(self):
                return close()
        
        if readMode == None:
          open_args.append(fileName,"r")
          return FD()
        else:
          open_args.append((fileName,readMode))
          return FD()


    def mock_input(s):
        outputs.append(s)
        return inputs.pop(0)


    cli.input = mock_input
    cli.gpw.getpass = mock_input
    cli.DB.read_prompt = mock_input
    cli.print = lambda s : outputs.append(s)
    cli.open = mock_open


    cli.main()


    assert outputs == spec_out_es
    assert open_was_called[0] == True 
    assert write_was_called[0] == True
    assert close_was_called[0] == True
    assert open_args[0] == (out_fn,'w+')
    assert write_cads[0] == out_db 

