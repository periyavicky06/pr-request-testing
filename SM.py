# Get input from user
word = input("Enter a word: ")

# Check palindrome
if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
