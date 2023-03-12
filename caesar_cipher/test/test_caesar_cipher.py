#!/usr/bin/python3
import unittest
from caesar_cipher import encrypt

class Test(unittest.TestCase):
    def test_encrypt(self):
        KEY = 12
        plaintext = "This is a test in 2023, {checked}"
        ciphertext = "`tu ,u ,m,!q !,uz,><>?8,(otqowqp*"

        self.assertEqual(encrypt(plaintext, KEY), ciphertext)
        self.assertEqual(encrypt(ciphertext, -KEY), plaintext)