def searchName(f, search):
    l = 0
    r = len(f) - 1
    while (l<=r):
        mid = (l + r) // 2
        res = (search == f[mid])
        print(res)
        if (res == 0):
            return mid - 1
        if (res > 0):
            l = mid + 1
        else:
            r = mid - 1
    return None

search = input("Введите фамилию: ")
f = open("baza tel numbers.txt", encoding='utf-8').readlines()
f1 = [line.split() for line in f]
f1.sort()
result = searchName(f1, search)
if (result == None):
    print("Такой фамилии нет в списке")
else:
    print(f1[result])