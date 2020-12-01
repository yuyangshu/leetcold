class Solution {
    public String findLongestWord(String s, List<String> d) {
        var result = "";

        for (var word : d) {
            var i = 0;
            for (var c : s.toCharArray()) {
                if (i < word.length() && word.charAt(i) == c) {
                    i += 1;
                }
            }

            if (i == word.length() && (word.length() > result.length() || word.length() == result.length() && word.compareTo(result) < 0)) {
                result = word;
            }
        }

        return result;
    }
}
