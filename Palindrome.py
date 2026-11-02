
# Program to check palindrome

string = input("Enter a string: ")

if string == string[::-1]:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")
