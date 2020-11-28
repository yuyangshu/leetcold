class Solution {
    public List<Integer> partitionLabels(String S) {
        var lastAppearance = new HashMap<Character, Integer>();

        for (var i = 0; i < S.length(); i ++) {
            lastAppearance.put(S.charAt(i), i);
        }

        var start = 0;
        var results = new ArrayList<Integer>();

        while (start <= S.length() - 1) {
            var currentLength = 0;
            var intervalEnd = lastAppearance.get(S.charAt(start));

            while (start <= intervalEnd) {
                currentLength += 1;
                intervalEnd = Math.max(intervalEnd, lastAppearance.get(S.charAt(start)));
                start += 1;
            }

            results.add(currentLength);
        }

        return results;
    }
}
