class Solution {
    public String minWindow(String s, String t) {
        var required = new HashMap<Character, Integer>();
        for (var c : t.toCharArray()) {
            if (required.containsKey(c)) {
                required.put(c, required.get(c) + 1);
            }
            else {
                required.put(c, 1);
            }
        }

        int start = 0, count = 0;
        var result = "";
        var rollingCount = new HashMap<Character, Integer>();

        for (int i = 0; i < s.length(); i ++) {
            var currentChar = s.charAt(i);
            var newCount = rollingCount.containsKey(currentChar) ? rollingCount.get(currentChar) + 1 : 1;
            rollingCount.put(currentChar, newCount);

            if (required.containsKey(currentChar) && newCount == required.get(currentChar)) {
                count += 1;
            }

            while (count == required.keySet().size()) {
                if (result == "" || result.length() > i - start + 1) {
                    result = s.substring(start, i + 1);
                }

                currentChar = s.charAt(start);
                newCount = rollingCount.get(currentChar) - 1;
                rollingCount.put(currentChar, newCount);

                if (required.containsKey(currentChar) && newCount == required.get(currentChar) - 1) {
                    count -= 1;
                }

                start += 1;
            }
        }

        return result;
    }
}
