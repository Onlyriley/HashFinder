import string
import random
import hashlib
import threading
import time

# You can define a hardcoded password for demonstration purposes
password = "SECRET"
passhash = hashlib.sha256(password.encode()).hexdigest()
print("Hash for attempted password: " + passhash)

# Thread-safe flag to stop threads
access_event = threading.Event()

# Validate input length
while True:
    try:
        length = int(input("Enter password length: "))
        break
    except ValueError:
        print("Please enter a valid integer for password length.")

def search():
    start_time = time.perf_counter()
    while not access_event.is_set():
        test = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if hashlib.sha256(test.encode()).hexdigest() == passhash:
            end_time = time.perf_counter()
            print(f"✅ Target password found: {test}")
            print(f"🔑 Target password hash: {hashlib.sha256(test.encode()).hexdigest()}")
            print(f"⏱️ Time taken: {end_time - start_time:.2f} seconds")
            access_event.set()

def main():
    threads = [threading.Thread(target=search) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()  # Wait for all threads to finish

if __name__ == "__main__":
    main()
