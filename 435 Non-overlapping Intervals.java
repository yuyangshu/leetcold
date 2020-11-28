class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }

        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

        int watermark = intervals[0][1];
        int keep = 1;

        for (int[] interval : intervals) {
            if (interval[0] >= watermark) {
                keep += 1;
                watermark = interval[1];
            }
        }

        return intervals.length - keep;
    }
}
