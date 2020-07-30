#decrypt.py
import pyAesCrypt
import os

def DecryptFile(filePath,password,bufferSize):
    
    try:
        path = filePath.get()
        finalPath = path.replace(".aes","")
        pyAesCrypt.decryptFile(path, finalPath, password, bufferSize)
        os.remove(path)
        return True
    except:
        return False
