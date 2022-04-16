def insertion_sort(arr):
    for i in range(1,len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item_to_insert:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = item_to_insert

f = open("test.txt", "r").readlines()
f = [line.rstrip() for line in f]
f1 = [int(item) for item in f]
insertion_sort(f1)
output = open("output.txt", "w+")
for i in range(len(f1)):
    output.write(str(f1[i])+ "\n")
output.close()