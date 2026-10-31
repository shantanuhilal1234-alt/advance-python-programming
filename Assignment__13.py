import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1 - Number: {i}")
        time.sleep(1)

def print_alphabets():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Thread 2 - Alphabet: {ch}")
        time.sleep(1)

def display_messages():
    messages = ["Hello", "Welcome", "Python", "Multithreading", "Complete"]
    for msg in messages:
        print(f"Thread 3 - Message: {msg}")
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=display_messages)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("\nAll threads have completed execution.")
