def searchName(arr, search):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = arr[middle][0]
        if midpoint > search:
            end = middle - 1
        elif midpoint < search:
            start = middle + 1
        else:
            return middle


search = input("Введите фамилию: ")
f = open("output.txt", encoding='utf-8').readlines()
f1 = [line.split() for line in f]
result = searchName(f1, search)
if (result == None):
    print("Такой фамилии нет в списке")
else:
    print(f1[result][1])
