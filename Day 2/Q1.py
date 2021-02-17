
# Author : Muhammad Turab

def add_into_list(number, list):
    list_len = len(list)
    for i in range(list_len):
        list[i] = list[i] + number
    return list


list1 = [1, 2, 3, 12, 19, 2]

print("Before adding 3: ", list1)

list1 = add_into_list(3, list1)

print("After adding 3: ", list1)

