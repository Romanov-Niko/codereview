"""
Дан рядок тексту, у якому можуть бути будь-які розділові знаки.
Вивести цей рядок, якщо у ньому є слова, що повторюються, то вивести таке слово лише один раз. Наприклад:
input: Hey, hey, Eliza.
output: [Hey, Eliza]
"""

import re

def get_splitted_text(text):
    return re.split('[ ,.:;!?-]+', text)

def find_most_frequent():
    text = input("Введіть текст: ")
    lowertext = []
    count = 0
    for word in get_splitted_text(text):
        lowertext.append(word[0].lower()+word[1:])
    for i in lowertext:
        for j in lowertext:
            if i == j:
                count = count + 1
            if count > 1:
                lowertext.remove(i)
    return lowertext

print(find_most_frequent())
