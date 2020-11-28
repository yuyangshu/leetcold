class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (a, b) -> a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]);

        var results = new ArrayList<int[]>();
        for (var p : people) {
            results.add(p[1], p);
        }

        return results.toArray(new int[people.length][2]);
    }
}
