import itertools as iter


def permutations(string):
    l = []
    for i in iter.permutations(string):
        s = ''.join(i)
        l.append(str(s))
    return set(l)

# import itertools
#
# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))


print(sorted(permutations('aabb')))
