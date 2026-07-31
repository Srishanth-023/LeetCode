class Solution {
    public int countDigits(int num) {
        int count = 0;
        int numCopy = num;
        // String numString = Integer.toString(num);

        // for (int i = 0; i < numString.length(); i++){
        //     char character = numString.charAt(i);
        //     int individualNumber = Character.digit(character, 10);

        //     if (num % individualNumber == 0){
        //         count++;
        //     }
        // }

        while (num > 0){
            int temp = num % 10;

            if (temp != 0 && numCopy % temp == 0){ // numCopy % (num % 10) == 0 (Instead of creating an additional variable, use that check in the loop)
                count++;
            }

            num = num / 10;
        }

        return count;
    }
}