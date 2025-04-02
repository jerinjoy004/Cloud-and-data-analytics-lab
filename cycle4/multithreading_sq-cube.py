import threading 
import time

def calculate_square(num):
    print(f"Calculating square of {num}")
    time.sleep(1)
    print(f"square of {num}: {num ** 2}")

def calculate_cube(num):
    print(f"Calculating cube of {num}")
    time.sleep(1)
    print(f"Cube of {num}: {num ** 3}")

if __name__ == "__main__":
    number = int(input("enter a number: "))
    
    thread1 = threading.Thread(target=calculate_square, args=(number,))
    thread2 = threading.Thread(target=calculate_cube, args=(number,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("finished")
