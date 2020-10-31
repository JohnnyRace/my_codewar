def find_uniq(arr):
    if len(arr) < 1000:
        for n in arr:
            if arr.count(n) == 1:
                return n
    else:
        for n in arr:
            if n != arr[arr.index(n) - 1] and n != arr[arr.index(n) + 1]:
                return n

    # def find_uniq(arr):
    #     a, b = set(arr) #=> {1, 2}
    #     return a if arr.count(a) == 1 else b


print(find_uniq([1, 1, 1, 2, 1, 1]))
