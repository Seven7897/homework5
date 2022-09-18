# напишите программу удаляющую все слова из текста содержащие "абв"
text = 'мы неабв очень любим питон иабв джавуабв '.split()
text2 = 'абв'
list = []

for item in text:
    print(item)
    if not text2 in item :
        list.append(item)
print(*list)
