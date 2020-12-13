class Solution {
    public int minPartitions(String n) {
        var result = 0;

        for (var c : n.toCharArray()) {
            result = Math.max(Character.getNumericValue(c), result);
        }

        return result;
    }
}
