def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

f = open("test.txt", "r").readlines()
f = [line.rstrip() for line in f]
f1 = [int(item) for item in f]
bubble(f1)
output = open("output.txt", "w+")
for i in range(len(f1)):
    output.write(str(f1[i])+ "\n")
output.close()