"""
Порахувати скільки в рядку цілих чисел
"""

text=input("Введіть текст - ")
splited_text = text.split()
count = 0
for i in splited_text:
    if isinstance(i, int):
        count = count+1
print(count)