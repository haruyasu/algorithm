def binary_search(list, num):
    sorted_list = sorted(list)

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        center = (low + high) / 2
        if num == sorted_list[center]:
            return True
        elif num > sorted_list[center]:
            low = center + 1
        else:
            high = center - 1

    return False

list = [1, 2, 4, 8, 16, 99, 32, 64]

num = 10
result = binary_search(list, num)
print result

num = 32
result = binary_search(list, num)
print result

num = 100
result = binary_search(list, num)
print result

num = 0
result = binary_search(list, num)
print result
