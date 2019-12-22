"""
Порахувати кількість дробових чисел в списку
"""

list = ["dfg", 1.4, 1.3, 6.6, "f", 8.7]
count = 0
for i in list:
    if isinstance(i, float):
        count = count + 1
print(count)
