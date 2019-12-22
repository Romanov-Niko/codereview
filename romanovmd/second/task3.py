"""
Дан рядок, вивести його задом наперед через одне слово
"""

def get_text(prompt):
  text = input(prompt)
  return text
def get_reverce():
  text = get_text("Введіть текст - ")
  newtext = text.split()
  return newtext[::-2]
print(get_reverce())
