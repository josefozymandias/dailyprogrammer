import random

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
word = raw_input().lower()
new_word = ""
for letter in word:
	if letter == "c":
		new_word += random.choice(consonants)
	else:
		new_word += random.choice(vowels)
print new_word
