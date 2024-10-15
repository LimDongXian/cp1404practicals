"""
Word Occurrences
Estimate: 15 minutes
Actual:   32 minutes
"""

text = input("Text: ")
word_to_count = {}

for word in text.split(" "):
    word_to_count[word] = word_to_count.get(word, 0) + 1
    width = max(len(word) for word in word_to_count.keys())
    print(f"{word:{width}} = {word_to_count[word]}")
