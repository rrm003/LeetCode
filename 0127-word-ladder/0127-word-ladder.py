from collections import deque as dq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lookup = {}
        l = len(beginWord)

        word_set = set(wordList)

        for i in range(l):
            lookup[i] = set()
        
        for i in range(l):
            for word in word_set:
                lookup[i].add(word[i])

        queue = dq([])
        queue.append((beginWord, 1))
        visited = {beginWord: 1}

        while queue:
            curr, lvl = queue.popleft()
            
            if curr == endWord: return lvl
            
            visited[curr] = lvl
            
            i, l = 0, len(curr)
            for i in range(l):
                for c in lookup[i]:
                    new_word = curr[:i] + c + curr[i+1:]
                    if new_word != curr and new_word not in visited and new_word in word_set:
                        queue.append((new_word, lvl + 1))
                        visited[new_word] = lvl + 1
        return 0