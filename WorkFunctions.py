import pickle
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def login(login, password, save):
    with open("users.bin", "rb") as file:
        data = pickle.load(file)
        print(data)
    hash = hashlib.sha256()
    hash.update(password.encode())
    print(password)
    isOk = False
    if login in data.keys() and data[login][0] == hash.hexdigest():
        isOk = True
    if isOk:
        with open("saved.bin", "wb") as file:
            if save:
                pickle.dump([save, login, password], file)
            else:
                pickle.dump([save, "", ""], file)
        return True
    return False

def checkRegister(login):
    with open("users.bin", "rb") as file:
        data = pickle.load(file)
    if login in data.keys():
        return False
    return True

def register(login, password, Name, SurName, Group, mother, pet, city): #todo all info group.upper
    with open("users.bin", "rb") as file:
        data = pickle.load(file)
    data[login] = list()
    hash0 = hashlib.sha256()
    hash0.update(password.encode())
    data[login].append(hash0.hexdigest())
    hash1 = hashlib.sha256()
    hash1.update(mother.encode())
    data[login].append(hash1.hexdigest())
    hash2 = hashlib.sha256()
    hash2.update(city.encode())
    data[login].append(hash2.hexdigest())
    hash3 = hashlib.sha256()
    hash3.update(pet.encode())
    data[login].append(hash3.hexdigest())

    with open("users.bin", "wb") as file:
        pickle.dump(data, file)

def isNumsLettersIn(text):
    text = text.lower()
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"
    digits = '0123456789'
    withDigits = False
    withLetters = False
    for i in letters:
        if i in text:
            withLetters = True
    for i in digits:
        if i in text:
            withDigits = True
    return withLetters and withDigits

def isCorrectAnswers(login, mother, city, pet):
    with open("users.bin", "rb") as file:
        data = pickle.load(file)
        print(data)
    isOk = True
    hash1 = hashlib.sha256()
    hash1.update(mother.encode())
    if data[login][1] != hash1.hexdigest():
        isOk = False
    hash2 = hashlib.sha256()
    hash2.update(city.encode())
    if data[login][2] != hash2.hexdigest():
        isOk = False
    hash3 = hashlib.sha256()
    hash3.update(pet.encode())
    if data[login][3] != hash3.hexdigest():
        isOk = False
    return isOk

def changePassword(login, password):
    with open("users.bin", "rb") as file:
        data = pickle.load(file)
    hash = hashlib.sha256()
    hash.update(password.encode())
    data[login][0] = hash.hexdigest()

    with open("users.bin", "wb") as file:
        pickle.dump(data, file)















if __name__ == "__main__":
    hash = hashlib.sha256()
    hash.update("sqrt(ab)".encode())
    with open("users.bin", "wb") as file:
        pickle.dump({"admin": [hash.hexdigest(),'Truller','It works','Здесь могла быть ваша реклама']}, file)

if __name__ == "__main__":
    hash = hashlib.sha256()
    hash.update("sqrt(ab)".encode())
    code = hash.hexdigest()
    key = RSA.generate(2048)

    encrypted_key = key.exportKey(
        passphrase=code,
        pkcs=8,
        protection="scryptAndAES128-CBC"
    )

    with open('private.bin', 'wb') as f:
        f.write(encrypted_key)

    with open('public.pem', 'wb') as f:
        f.write(key.publickey().exportKey())