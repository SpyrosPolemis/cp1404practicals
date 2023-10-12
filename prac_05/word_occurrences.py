"""
Word occurrences
Estimate: 30 minutes
Actual:
"""

text = input("Text: ")
words = text.split()
word_to_number_of_word = {}
for word in words:
    if word not in word_to_number_of_word:
        word_to_number_of_word[word] = 1
    else:
        word_to_number_of_word[word] += 1
for word, number_of_word in word_to_number_of_word.items():
    print(f"{word} : {number_of_word}")
