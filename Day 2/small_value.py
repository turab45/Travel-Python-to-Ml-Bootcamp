
# Muhammad Turab

def find_small_value(list):
    list_len = len(list)

    small = list[1]

    for i in range(list_len - 1):

        if small > list[i]:
            small = list[i]
    
    return small


list1 = [99, 22, 11, 56, 9, 78, 100]

print("Small number in the list is : ", find_small_value(list1))


