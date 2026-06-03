class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        nums = []
        for row in mat:
            nums.extend(row)

        result = []
        for i in range(0, len(nums), c):
            result.append(nums[i:i + c])

        return result