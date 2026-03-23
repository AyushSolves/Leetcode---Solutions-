public class Solution {

    public char findTheDifference(String s, String t) {

        char result = 0;

        for (char c : s.toCharArray()) {
            result ^= c;
        }

        for (char c : t.toCharArray()) {
            result ^= c;
        }

        return result;
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        String s1 = "abcd";
        String t1 = "abcde";

        String s2 = "";
        String t2 = "y";

        System.out.println(sol.findTheDifference(s1, t1)); // e
        System.out.println(sol.findTheDifference(s2, t2)); // y
    }
}