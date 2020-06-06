import pytest

@pytest.fixture
def in_data():
    i_f = open("fixtures/input.yml")
    i_dat = i_f.read()
    i_f.close()
    return i_dat


@pytest.fixture
def out_data():
    o_f = open("./fixtures/out_put.txt")
    o_dat = o_f.read()
    o_f.close()
    return o_dat


@pytest.fixture
def key():
    k_f = open("./fixtures/some_key.txt")
    k_dat = k_f.read().rstrip('\n')
    k_f.close()
    return k_dat

@pytest.fixture
def iv():
    v_f = open("./fixtures/some_iv.txt")
    v_dat = v_f.read().rstrip('\n')
    v_f.close()
    return v_dat

