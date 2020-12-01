class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int c = 0;
        for (int i = 0; c < g.length && i < s.length; i ++) {
            if (g[c] <= s[i]) {
                c += 1;
            }
        }

        return c;
    }
}