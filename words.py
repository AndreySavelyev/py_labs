# words count in input text
import sys
import operator

from collections import Counter # built-in solution for the same thing
input_text  = sys.stdin.read()

print('Counting words in input text...')
print(input_text)
print('---')

def wordcount(input_text):
    words_map = dict()

    for word in input_text.split():
        cleaned_word = word.strip('.,!-*\'').lower()
        if cleaned_word not in words_map:
            words_map[cleaned_word] = 0
        words_map[cleaned_word] += 1

    word_tuples = words_map.items()
    sorted_map = sorted(
        word_tuples, key=operator.itemgetter(1), reverse=True
    )
    return sorted_map

print(wordcount(input_text))