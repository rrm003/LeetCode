import "strings"

func removeComments(source []string) []string {
    isMultiline := false
    isSingleline := false
    rslt := ""
    
    joinedSource := strings.Join(source, "\\n")
    for i := 0; i < len(joinedSource); i++ {
        if i + 1 < len(joinedSource) && string(joinedSource[i]) == "/" && string(joinedSource[i+1]) == "*" && !isSingleline && !isMultiline{
            isMultiline = true
            i+=1
            continue
        }

        if i + 1 < len(joinedSource) && string(joinedSource[i]) == "*" && string(joinedSource[i+1]) == "/" && isMultiline{
            isMultiline = false
            i+=1
            continue
        }
        
        if isMultiline{
            continue
        }

        if i + 1 < len(joinedSource) && string(joinedSource[i]) == "/" && string(joinedSource[i+1]) == "/"{
            isSingleline = true
            i+=1
            continue
        }

        if i + 1 < len(joinedSource) && string(joinedSource[i]) == "\\" && string(joinedSource[i+1]) == "n"{
            isSingleline = false
            i+=1
            rslt += "\n"
            continue
        }

        if isSingleline {
            continue
        }

        rslt += string(joinedSource[i])
    }

 
    // fmt.Println("rslt", rslt)
    // fmt.Println("splitted", strings.Split(rslt,"\n"))
    splitted := strings.Split(rslt,"\n")
    no_empty := []string{}

    for i:=0; i<len(splitted); i++ {
        if splitted[i] != "" {
            no_empty = append(no_empty, splitted[i])
        }
    }

    return no_empty
}