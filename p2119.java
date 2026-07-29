class Solution {
    public boolean isSameAfterReversals(int num) {
        // // My solution
        // String numStr1 = Integer.toString(num);
        // String revStr1 = new StringBuilder(numStr1).reverse().toString();
        // int num1 = Integer.parseInt(revStr1);

        // String numStr2 = Integer.toString(num1);
        // String revStr2 = new StringBuilder(numStr2).reverse().toString();
        // int num2 = Integer.parseInt(revStr2);

        // if (num == num2){
        //     return true;
        // } else{
        //     return false;
        // }

        
        // General approach
        if (num == 0){
            return true;
        } else if (num % 10 == 0){
            return false;
        }

        return true;
    }
}