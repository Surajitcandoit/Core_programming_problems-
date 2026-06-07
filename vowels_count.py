
def count_vowel(s):
  vowels = ['a','e','i','o','u']
  count = 0

  clnd_s = "".join(ch.lower() for ch in s if ch.isalnum())
  for i in clnd_s:
    if i in vowels:
      count += 1
  return count

print(f"\n\t\t\tVowel Counter\n")

text = input("Enter your text: ")
result = count_vowel(text)

print(f"Your text contains {result} vowels.\n")
