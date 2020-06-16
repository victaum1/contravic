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

@pytest.fixture
def inputs():
    return [
            "N",
            '"Cuenta 1"',
            '"Usuario 1"',
            '"Contra 1"',
            "n",
            "n",
            "N",
            "N"
           ]

@pytest.fixture
def spec_out_es():
    return [
  "Crear nueva DB o cargarla? (N/C): ",
  "Creando nueva DB...",
  "Account?: ",
  "Users: ",
  "User?: ",
  "PassWord?: ",
  "Another [y/n]?: ",
  "Another [y/n]?: ",
  "Encriptar DB? (S/N): ",
              ]


@pytest.fixture
def out_fn():
    return "myDB.json"

@pytest.fixture
def out_db():
    i_f = open("fixtures/spec_db.json")
    i_dat = i_f.read()
    i_f.close()
    return i_dat


