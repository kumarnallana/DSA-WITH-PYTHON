nums: list[int] = [
    34, 17, 88, 5, 62, 91, 14, 23, 76, 45,
    12, 99, 58, 3, 80, 27, 64, 41, 10, 85,
    38, 7, 92, 53, 16, 73, 48, 29, 82, 67,
    20, 95, 4, 61, 36, 79, 18, 55, 70, 31,
    86, 9, 50, 65, 22, 97, 44, 13, 78, 35,
    60, 25, 84, 1, 68, 43, 8, 89, 52, 37,
    74, 15, 96, 47, 24, 81, 30, 63, 6, 93,
    42, 19, 72, 57, 28, 87, 2, 59, 32, 75,
    46, 21, 94, 11, 70, 39, 88, 51, 26, 69,
    40, 98, 33, 83, 18, 54, 77, 66, 90, 49
]


def largest_even(nums: list[int]) -> int:
    if not nums:
        return []

    even_list: list[int] = []

    for num in nums:
        if num % 2 == 0:
            even_list.append(num)

    largest = even_list[0]

    for even in even_list:
        if even > largest:
            largest = even

    return largest


print(largest_even(nums))
