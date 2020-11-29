class Solution {
    public int minMoves(int[] nums, int limit) {
        var turningPoint = new TreeMap<Integer, Integer>();

        for (int i = 0; i < nums.length / 2; i ++) {
            int less = Math.min(nums[i], nums[nums.length - i - 1]), more = Math.max(nums[i], nums[nums.length - i - 1]);

            if (less == 1) {
                addToMap(turningPoint, 2, 1);
            }
            else {
                addToMap(turningPoint, 2, 2);
                addToMap(turningPoint, less + 1, -1);
            }

            addToMap(turningPoint, less + more, -1);

            if (less + more + 1 <= limit * 2) {
                addToMap(turningPoint, less + more + 1, 1);
            }
            if (more + limit + 1 <= limit * 2) {
                addToMap(turningPoint, more + limit + 1, 1);
            }
        }

        int watermark = 0, minimal = Integer.MAX_VALUE;
        for (var entry : turningPoint.entrySet()) {
            watermark += entry.getValue();
            if (watermark < minimal) {
                minimal = watermark;
            }
        }

        return minimal;
    }

    private void addToMap(TreeMap<Integer, Integer> map, int key, int change) {
        if (map.containsKey(key)) {
            map.put(key, map.get(key) + change);
        }
        else {
            map.put(key, change);
        }
    }
}
