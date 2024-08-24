import re
from collections import Counter

def count_words_in_file(filename):

    with open(filename,'r') as file:
        text=file.read().lower()

    words=re.findall(r'\b\w+\b',text)

    word_count=Counter(words)

    for word in sorted(word_count):
        print(f"{word}:{word_count[word]}")

filename='Genai_001.txt'
count_words_in_file(filename)