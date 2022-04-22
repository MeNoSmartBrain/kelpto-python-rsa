import rsa

keyPair = rsa.newkeys(16)

publicKey = keyPair[0]
privateKey = keyPair[1]

print("P:", privateKey.p)
print("Q:", privateKey.q)
