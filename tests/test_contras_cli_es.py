# coding utf-8
# testin main: contras_cli

import pytest
import sys
from crypty import encrypt, decrypt
# import pdb

sys.path.append("../src")
import contras_cli as cli


@pytest.mark.happy
def test_usr_happy_path_1(inputs, out_fn, out_db, spec_out_es):
    from MyMock import MockInOut, MockOpen
    m_input = MockInOut(inputs[0])

    cli.input = m_input.input
    cli.gpw.getpass = m_input.input
    cli.DB.read_prompt = m_input.input
    cli.print = MockInOut().print
    cli.open = MockOpen().open

    cli.main()

    assert MockInOut.outputs == spec_out_es[0]
    assert MockOpen.called == True 
    assert MockOpen.write_called == True
    assert MockOpen.close_called == True
    assert MockOpen.args[0] == (out_fn[0],'w+')
    assert MockOpen.out_cads[0] == out_db[0] 


# @pytest.mark.happy
@pytest.mark.skip
def test_usr_happy_path_2():
    from MyMock import MockInOut, MockOpen
    m_input = MockInOut()
    m_print = MockInOut()
    m_open = MockOpen()

    cli.input = m_input.input
    cli.gpw.getpass = m_input.input
    cli.DB.read_prompt = m_input.input
    cli.print = m_print.print
    cli.open = m_open.open

    cli.main()

    assert False

