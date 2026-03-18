public class Solution {

    public boolean isPerfectSquare(int num) {

        if (num < 2) {
            return true;
        }

        long left = 1;
        long right = num;

        while (left <= right) {

            long mid = left + (right - left) / 2;
            long square = mid * mid;

            if (square == num) {
                return true;
            } 
            else if (square < num) {
                left = mid + 1;
            } 
            else {
                right = mid - 1;
            }
        }

        return false;
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        int num1 = 16;
        int num2 = 14;

        System.out.println(num1 + " -> " + sol.isPerfectSquare(num1)); // true
        System.out.println(num2 + " -> " + sol.isPerfectSquare(num2)); // false
    }
}