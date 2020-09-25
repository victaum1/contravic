# 
"""
 Testing Crypty Module
"""

import pytest
import sys

sys.path.append("./src")

from crypty import encrypt, decrypt
"""
  Testing Encrypting - Decrypt
"""


@pytest.mark.crypt
def test_should_enc_be_aes(in_data, key, iv, out_data):
    assert out_data[0] == encrypt(key, in_data[0], iv)


@pytest.mark.crypt
def test_should_dec_be_aes(in_data, key, out_data):
    assert in_data[0] == decrypt(key, out_data[0])


@pytest.mark.crypt
def test_should_enc_and_dec_be_inverses(in_data, key):
    assert in_data[0] == decrypt(key, encrypt(key, in_data[0]))
