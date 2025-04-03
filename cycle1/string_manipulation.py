def string_operations():
    print("String Manipulation Operations")

    # Input strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # a) String Concatenation
    concatenated = str1 + " " + str2
    print("\na) Concatenated String:", concatenated)

    # b) Reverse a String (using slicing)
    reversed_str1 = str1[::-1]
    print("b) Reversed First String:", reversed_str1)

    # c) String Slicing
    start = int(input("\nEnter start index for slicing (0-based): "))
    end = int(input("Enter end index for slicing: "))
    step = int(input("Enter step value (1 for normal, 2 for skipping every other, etc.): "))

    sliced_str = str1[start:end:step]
    print(f"c) Sliced String (from {start} to {end} with step {step}):", sliced_str)


if __name__ == "__main__":
    string_operations()
