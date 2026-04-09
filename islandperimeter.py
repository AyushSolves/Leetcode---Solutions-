class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4

                    # Check top
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # Check left
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter

if __name__ == "__main__":
    sol = Solution()

    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]

    print(sol.islandPerimeter(grid))  # Output: 16