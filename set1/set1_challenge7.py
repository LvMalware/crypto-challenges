import base64
from Crypto.Cipher import AES

def encryptText(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(text)

def decryptText(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(text)

def main():
    key  = "YELLOW SUBMARINE"
    file = open('7.txt', 'r')
    text = file.read()
    file.close()
    text = base64.b64decode(text)
    decr = decryptText(text, key)
    print (decr)
    return 0

if __name__ == '__main__':
    quit(main())
