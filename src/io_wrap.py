#
"""
io_wrap
Wrapping input/output
"""

def my_print(cad):
    print(cad)


def my_input(prompt):
    result = input(prompt)
    return result


def my_open(_file, _mode="r"):
    handle = open(_file, _mode)
    return handle
