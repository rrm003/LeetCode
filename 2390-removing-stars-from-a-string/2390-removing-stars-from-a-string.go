func removeStars(s string) string {
    stack := []string{}

    for _, r := range s{
        if r == '*' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            }

            continue
        }
        
        stack = append(stack, string(r))
    }

    return strings.Join(stack, "")
}