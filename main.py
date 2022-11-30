import string
import random
import hashlib
import secret
import threading

length = input("Enter password length: ")

access = False

passhash = hashlib.sha256(secret.password.encode()).hexdigest()
print("Hash for attempted password: " + passhash)

def search():
    access = True
    while not access:
        test = ''.join(random.choices(string.ascii_uppercase + string.digits, k=int(length)))
        if hashlib.sha256(test.encode()).hexdigest() == passhash:
            print("Target password: " + test)
            print("Target password hash: " + hashlib.sha256(test.encode()).hexdigest())
            access = True

def main():
    thread1 = threading.Thread(target=search())
    thread2 = threading.Thread(target=search())
    thread3 = threading.Thread(target=search())
    thread1.start()
    thread2.start()
    thread3.start()

if __name__ == "__main__":
    main()