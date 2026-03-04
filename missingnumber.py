class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        result = n

        for i in range(n):
            result ^= i ^ nums[i]

        return result


# For VS Code / local testing
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 0, 1]
    nums2 = [0, 1]
    nums3 = [9,6,4,2,3,5,7,0,1]

    print("Input:", nums1, "Output:", sol.missingNumber(nums1))  # 2
    print("Input:", nums2, "Output:", sol.missingNumber(nums2))  # 2
    print("Input:", nums3, "Output:", sol.missingNumber(nums3))  # 8