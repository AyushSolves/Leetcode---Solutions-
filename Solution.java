public class Solution {

    public String convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }

        boolean negative = false;

        if (num < 0) {
            negative = true;
            num = -num;
        }

        String result = "";

        while (num > 0) {
            result = (num % 7) + result;
            num = num / 7;
        }

        if (negative) {
            result = "-" + result;
        }

        return result;
    }

    // For VS Code testing
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.convertToBase7(100)); // Output: 202
        System.out.println(sol.convertToBase7(-7));  // Output: -10
    }
}