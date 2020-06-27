# coding utf-8
# testin main: contras_cli

import pytest
import sys
from crypty import encrypt, decrypt
import pdb

sys.path.append("../src")
import contras_cli as cli
from MyMock import MockInOut, MockOpen

def setup_open():
    MockOpen.args = []
    MockOpen.called = False
    MockOpen.read_called = False
    MockOpen.write_called = False
    MockOpen.close_called = False
    MockOpen.out_cads = []

def setup_InOut():
    MockInOut.outputs = []


@pytest.mark.happy
def test_usr_happy_path_1(inputs, out_fn, in_data, spec_out_es):
    setup_InOut()
    setup_open()

    m_input = MockInOut(inputs[0])

    cli.my_input = m_input.input
    cli.gpw.getpass = m_input.input
    cli.DB.read_prompt = m_input.input
    cli.my_print = MockInOut().print
    cli.open = MockOpen().open

    cli.main()

    assert MockInOut.outputs == spec_out_es[0]
    assert MockOpen.called == True 
    assert MockOpen.write_called == True
    assert MockOpen.close_called == True
    assert MockOpen.args[0] == (out_fn[0],'w+')
    assert MockOpen.out_cads[0] == in_data[1] 


#@pytest.mark.skip
@pytest.mark.happy
def test_usr_happy_path_2(inputs, in_data, out_fn, spec_out_es):
    setup_InOut()
    setup_open()

    pass_frase = inputs[1][4]
    
    m_input = MockInOut(inputs[1])
    m_print = MockInOut()
    m_open = MockOpen(in_data[1])

    cli.my_input = m_input.input
    cli.gpw.getpass = m_input.input
    cli.DB.read_prompt = m_input.input
    cli.my_print = m_print.print
    cli.open = m_open.open

    cli.main()

    assert MockOpen.called == True 
    assert MockOpen.write_called == True
    assert MockOpen.close_called == True
    assert MockOpen.args[0] == (out_fn[0],'r')
    assert MockOpen.args[1] == (out_fn[1],'w+')
    assert decrypt(pass_frase, MockOpen.out_cads[0]) == in_data[1]
    assert MockInOut.outputs == spec_out_es[1]
