"""
Word occurrences
Estimate: 30 minutes
Actual: 27 minutes
"""

text = input("Text: ")
words = text.split()
word_to_number_of_word = {}
for word in words:
    if word not in word_to_number_of_word:
        word_to_number_of_word[word] = 1
    else:
        word_to_number_of_word[word] += 1
words_and_counts = list(word_to_number_of_word.items())
words_and_counts.sort()
longest_word_length = max((len(word) for word in word_to_number_of_word))
for word_and_count in words_and_counts:
    print(f"{word_and_count[0]:{longest_word_length}} : {word_and_count[1]}")
