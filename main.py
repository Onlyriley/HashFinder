import string
import random
import hashlib
import secret
import threading
import time

length = input("Enter password length: ")

access = False

passhash = hashlib.sha256(secret.password.encode()).hexdigest()
print("Hash for attempted password: " + passhash)

def search():
    global access
    access = False
    start_time = time.perf_counter()
    while not access:
        test = ''.join(random.choices(string.ascii_uppercase + string.digits, k=int(length)))
        if hashlib.sha256(test.encode()).hexdigest() == passhash:
            end_time = time.perf_counter()
            print("Target password: " + test)
            print("Target password hash: " + hashlib.sha256(test.encode()).hexdigest())
            print(f"Target found in {end_time - start_time} seconds")
            access = True

def main():
    thread1 = threading.Thread(target=search)
    thread2 = threading.Thread(target=search)
    thread3 = threading.Thread(target=search)
    thread1.start()
    thread2.start()
    thread3.start()
    if access == True:
        quit()

if __name__ == "__main__":
    main()