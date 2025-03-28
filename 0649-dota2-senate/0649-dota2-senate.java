class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Integer> queueR = new LinkedList();
        Queue<Integer> queueD = new LinkedList();
        for (int i=0; i<senate.length(); i++){
            if (senate.charAt(i) == 'R') {
                queueR.add(i);
            }else{
                queueD.add(i);
            }
        }

        int l = senate.length();

        while(!queueR.isEmpty() && !queueD.isEmpty()){
            int r = queueR.poll();
            int d = queueD.poll();
            
            if (r < d) {
                queueR.add(l + r);
            }else{
                queueD.add(l + d);
            }

        }

        if (!queueR.isEmpty()){
            return "Radiant";
        }else{
            return "Dire";
        }
    }
}