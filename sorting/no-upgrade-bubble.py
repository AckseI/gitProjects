def upgrade_bubble(arr):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

f = open("test.txt", "r").readlines()
f = [line.rstrip() for line in f]
f1 = [int(item) for item in f]
upgrade_bubble(f1)
output = open("output.txt", "w+")
for i in range(len(f1)):
    output.write(str(f1[i])+ "\n")
output.close()