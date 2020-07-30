#crypt.py
import pyAesCrypt
import traceback
import os

def CryptFile(filePath,password,password2,bufferSize):

    try:
        path = filePath.get()
        pyAesCrypt.encryptFile(path, path+".aes", password, bufferSize)
        os.remove(path)
        return True
    except Exception as e:
        print(e)
        return False
