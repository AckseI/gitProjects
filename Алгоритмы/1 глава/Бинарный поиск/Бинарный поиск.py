def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        guess = list[mid]
        if guess == item:
            return print(mid) 
        if guess > item:
            high = mid - 1  
        else:
            low = mid + 1
    return print(None)

my_list = [1, 3, 5, 7, 9, 16, 22, 66, 200]

binary_search(my_list, 16)