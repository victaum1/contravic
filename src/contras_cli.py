# -*- coding: UTF-8 -*-
import os.path as os_path
import sys
import crypty as cpt
import getpass as gpw

en_file = "scrambled"
de_file = "out_put"

def main():
  inlin = input("Input file name to process it: ")
  if os_path.isfile(inlin):
    opt = input("Do you want to encrypt or decrypt: ")
  else:
    raise SystemExit('File not found!')

  if opt == "e" or opt == "E":
    print("Encrypting file %s ---" % inlin)
    i_f = open(inlin)
    o_f = open(en_file+".txt","w")
    i_str = i_f.read()
    key = gpw.getpass("Enter passfrase: ")
    o_str = cpt.encrypt(key,i_str)
    o_f.write(o_str)
    o_f.close()
		
  else:
    if opt == "d" or opt == "D":
        print ("Decrypting file %s ---" % inlin)
        i_f = open(inlin)
        o_f = open(de_file+".txt","w")
        i_str = i_f.read()
        key = gpw.getpass("Enter passfrase: ")
        o_str = cpt.decrypt(key,i_str)
        o_f.write(o_str)
        o_f.close()
    else:
        print("Nothing to do")
	
  print("Done!")

if __name__ == "__main__":
    main()
