
def is_palindrome(s):
  cleaned_s = "".join(char.lower() for char in s if char.isalnum())
  reversed = cleaned_s[::-1]
  if cleaned_s == reversed:
    return True
  else:
    return False

text = input("Enter your word/text: ").strip()

print("\nRESULT:")
if is_palindrome(text):
  print(f"Your text is a palindrome.\n")
else:
  print(f"Your text is not palindrome.\n")




