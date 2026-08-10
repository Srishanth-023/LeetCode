class Solution {
    public int scoreOfString(String s) {
        char[] charArray = s.toCharArray();

        int score = 0;
        for (int i = 1; i < charArray.length; i++){
            score += Math.abs((int)charArray[i] - (int)charArray[i - 1]);
        }

        return score;
    }
}