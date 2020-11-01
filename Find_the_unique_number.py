def find_uniq(arr):
    a, b = set(arr) #=> {1, 2}
    return a if arr.count(a) == 1 else b


print(find_uniq([1, 1, 1, 2, 1, 1]))
