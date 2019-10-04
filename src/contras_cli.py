# -*- coding: UTF-8 -*-
#import os.path as os_path
#import sys
#import crypty as cpt
import getpass as gpw
import json

db_name = "db"
db_encrypted = db_name+".enc"

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
    if (file_name==None):
      new_db = []
    else:
        pass
    return new_db

def save_db(db, pass_frase=""):
    if pass_frase == "":
        of = open(db_name + ".json","w")
        of.write(json.dumps(db)+"\n")
        of.close()
    else:
      pass
    pass

def create_entry(account):
    new_entry = {}
    new_entry["Account"] = account
    new_entry["Users"] = []
    return new_entry

def account_add_usr(account, user):
    account["Users"].append(user)
    pass

def db_add_account(db, account):
    db.append(account)

def main():

    db = None
    
    opt = input("Crear nueva DB o cargarla? (N/C): ")

    if (opt == "N"):
        print("Creando nueva DB...")
        db = load_db()
        opt = "S"
        while True:
          print("Creando nueva entrada...") 
          account = input("Nombre de la cuenta: ")
          account = create_entry(account)
          usr_name = input("Nombre de usuario: ")
          password  = gpw.getpass("Contraseña: ")
          user = create_user(usr_name, password)
          account_add_usr(account,user)
          db_add_account(db, account)
          opt = input("Crear otra cuenta? (S/N): ")
          if opt != "S":
              break
          pass

    if (opt == "N"):
        opt = input("Encriptar DB? (S/N): ")
        if (opt == "N"):
            save_db(db)
        else:
            # TODO
          pass
    else:
        # TODO
        pass
    pass

if __name__ == "__main__":
    main()
