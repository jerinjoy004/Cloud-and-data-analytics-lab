import threading
import os

def display_info():
    print(f"Process ID: {os.getpid()}, Thread name: {threading.current_thread().name}")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        thread = threading.Thread(target=display_info, name=f"Thread-{i+1}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print("finished")
