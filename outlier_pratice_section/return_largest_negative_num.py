nums = [-8, -3, 5, -10, 2]


def largest_negative(nums: list[int]) -> int | None:

    if not nums:
        return None

    largest: int = None

    for num in nums:
        if num < 0:
            if largest is None:
                largest = num

            elif num > largest:
                largest = num

    return largest


print(largest_negative(nums))
