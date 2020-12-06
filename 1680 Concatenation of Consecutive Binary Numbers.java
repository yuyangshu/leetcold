class Solution {
    public int concatenatedBinary(int n) {
        long numDigits = 1, threshold = 2, result = 0, modulo = 1000000007;

        for (var i = 1; i <= n; i ++) {
            if (i == threshold) {
                threshold *= 2;
                numDigits += 1;
            }
            result = ((result << numDigits) + i) % modulo;
        }

        return Math.toIntExact(result);
    }
}
