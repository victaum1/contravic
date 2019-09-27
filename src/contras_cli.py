# -*- coding: UTF-8 -*-
#import os.path as os_path
#import sys
#import crypty as cpt
#import getpass as gpw

def create_user(name):
    new_user = {}
    return new_user

def create_users():
    users = []
    return users

def load_db(file_name=None, pass_frase=None):
    new_db = []
    return new_db

def save_db(db, pass_frase=""):
    pass

def create_entry(account=""):
    new_entry = {}
    return new_entry

def account_add_usr(account, user):
    #account["Users"].append(user)
    pass

def user_set_name(user, name):
    #user["Name"] = name
    pass

def user_set_psw(user, psw):
    #user["PassWord"]=psw
    pass

def main():
    db = None
    std_db = "db"
    db_encrypted =std_db+".enc"
    
    opt = input("Crear nueva DB o cargarla? (N/C): ")

    if (opt == "N"):
        print("Creando nueva DB...")
        db = load_db()
        print("Creando nueva entrada...") 
        account = input("Nombre de la cuenta: ")
        account = create_entry(account)
        usr_name = input("Nombre de usuario: ")
        user = create_user(usr_name)
        password  = input("Contraseña: ")
        password = user_set_psw(user, password)

    opt = input("Crear otra cuenta? (S/N): ")

    if (opt == "N"):
        opt = input("Encriptar DB? (S/N): ")
        if (opt == "N"):
            safe_db(data)
        else:
            # TODO
          pass
    else:
        # TODO
        pass
    pass

if __name__ == "__main__":
    main()
