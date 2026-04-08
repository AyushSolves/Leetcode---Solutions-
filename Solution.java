public class Solution {

    public int hammingDistance(int x, int y) {

        int xor = x ^ y; // XOR gives differing bits
        int count = 0;

        while (xor != 0) {
            count += xor & 1; // check last bit
            xor >>= 1;        // shift right
        }

        return count;
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        int x1 = 1, y1 = 4;
        int x2 = 3, y2 = 1;

        System.out.println(sol.hammingDistance(x1, y1)); // 2
        System.out.println(sol.hammingDistance(x2, y2)); // 1
    }
}