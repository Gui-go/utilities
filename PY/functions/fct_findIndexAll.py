def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):  # repeat itself indefinitely, recursively.
                indices.append([i]+index)
    return indices

if __name__ == '__main__':    
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))
    print(index_all(example, [1, 2, 3]))



# isinstance() checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
# numbers = [1, 2, 3, 4, 2, 5]
# isinstance(numbers, list)
# Output: True

