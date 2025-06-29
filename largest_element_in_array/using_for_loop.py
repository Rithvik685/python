def largest(arr: list[int]) -> int:
    a = arr[0]
    for i in arr:
        if i > a:
            a = i
    return a


largest([1, 8, 9, 44, 90])
