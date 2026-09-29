nums = [4, 5, 6, 6, 5, 7]

frequency: dict[int | int] = {}


def non_repeating_num(nums: list[int]) -> int:
    for num in nums:
        if num in frequency:
            frequency[num] += 1

        else:
            frequency[num] = 1

    for num in nums:
        if frequency[num] == 1:
            return num

    return None


print(non_repeating_num(nums))
