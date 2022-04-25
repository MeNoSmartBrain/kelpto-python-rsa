import typing

import rsa
from os.path import exists


if not exists("key"):
    absKey = rsa.key.PublicKey(143, 3)

    out_file = open("key", "wb")
    out_file.write(absKey._save_pkcs1_pem())

    out_file.close()

else:
    in_file = open("key", "rb")
    key = rsa.key.PublicKey._load_pkcs1_pem(in_file.read())

    print(key)

#
# keyPair = rsa.newkeys(16)
#
# publicKey = keyPair[0]
# privateKey = keyPair[1]
#
# print("P:", privateKey.p)
# print("Q:", privateKey.q)
