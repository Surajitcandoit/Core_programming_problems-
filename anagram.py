
def check_anagram(a, b):
  a = sorted(a.strip().lower())                                      

  first = "".join(a)
  s = sorted(b.strip().lower())
  sec = "".join(s)
  if first == sec:                                         
    print("Two word have the same anagram.")
  else:
    print("Two word don't have the same anagram.")


a = input("Enter a word: ")
b = input("Enter another word: ")

if a.isalpha() and b.isalpha():
  check_anagram(a, b)

else:
  print("Please enter two real-world words containing only alphabets")
