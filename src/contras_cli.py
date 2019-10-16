# -*- coding: UTF-8 -*-
# import os.path as os_path
# import sys
"""
Contras - cli
Managing a database of passwords
"""
import json
import getpass as gpw
import crypty as cpy

db_name = "db"


def create_user(name, password):
    new_user = {}
    new_user["Name"] = name
    new_user["PassWord"] = password
    return new_user


def create_users():
    users = []
    return users


def load_db(file_name=None, pass_frase=None):
    new_db = None
    if file_name is None:
        new_db = []
    else:
        if pass_frase is None:
            with open(file_name + ".json") as f:
                cad = f.read()
            new_db = json.loads(cad)
        else:
            with open(file_name + ".enc") as f:
                cad = f.read()
            new_db = json.loads(cpy.decrypt(pass_frase, cad))
    return new_db


def save_db(db, pass_frase=""):
    if pass_frase == "":
        o_f = open(db_name + ".json", "w")
        o_f.write(json.dumps(db)+"\n")
        o_f.close()
    else:
        o_f = open(db_name + ".enc", "w")
        out = json.dumps(db)+"\n"
        out = cpy.encrypt(pass_frase, out)
        o_f.write(out + "\n") 
        o_f.close()


def create_entry(account):
    new_entry = {}
    new_entry["Account"] = account
    new_entry["Users"] = []
    return new_entry


def account_add_usr(account, user):
    account["Users"].append(user)


def db_add_account(db, account):
    db.append(account)


def main():
    d_b = None
    opt = input("Crear nueva DB o cargarla? (N/C): ")

    if opt == "N":
        print("Creando nueva DB...")
        d_b = load_db()
        while True:
            print("Creando nueva entrada...")
            account = input("Nombre de la cuenta: ")
            account = create_entry(account)
            usr_name = input("Nombre de usuario: ")
            password = gpw.getpass("Contraseña: ")
            user = create_user(usr_name, password)
            account_add_usr(account, user)
            db_add_account(d_b, account)
            opt = input("Crear otra cuenta? (S/N): ")
            if opt == "N":
                break

    if opt == "C":
        db_name = input("Nombre de archivo para DB: ")
        d_b = load_db(db_name)
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
