def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n = n // 10
    return reversed_num

num = int(input("enter a num: "))
print(f"reversed: {reverse_number(num)}")
