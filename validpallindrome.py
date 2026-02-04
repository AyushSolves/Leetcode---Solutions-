class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "

    print(sol.isPalindrome(s1))  
    print(sol.isPalindrome(s2))  
    print(sol.isPalindrome(s3))  
