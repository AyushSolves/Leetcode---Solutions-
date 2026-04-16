class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                max_count = max(max_count, current)
            else:
                current = 0

        return max_count

if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,1,0,1,1,1]
    print(sol.findMaxConsecutiveOnes(nums1))  # Output: 3

    nums2 = [1,0,1,1,0,1]
    print(sol.findMaxConsecutiveOnes(nums2))  # Output: 2