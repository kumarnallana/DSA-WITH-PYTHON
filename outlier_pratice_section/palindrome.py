
char_list: list[str] = ["madam", "python", "RaceCar", ""]
language = "python"


class Solution:

    def manual_length(self, text: str) -> int:

        count = 0

        for _ in text:
            count += 1

        return count

    def is_palindrome(self, text: str) -> bool:

        n = self.manual_length(text)
        left = 0
        right = n - 1

        if not text:
            return True

        while left < right:
            if text[left].lower() != text[right].lower():
                return False

            else:
                left += 1
                right -= 1

        return True


solution = Solution()

print(solution.is_palindrome(char_list[0]))
