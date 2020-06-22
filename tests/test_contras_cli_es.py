# coding utf-8
# testin main: contras_cli

import pytest
import sys
from MyMock import MockInOut, MockOpen
# import pdb

sys.path.append("../src")
import contras_cli as cli
from crypty import encrypt, decrypt

@pytest.mark.happy
def test_usr_happy_path_1(inputs, out_fn, out_db, spec_out_es):

    m_input = MockInOut(inputs)

    cli.input = m_input.input
    cli.gpw.getpass = m_input.input
    cli.DB.read_prompt = m_input.input
    cli.print = MockInOut().print
    cli.open = MockOpen().open


    cli.main()


    assert MockInOut.outputs == spec_out_es
    assert MockOpen.called == True 
    assert MockOpen.write_called == True
    assert MockOpen.close_called == True
    assert MockOpen.args[0] == (out_fn,'w+')
    assert MockOpen.out_cads[0] == out_db 

