"""
Дан рядок, вивести його задом наперед через одне слово
"""

text = input("Введіть текст - ")
newtext = text.split(" ")
print(newtext[::-2])