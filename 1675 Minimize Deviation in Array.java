class Solution {
    public int minimumDeviation(int[] nums) {
        var heap = new PriorityQueue<Integer>();
        int min = Integer.MAX_VALUE;

        for (var n : nums) {
            if (n % 2 == 1) {
                n *= 2;
            }
            heap.add(-n);
            min = Math.min(min, n);
        }

        int result = Integer.MAX_VALUE;
        while (heap.size() > 0) {
            var max = -heap.poll();

            result = Math.min(result, max - min);
            if (max % 2 == 1) {
                return result;
            }

            min = Math.min(max / 2, min);
            heap.add(-max / 2);
        }

        return result;
    }
}
