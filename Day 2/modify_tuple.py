
# Author : Muhammad Turab

def append_into_tuple(element, tuple1):
    list1 = list(tuple1)

    list1.append(element)

    tuple2 = tuple(list1)

    return tuple2


tuple1 = (1, 2, 3, 4, 5, 6)

print("Tuple before appending an element: ", tuple1)

print("Tuple after appending an element: ", append_into_tuple(20, tuple1))

