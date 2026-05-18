palindrome = lambda s: s == s[::-1]
text = input("Enter a string: ")
if palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")