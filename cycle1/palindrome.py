def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
    
word = input("enter a string: ")
print(f"'{word}' is {'a palindrome' if is_palindrome(word) else 'not a palindrome'}.")
