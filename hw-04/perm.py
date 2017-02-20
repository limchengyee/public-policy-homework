def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    perms = []
    for i in range(len(lst)):
        curr = lst[i]
        others = lst[:i] + lst[i+1:]
        for p in permutation(others):
            perms.append([curr] + p)
    return perms

a = permutation([1,7,9])
#    b = ", ".join(str(i) for i in a)
for i in range(len(a)):
    b = ''.join(str(x) for x in a[i])
    print(b)
