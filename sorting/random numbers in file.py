import random
N = int(input("Введите кол-во элементов в массиве: "))
f = open("test.txt", "w+")
for i in range(N):
    num = random.randint(1,1000000)
    f.write(str(num) + '\n')
f.close()