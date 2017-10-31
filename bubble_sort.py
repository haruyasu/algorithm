def bubble_sort(list):
        for i in range(len(list)):
            for j in range(len(list) - 1, i, -1):
                if list[j] < list[j - 1]:
                    list[j], list[j - 1] = list[j - 1], list[j]
        return list

list = [1,3,5,7,9,2,4,6,8]
sort_list = bubble_sort(list)
print sort_list
