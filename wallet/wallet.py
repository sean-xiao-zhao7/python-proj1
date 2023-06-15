from Crypto.PublicKey import RSA
import Crypto.Random
import binascii


class Wallet:
    def __init__(self):
        pr_key = RSA.generate(1024, Crypto.Random.new().read)
        pub_key = pr_key.publickey()
        return (binascii.hexlify(pr_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(pub_key.exportKey(format='DER')).decode('ascii'))
