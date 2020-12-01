class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        var counter = new HashMap<Character, Integer>();
        int result = 0, head = 0, count = 0;

        for (var i = 0; i < s.length(); i ++) {
            if (counter.containsKey(s.charAt(i))) {
                counter.put(s.charAt(i), counter.getOrDefault(s.charAt(i), 0) + 1);
            }
            else {
                counter.put(s.charAt(i), 1);
                count += 1;
            }

            while (head <= i && count > k) {
                if (counter.getOrDefault(s.charAt(head), 0) > 1) {
                    counter.put(s.charAt(head), counter.get(s.charAt(head)) - 1);
                }
                else {
                    counter.remove(s.charAt(head));
                    count -= 1;
                }

                head += 1;
            }

            result = Math.max(i - head + 1, result);
        }

        return result;
    }
}
