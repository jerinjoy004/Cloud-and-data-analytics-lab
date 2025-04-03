def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test
text = input("Enter a string: ")
print(f"Vowel count: {count_vowels(text)}")
