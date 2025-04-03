def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# Test
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Largest number: {find_max(numbers)}")
