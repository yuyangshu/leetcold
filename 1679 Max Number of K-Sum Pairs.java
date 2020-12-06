class Solution {
    public int maxOperations(int[] nums, int k) {
        var seen = new HashMap<Integer, Integer>();
        var count = 0;

        for (var i : nums) {
            if (seen.getOrDefault(k - i, 0) > 0) {
                count += 1;
                seen.put(k - i, seen.get(k - i) - 1);
            }
            else {
                seen.put(i, seen.getOrDefault(i, 0) + 1);
            }
        }

        return count;
    }
}
