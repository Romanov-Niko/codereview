"""
Порахувати кількість чисел в рядку
"""

text=input("Введіть текст - ")
count=0
for i in text:
    if i in "0123456789":
        count = count+1
print(count)
