"""
Порахувати кількість дробових чисел в списку
"""

import re

list = ["dfg", 1.4, 1.3, 6.6, "f", 8.7]
count = 0
for i in list:
    if re.match("^\d+.\d*[123456789]\d*$",str(i)):
        count = count + 1
print(count)
