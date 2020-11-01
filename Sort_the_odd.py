def sort_array(arr):
    odds = sorted((x for x in arr if x%2 != 0), reverse=True)
    return [x if x%2==0 else odds.pop() for x in arr]

# def sort_array(source_array):
#     return [] if len(source_array) == 0 else list(map(int, (
#         ','.join(['{}' if a % 2 else str(a) for a in source_array])).format(
#         *list(sorted(a for a in source_array if a % 2 == 1))).split(',')))


print(sort_array([11, 1, 11, 11, 2, 1, 111, 0]))
