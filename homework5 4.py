path = 'file.txt'
data = open(path, 'r')
for line in data:
    list = line
data.close

list2 = []

def split(s):
    return [char for char in s]

split(list)

j = 0
i = 0
print(f"long  {len(list)}")
while i < len(list) - 1 :
    count = 2
    if list[i] == list[i + 1]:
        k = i + 2
        while True:
            if list[i] == list[k]:
                count += 1
            else: break
            k += 1
            if k == len(list):
                break
    if count < 3:
        list2.append(list[i])
        if i == len(list) - 2:
            list2.append(list[i + 1 ])
    else:
        list2.append(f'{count}{list[i]}')
        i = k - 1
    i += 1
print(*list2)

strrr = ''
for item in list2:
    strrr += item
print(strrr)
