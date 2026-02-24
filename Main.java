
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int n1 = 16;
        int n2 = 3;

        System.out.println(n1 + " is power of two: " + sol.isPowerOfTwo(n1));
        System.out.println(n2 + " is power of two: " + sol.isPowerOfTwo(n2));
    }
}

class Solution {

    public boolean isPowerOfTwo(int n) {

        return n > 0 && (n & (n - 1)) == 0;

    }
}