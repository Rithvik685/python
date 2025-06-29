def largest(arr: list[int]) -> int:
    a = arr[0]
    for i in arr:
        if i > a:
            a = i
    return a


result = largest([1, 8, 9, 44, 90])
print(result)
