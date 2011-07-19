'''Unittest for saving and loading keys.'''

import base64
import unittest

import rsa.key

B64PRIV_DER = 'MC4CAQACBQDeKYlRAgMBAAECBQDHn4npAgMA/icCAwDfxwIDANcXAgInbwIDAMZt'
PRIVATE_DER = base64.decodestring(B64PRIV_DER)

PRIVATE_PEM = '''
-----BEGIN CONFUSING STUFF-----
Cruft before the key

-----BEGIN RSA PRIVATE KEY-----
%s
-----END RSA PRIVATE KEY-----

Stuff after the key
-----END CONFUSING STUFF-----
''' % B64PRIV_DER

CLEAN_PRIVATE_PEM = '''\
-----BEGIN RSA PRIVATE KEY-----
%s
-----END RSA PRIVATE KEY-----
''' % B64PRIV_DER


class DerTest(unittest.TestCase):
    '''Test saving and loading DER keys.'''

    def test_load_private_key(self):
        '''Test loading private DER keys.'''

        key = rsa.key.load_private_key_der(PRIVATE_DER)
        expected = rsa.key.PrivateKey(3727264081, 65537, 3349121513, 65063, 57287)

        self.assertEqual(expected, key)

    def test_save_private_key(self):
        '''Test saving private DER keys.'''

        key = rsa.key.PrivateKey(3727264081, 65537, 3349121513, 65063, 57287)
        der = rsa.key.save_private_key_der(key)

        self.assertEqual(PRIVATE_DER, der)

class PemTest(unittest.TestCase):
    '''Test saving and loading PEM keys.'''


    def test_load_private_key(self):
        '''Test loading private PEM files.'''

        key = rsa.key.load_private_key_pem(PRIVATE_PEM)
        expected = rsa.key.PrivateKey(3727264081, 65537, 3349121513, 65063, 57287)

        self.assertEqual(expected, key)

    def test_save_private_key(self):
        '''Test saving private PEM files.'''

        key = rsa.key.PrivateKey(3727264081, 65537, 3349121513, 65063, 57287)
        pem = rsa.key.save_private_key_pem(key)

        self.assertEqual(CLEAN_PRIVATE_PEM, pem)
