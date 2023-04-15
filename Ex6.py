word = input("Enter string:")
wordy = []

for letter in word:
    wordy.append(letter)

ydrow = wordy[::-1]

if wordy == ydrow:
    print(word + " is a palindrome")
else:
    print(False)
