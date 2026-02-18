import java.util.*;

public class Solution 
{
    public boolean containsNearbyDuplicate(int[] nums, int k) 
    {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            if (map.containsKey(nums[i])) {

                int prevIndex = map.get(nums[i]);

                if (i - prevIndex <= k) {
                    return true;
                }
            }

            map.put(nums[i], i);
        }

        return false;
    }
    public static void main(String[] args) 
    {

        int[] nums = {1, 2, 3, 1};
        int k = 3;

        Solution sol = new Solution();

        System.out.println(sol.containsNearbyDuplicate(nums, k));
    }
}
