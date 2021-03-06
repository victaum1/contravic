#
import pytest

@pytest.fixture
def in_data():
    i_dat = []
    with open("tests/fixtures/input.yml") as f:
        i_dat.append(f.read())
    with open("tests/fixtures/spec_db.json") as f:
        i_dat.append(f.read())
    return i_dat


@pytest.fixture
def out_data():
    o_dat = []
    with open("tests/fixtures/out_put.txt") as f:
        o_dat.append(f.read())
    with open("tests/fixtures/spec_db_enc.json") as f:
        o_dat.append(f.read())
    with open("tests/fixtures/spec_db.json") as f:
        o_dat.append(f.read())
    return o_dat


@pytest.fixture
def key():
    with open("tests/fixtures/some_key.txt") as f:
        k_dat = f.read().rstrip('\n')
    return k_dat

@pytest.fixture
def iv():
    with open("tests/fixtures/some_iv.txt") as f:
        v_dat = f.read().rstrip('\n')
    return v_dat

@pytest.fixture
def inputs():
    return [[
            "N",
            '"Cuenta 1"',
            '"Usuario 1"',
            '"Contra 1"',
            "n",
            "n",
            "N",
            "N"
           ],
           [
            "C",
            "miDB",
            "S",
            "S",
            "Contra 1"
           ]
           ]

@pytest.fixture
def spec_out_es():
    return [[
  "¿Crear nueva DB o cargarla? (N/C): ",
  "Creando nueva DB...",
  "Account?: ",
  "Users: ",
  "User?: ",
  "PassWord?: ",
  "¿Otro [s/n]?: ",
  "¿Otro [s/n]?: ",
  "¿Encriptar DB? (S/N): ",
           ],
           [
  "¿Crear nueva DB o cargarla? (N/C): ",
  "Nombre de archivo para DB: ",
  "Account:  Cuenta 1",
  "Users:  [{'User': 'Usuario 1', 'PassWord': 'Contra 1'}]",
  "\n",
  "¿Extraer contra o salir? (E/S): ",
    "¿Encriptar DB? (S/N): ",
  "Contraseña: "
            ],[],[]]


@pytest.fixture
def out_fn():
    return [
            "miDB.json",
            "miDB_enc.json"
            ]

