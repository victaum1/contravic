# -*- coding: UTF-8 -*-
# Crypty module

import sys
import json
from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# Encrypting...
def encrypt(key,data,_iv = None):
  _key  = pad(bytes(key.encode('utf-8')), AES.block_size)
  _data = pad(bytes(data.encode('utf-8')), AES.block_size) 
  if _iv == None:
    cipher = AES.new(_key, AES.MODE_CBC)
  else:
    _iv = bytes(_iv.encode('utf-8'))
    cipher = AES.new(_key, AES.MODE_CBC, _iv)
  ct_bytes = cipher.encrypt(_data)
  iv = b64encode(cipher.iv).decode('utf-8')
  ct = b64encode(ct_bytes).decode('utf-8')
  result = json.dumps({'iv':iv, 'ciphertext':ct})
  return result

# Decrypting  
def decrypt(key,data):
  pt = ""
  try:
    _key  = pad(bytes(key.encode('utf-8')), AES.block_size)
    b64 = json.loads(data)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(_key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    pt = pt.decode('utf-8')
  except (Exception):
    print("Incorrect decryption")
    print (Exception.msg) 
  return pt

