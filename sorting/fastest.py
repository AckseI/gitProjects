import time

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

start_time = time.time()

f = open("sorting/test.txt", "r").readlines()
f = [line.rstrip() for line in f]
f1 = [int(item) for item in f]
quick_sort(f1)
output = open("sorting/output.txt", "w+")
for i in range(len(f1)):
    output.write(str(f1[i])+ "\n")
output.close()

time_execution =  time.time() - start_time

print("Время выполнения: ", time_execution)