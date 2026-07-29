// class Solution {
//     public int sum(int num1, int num2) {
//         return num1 + num2;
//     }
// }

// Addition of 2 numbers without using '+' operator
class Solution {
    public int sum(int num1, int num2) { 
        while (num2 != 0){
            int carry = num1 & num2; // Where bits are 1
            num1 = num1 ^ num2; // Sum without carrying
            num2 = carry << 1; // Carry belong to next position, so shift left 
        }

        return num1;
    }
}