def selection_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

f = open("test.txt", "r").readlines()
f = [line.rstrip() for line in f]
f1 = [int(item) for item in f]
selection_sort(f1)
output = open("output.txt", "w+")
for i in range(len(f1)):
    output.write(str(f1[i])+ "\n")
output.close()