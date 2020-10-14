#
# testin main: contras_cli

import pytest
import sys
import pdb

sys.path.append("./src")
from crypty import encrypt, decrypt
import io_wrap
import contras_cli as cli

@pytest.mark.happy
def test_usr_happy_path_1(mocker, inputs, out_fn, spec_out_es,
        out_data):
    t_inputs = inputs[0]
    t_outputs = []

    def m_input(s):
        t_outputs.append(s)
        return t_inputs.pop(0)

    def m_print(s):
        t_outputs.append(s)

    mocker.patch.object(cli,'my_input', side_effect=m_input)
    mocker.patch.object(cli.gpw,'getpass', side_effect=m_input)
    mocker.patch.object(cli,'my_print', side_effect=m_print)
    m_open = mocker.mock_open()
    mocker.patch.object(cli,'my_open', m_open)

    cli.main()

    m_open.assert_called_once_with(out_fn[0],'w+')
    assert t_outputs == spec_out_es[0]
    handle = m_open()
    handle.close.assert_called_once()
    handle.write.assert_called_with(out_data[2])

@pytest.mark.happy
def test_usr_happy_path_2(mocker, inputs, in_data, out_data,
        out_fn, spec_out_es):
    call = mocker.call
    t_inputs = inputs[1]
    pass_frase = inputs[1][4]
    t_outputs = []

    def m_input(s):
        t_outputs.append(s)
        return t_inputs.pop(0)

    def m_print(s):
        t_outputs.append(s)

    mocker.patch.object(cli,'my_input', side_effect=m_input)
    mocker.patch.object(cli.gpw,'getpass', side_effect=m_input)
    mocker.patch.object(cli,'my_print', side_effect=m_print)
    m_open = mocker.mock_open(read_data=in_data[1])
    mocker.patch.object(cli,'my_open', m_open)

    cli.main()

    assert t_outputs == spec_out_es[1]
    calls = [call(out_fn[0]), call(out_fn[1],'w+')]
    m_open.assert_has_calls(calls,any_order=True)
    handle = m_open()
    (_arg, ) = handle.write.call_args[0]
    assert decrypt(pass_frase, _arg) == in_data[1]
