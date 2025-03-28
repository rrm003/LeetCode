class RecentCounter {
    int counter;
    Queue<Integer> requests;

    public RecentCounter() {
        this.requests = new LinkedList();
    }
    
    public int ping(int t) {
        this.requests.add(t);

        int index = 0;
        Iterator<Integer> iterator = this.requests.iterator();
        while (iterator.hasNext()){
            int element = iterator.next();
            
            if (element >=  t - 3000) {
                return this.requests.size() - index;
            }

            index += 1;
        }

        return 1;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */