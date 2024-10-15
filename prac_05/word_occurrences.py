"""
Word Occurrences
Estimate: 15 minutes
Actual:   20 minutes
"""

from operator import itemgetter

text = input("Text: ")
word_to_count = {}

for word in text.split(" "):
    word_to_count[word] = word_to_count.get(word, 0) + 1

width = max(len(word) for word in word_to_count.keys())

for word, count in sorted(word_to_count.items(), key=itemgetter(1), reverse=True):
    print(f"{word:{width}} = {word_to_count[word]}")
