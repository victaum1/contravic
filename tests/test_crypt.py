# coding: utf-8
# testin Crypty Module

#from mockito import mock, verify
import unittest
import sys
# import json

sys.path.append("../src")

from crypty import encrypt, decrypt

# Testing Encrypting - Decrypt...
class TestCrypto(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        k_f  = open("./fixtures/some_key.txt","r")
        i_f  = open("./fixtures/in_put.yml","r")
        o_f  = open("./fixtures/out_put.txt","r")
        iv_f = open("./fixtures/some_iv.txt","r")
        self.key_val  = k_f.read()
        k_f.close()
        self.in_data  = i_f.read()
        i_f.close()
        self.out_data = o_f.read()
        o_f.close()
        self.iv_val = iv_f.read()
        iv_f.close()

    def test_should_enc_and_dec_be_inverses(self):
        self.assertEqual(self.in_data,decrypt(self.key_val,
          encrypt(self.key_val,self.in_data)))

    def test_should_enc_be_aes(self):
        in_dat = self.in_data
        ou_dat = self.out_data
        _key   = self.key_val
        _iv    = self.iv_val
        self.assertEqual(ou_dat,encrypt(_key,in_dat,_iv)) 

    def test_should_dec_be_aes(self):
        in_dat = self.in_data
        ou_dat = self.out_data
        _key   = self.key_val
        self.assertEqual(in_dat,decrypt(_key,ou_dat)) 
        
