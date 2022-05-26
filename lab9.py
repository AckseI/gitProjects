def searchName(f, search):
    if search in f:
        return f

search = input("Введите фамилию: ")
f = open("baza tel numbers.txt", encoding='utf-8').readlines()
f = [line.split() for line in f]
f.sort()
index = searchName(f, search)
print(f[index][1])