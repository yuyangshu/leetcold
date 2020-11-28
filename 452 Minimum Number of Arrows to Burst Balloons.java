class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }

        Arrays.sort(points, (a, b) -> a[1] - b[1]);

        int strikingAt = points[0][1], count = 1;

        for (int i = 1; i < points.length; i ++) {
            if (strikingAt < points[i][0] || strikingAt > points[i][1]) {
                count += 1;
                strikingAt = points[i][1];
            }
        }

        return count;
    }
}
