type RecentCounter struct {
    queue []int
}


func Constructor() RecentCounter {
    return RecentCounter{
        queue: []int{},
    }
}


func (this *RecentCounter) Ping(t int) int {
    this.queue= append(this.queue, t)
    
    i := 0 
    for this.queue[i] < t - 3000 {
        i += 1
    }

    this.queue = this.queue[i:]

    return len(this.queue)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */