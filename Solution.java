public class Solution {

    public int[] constructRectangle(int area) {

        int w = (int) Math.sqrt(area);

        // find the largest factor <= sqrt(area)
        while (area % w != 0) {
            w--;
        }

        int l = area / w;

        return new int[]{l, w};
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        int area1 = 4;
        int[] res1 = sol.constructRectangle(area1);
        System.out.println(res1[0] + " " + res1[1]); // 2 2

        int area2 = 37;
        int[] res2 = sol.constructRectangle(area2);
        System.out.println(res2[0] + " " + res2[1]); // 37 1
    }
}