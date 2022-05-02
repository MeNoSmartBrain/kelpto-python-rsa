import rsa


def print_private_key(key):
    print(str({
        'n': key.n,
        'e': key.e,
        'd': key.d,
        'p': key.p,
        'q': key.q,
    }))


keyPair = rsa.newkeys(64)

publicKey = keyPair[0]
privateKey = keyPair[1]

print("P:", privateKey.p)
print("Q:", privateKey.q)

print("Public-Key:", publicKey)
print_private_key(privateKey)


