# coding: utf-8

"""
 Testing Crypty Module
"""

import pytest
import sys

sys.path.append("../src")

from crypty import encrypt, decrypt


"""
  Testing Encrypting - Decrypt
"""

def test_should_enc_be_aes(in_data, key, iv, out_data):
    assert out_data == encrypt(key,in_data,iv)

def test_should_dec_be_aes(in_data, key, out_data):
    assert in_data == decrypt(key,out_data)
    

def test_should_enc_and_dec_be_inverses(in_data, key):
    assert in_data == decrypt(key,encrypt(key,in_data))

