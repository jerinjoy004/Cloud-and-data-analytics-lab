import threading

def write_characters(content):
    with open("output1.txt", "w") as f1:
        for char in content:
            if char.isalpha():
                f1.write(char)
    print("Thread 1: char written")

     
def write_numbers(content):
	with open("output2.txt", "w") as f2:
		for char in content:
			if char.isdigit():
				f2.write(char)
	print("thread 2: digit written")
	
def write_special(content):
	with open("output3.txt", "w") as f3:
		for char in content:
			if not char.isalnum():
				f3.write(char)
	print("thread 3: special written")
	
if __name__ == "__main__":
	with open("input.txt", "r") as file:
		content = file.read()
	
	thread1 = threading.Thread(target=write_characters, args=(content,)) 
	thread2 = threading.Thread(target=write_numbers, args=(content,)) 
	thread3 = threading.Thread(target=write_special, args=(content,)) 
	
	thread1.start()
	thread2.start()
	thread3.start()
	
	thread1.join()
	thread2.join()
	thread3.join()
	
	print("all complete")
