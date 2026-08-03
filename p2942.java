class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        ArrayList<Integer> indicesArray = new ArrayList<Integer>();

        for (int i = 0; i < words.length; i++){
            if (words[i].contains(x + "")){ // words[i].indexOf(x) != -1
                indicesArray.add(i);
            }
        }

        return indicesArray;
    }
}