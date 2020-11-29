class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        int stack[] = new int[k], j = 0, n = nums.length;

        for (int i = 0; i < nums.length; i ++) {
            while (j > 0 && nums[i] < stack[j - 1] && j + n - i - 1 >= k) {
                j --;
            }
            if (j < k) {
                stack[j] = nums[i];
                j ++;
            }
        }

        return stack;
    }
}
