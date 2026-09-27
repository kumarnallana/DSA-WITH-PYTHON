company: str = "OpenAI"


def vowels_count(word: str) -> int:
    count = 0

    vowels: set = {'a', 'e', 'i', 'o', 'u'}

    for letter in word:
        if letter.lower() in vowels:
            count += 1

    return count


print(vowels_count(company))
