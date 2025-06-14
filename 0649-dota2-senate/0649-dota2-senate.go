type Senator struct {
    char rune
    index int
}

func predictPartyVictory(senate string) string {
    rQueue := []Senator{}
    dQueue := []Senator{}

    for i, s := range senate{
        if s == 'R' {
            rQueue = append(rQueue, Senator{index:i, char:s})
        }else{
            dQueue = append(dQueue, Senator{index:i, char:s})
        }
    }

    for len(rQueue) > 0 && len(dQueue) > 0 {
        if rQueue[0].index < dQueue[0].index{
            winner := rQueue[0]
            rQueue = rQueue[1:]
            dQueue = dQueue[1:]
            winner.index += len(senate)
            rQueue = append(rQueue, winner)
        }else{
            winner := dQueue[0]
            rQueue = rQueue[1:]
            dQueue = dQueue[1:]
            winner.index += len(senate)
            dQueue = append(dQueue, winner)
        }
    } 

    if len(rQueue) == 0 {
        return "Dire"
    }else{
        return "Radiant"
    }
}