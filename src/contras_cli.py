# -*- coding: UTF-8 -*-
# import os.path as os_path
# import sys
"""
Contras - cli
Managing a database of passwords
"""
# import pdb # debug
import json
import getpass as gpw
import crypty as cpy
import MyDB as DB
from Db_template import customDB


db_name = "myDB"

def is_valid_input(inp):
    jval = '{ "val": ' + '['+inp+']' + ' }'
    try:
        json.loads(jval)
        return True
    except:
        return False


def yOrN(cad):
    if cad == "y":
        return True
    if cad == "n":
        return False
    return None


def dump(db):
    for record in db:
        for f in list(record):
            v = record[f]
            print("{}:  {}".format(f,v))
        print("\n")


def read_prompt(prompt=None):
    if prompt is None:
        read_prompt("continue/exit): ")
        return None
    else:
        val = input("{}?: ".format(prompt))
        return val

def check_input(key):
    while True:
        cad = read_prompt(key)
        if is_valid_input(cad):
            break
        else:
            print("Invalid input...")
    return cad


def read(db_temp=None):
    db=[]
    follow=True
    while follow:
        rd = read_record(db_temp[0])
        DB.add_record(rd,db)
        follow = read_prompt("Another [y/n]")
        follow = yOrN(follow)
    return db


def save(db,file_name=None):
    if file_name is None:
        Fd = open("myDB.json","w+")
        Fd.write(json.dumps(db)+"\n")
        Fd.close()
    else:
        Fd = open(file_name+".json","a+")
        Fd.write(json.dumps(db)+"\n")
        Fd.close()


def load(file_name=None):
    if file_name is None:
        Fd = open("myDB.json","r+")
        cad = Fd.read()
        db = json.loads(cad)
        Fd.close()
        return db
    else:
        Fd = open(file_name+".json","r+")
        db = Fd.read()
        db = json.loads(db)
        Fd.close()
        return db


def read_record(rd_temp=None):
    rd = {}
    if rd_temp is None:
        return rd 
    else:
        for key in rd_temp.keys():
            if type(rd_temp[key]) is type([]):
                print("{}: ".format(key))
                rd[key] = read(rd_temp[key])
            else:
                val = check_input(key)
                rd[key] = json.loads(val)   
    return rd


def new_db():
    n_db = read(customDB)
    return n_db


def load_db(file_name=None, pass_frase=None):
    new_db = None
    if pass_frase is None:
        new_db = load(file_name)
    else:
        f = open(file_name + "_enc.json")
        cad = f.read()
        f.close()
        new_db = json.loads(cpy.decrypt(pass_frase, cad))
    return new_db


def save_db(db,file_Name=None,pass_frase=None):
    if pass_frase is None:
        save(db,file_Name)
    else:
        o_f = open(db_name + "_enc.json", "w")
        out = json.dumps(db)+"\n"
        out = cpy.encrypt(pass_frase, out)
        o_f.write(out + "\n")
        o_f.close()

def main():
    d_b = None
    opt = input("Crear nueva DB o cargarla? (N/C): ")

    if opt == "N":
        print("Creando nueva DB...")
        d_b = new_db()

    if opt == "C":
        db_name = input("Nombre de archivo para DB: ")
        d_b = load_db(db_name)
        dump(d_b)
        opt = input("Extraer contra o salir? (E/S): ")
        if opt == "E":
            pass
        if opt == "S":
            pass

    opt = input("Encriptar DB? (S/N): ")

    if opt == "N":
        save_db(d_b)
    if opt == "S":
        pass_frase = gpw.getpass("Contraseña: ")
        save_db(d_b, pass_frase)


if __name__ == "__main__":
    main()

