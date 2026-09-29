nums = [7, 3, 11, 5, 9]


def largest_odd(nums):
    largest = None

    for num in nums:
        if num % 2 != 0:
            if largest is None:
                largest = num
            elif num > largest:
                largest = num

    return largest


print(largest_odd(nums))
