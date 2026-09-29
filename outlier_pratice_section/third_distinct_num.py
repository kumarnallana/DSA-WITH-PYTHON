
nums: list[int] = [6, 2, 9, 7, 9, 5, 3, 22]


def third_distinct(nums: list[int]) -> int | None:

    largest = None
    second = None
    third = None

    seen = set()

    if not nums:
        return None

    for num in nums:
        if largest == num or second == num or third == num:
            continue

        elif largest is None or num > largest:
            third = second
            second = largest
            largest = num

        elif second is None or num > second:
            third = second
            second = num

        elif third is None or num > third:
            third = num

        else:
            seen.add(num)

    return third


print(third_distinct(nums))
