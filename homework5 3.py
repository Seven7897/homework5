N = 3
M = 3
A = []
for i in range(N):
    A.append([0]*M) 
for i in range(N):
    for j in range(M):
        A[i][j] = '-'

def user_clic_rows():
    try:
        while True:
            rows = int(input("Задайте строку : ")) - 1
            if -1 < rows < N :
                break
            else:
                print("вы ввели число меньше 1 или больше 3 ")
        return rows
    except:
            print("Введите пожалуйста число !")

def user_clic_colums():
    try:
        while True:
            colums = int(input("Задайте столбец : ")) - 1
            if -1 < colums < M :
                break
            else:
                print("вы ввели число меньше 1 или больше 3 ")
        return colums
    except:
            print("Введите пожалуйста число !")

def proverka_na_pobedu():
    if A[rows][colums] == A[0][0] and A[rows][colums] == A[0][1] and A[rows][colums] == A[0][2]:
        return True
    if A[rows][colums] == A[1][0] and A[rows][colums] == A[1][1] and A[rows][colums] == A[1][2]:
        return True
    if A[rows][colums] == A[2][0] and A[rows][colums] == A[2][1] and A[rows][colums] == A[2][2]:
        return True
    if A[rows][colums] == A[0][0] and A[rows][colums] == A[1][0] and A[rows][colums] == A[2][0]:
        return True
    if A[rows][colums] == A[0][1] and A[rows][colums] == A[1][1] and A[rows][colums] == A[2][1]:
        return True
    if A[rows][colums] == A[0][2] and A[rows][colums] == A[1][2] and A[rows][colums] == A[1][2]:
        return True
    if A[rows][colums] == A[0][0] and A[rows][colums] == A[1][1] and A[rows][colums] == A[2][2]:
        return True
    if A[rows][colums] == A[0][2] and A[rows][colums] == A[1][1] and A[rows][colums] == A[2][0]:
        return True

lot = int(input("Какой игрок начинает  1 или 2 ? :  "))
while True:
    if lot == 1 :
        print('Ходит игрок 1 ')
        try:
            while True:
                rows = user_clic_rows()
                colums = user_clic_colums()
                if A[rows][colums] != 'X' and A[rows][colums] != 'O':
                    break
                else:
                    print("Позиция занята")
        except:
            print("Позиция занята ")
        A[rows][colums] = 'X'
        proverka = proverka_na_pobedu()
        if proverka == True:
            break
        print(*A[0])
        print(*A[1])
        print(*A[2])
        lot = 2
    else:
        print('Ходит игрок 2 ')
        try:
            while True:
                rows = user_clic_rows()
                colums = user_clic_colums()
                if A[rows][colums] != 'X' and A[rows][colums] != 'O':
                    break
                else :
                    print("Позиция занята ")
        except:
            print("Позиция занята ")
        A[rows][colums] = 'O'
        proverka = proverka_na_pobedu()
        if proverka == True:
            break
        print(*A[0])
        print(*A[1])
        print(*A[2])
        lot = 1
print(f"Победил игрок {lot} . Поздравляем !!!")
print(f"Итоговая табличка выглядит следующим образом : ")
print(*A[0])
print(*A[1])
print(*A[2])
