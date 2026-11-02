
# Program to check palindrome

words = ["hello", "madam"]

for string in words:
    if string == string[::-1]:
        print(string, "is a Palindrome")
    else:
        print(string, "is not a Palindrome")