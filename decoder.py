from itertools import product
from Crypto.Cipher import AES

chars = 'abcdef0123456789'

sufix_keyhex = 'b4635e3d7d5ac56b286617d3c4f76ff02a278d7c9436bcbe069ea6dd'
ivhex = '8b3ed971287585333b2f3580e08ec02f'
iv = ivhex.decode("hex")

secret = 'ntfV2ULZYRiIEotYV+lsSVQ6+Wp7/UH6ebDrBYpW3JbUvKKswA/vi+5TXnFk1xHheh4d1MEg8n05FZr7AhvMl9hwBfmqKYvP4RRlzaJrAdB4MUN2fHWW/zgb72E7BucG'.decode(
    "base64")


def isprintable(s, codec='utf8'):
    try:
        s.decode(codec)
    except UnicodeDecodeError:
        return False
    else:
        return True


def find_message(missing_key_chars):
    for achar in product(chars, repeat=missing_key_chars):
        keyhex = ''.join(achar) + sufix_keyhex

        if (isprintable(AES.new(keyhex.decode("hex"), AES.MODE_CBC, iv).decrypt(secret))):
            print ("message: " + AES.new(keyhex.decode("hex"), AES.MODE_CBC, iv).decrypt(
                secret) + "\n" "key: " + keyhex.decode("hex").encode("hex"))
            break


find_message(8)  # find_message(missing_key_chars)

