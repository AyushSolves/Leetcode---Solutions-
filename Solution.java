
public class Solution {

    public boolean canConstruct(String ransomNote, String magazine) {

        int[] count = new int[26];

        for (char c : magazine.toCharArray()) {
            count[c - 'a']++;
        }

        for (char c : ransomNote.toCharArray()) {
            if (count[c - 'a'] == 0) {
                return false;
            }
            count[c - 'a']--;
        }

        return true;
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        System.out.println(sol.canConstruct("a", "b"));     // false
        System.out.println(sol.canConstruct("aa", "ab"));   // false
        System.out.println(sol.canConstruct("aa", "aab"));  // true
    }
}
