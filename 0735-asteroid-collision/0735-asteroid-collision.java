class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack();

        for(int i=0; i < asteroids.length; i++) {
            int a = asteroids[i];

            if(stack.size() == 0) {
                stack.push(a);
                continue;
            }

            if (stack.peek() > 0 & a < 0) {
               while( stack.size() > 0 && stack.peek() > 0 && Math.abs(stack.peek()) < Math.abs(a)){
                    stack.pop();
               }

               if(stack.size() == 0){
                    stack.push(a);
               }else if(stack.peek() + a == 0){
                    stack.pop();
               }else if(stack.peek() < 0){
                    stack.push(a);
               }
            }else{
                stack.push(a);
            }

            // System.out.println(stack);
        }

        if(stack == null) 
            return new int[0];

        int l = stack.size();
        int[] rslt = new int[l];

        int i = l - 1;
        while(stack.size()!=0){
            int top = stack.pop();
            rslt[i] = top;
            i -= 1;
        }

        return rslt;
    }
}