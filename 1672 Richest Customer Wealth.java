class Solution {
    public int maximumWealth(int[][] accounts) {
        int highest = 0, m = accounts.length, n = accounts[0].length;
        for (int i = 0; i < m; i ++) {
            var rollingSum = 0;

            for (int j = 0; j < n; j ++) {
                rollingSum += accounts[i][j];
            }

            if (rollingSum > highest) {
                highest = rollingSum;
            }
        }

        return highest;
    }
}
