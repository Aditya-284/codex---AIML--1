def palindrome(string):
    string = string.lower()
    reversed_string = string[::-1]
    return string == reversed_string
string = input("Enter a word: ")
if palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
