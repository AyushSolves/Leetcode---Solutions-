public class Solution {

    public String toHex(int num) {

        if (num == 0) return "0";

        char[] hex = "0123456789abcdef".toCharArray();
        StringBuilder result = new StringBuilder();

        while (num != 0) {
            int digit = num & 15; // last 4 bits
            result.append(hex[digit]);
            num >>>= 4; // unsigned right shift
        }

        return result.reverse().toString();
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        int num1 = 26;
        int num2 = -1;

        System.out.println(num1 + " -> " + sol.toHex(num1)); // 1a
        System.out.println(num2 + " -> " + sol.toHex(num2)); // ffffffff
    }
}