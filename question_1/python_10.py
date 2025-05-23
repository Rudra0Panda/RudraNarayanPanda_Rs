def missing(arr1, arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    missing = s1.symmetric_difference(s2)
    return missing.pop() if missing else None
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 1, 5]
print(missing(arr1, arr2))
