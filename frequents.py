
def count_frequent(s):
  freq = {}
  clnd = "".join(ch.lower() for ch in s if ch.isalpha())

  for i in clnd:
    if i in freq:
      freq[i] = freq.get(i, 0) + 1
    else:
      freq[i] = 1
  return freq

print(f"\n\t\t\tFrequency Counter")
print(f"__________" * 6, "\n")
text = input("Enter your text: ")

freq = count_frequent(text)
sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

for k, v in sorted_freq.items():
  print(f"{k}: {v}")
