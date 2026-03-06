class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0

        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill remaining positions with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1


# For VS Code / Local Testing
if __name__ == "__main__":
    sol = Solution()

    nums1 = [0,1,0,3,12]
    sol.moveZeroes(nums1)
    print("Output:", nums1)

    nums2 = [0]
    sol.moveZeroes(nums2)
    print("Output:", nums2)