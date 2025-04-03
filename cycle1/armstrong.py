def is_armstrong(num):
    temp = num
    sum_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp = temp // 10
    return num == sum_cubes

# Test
n = int(input("Enter a number: "))
print(f"{n} is {'Armstrong' if is_armstrong(n) else 'not Armstrong'}.")

