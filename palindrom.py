def is_palindrome(s):
    string1 = s
    string2 = s[::-1]
    return string1 == string2

s = input("Enter the string: ")
result = is_palindrome(s)
if result:
    print("Is palindrome")
else:
    print("Not palindrome")
