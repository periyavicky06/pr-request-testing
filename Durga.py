def is_palindrome(text):
  """
  Checks if a given string is a palindrome.

  Args:
    text: The string to be checked.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Convert the text to lowercase for case-insensitive comparison
  cleaned_text = text.lower()
  
  # Reverse the cleaned text
  reversed_text = cleaned_text[::-1]
  
  # Compare the original cleaned text with its reversed version
  return cleaned_text == reversed_text

# Test cases
print(f"'racecar' is a palindrome: {is_palindrome('racecar')}")
print(f"'Madam' is a palindrome: {is_palindrome('Madam')}")
print(f"'hello' is a palindrome: {is_palindrome('hello')}")
print(f"'A man, a plan, a canal: Panama' is a palindrome: {is_palindrome('A man, a plan, a canal: Panama')}")
