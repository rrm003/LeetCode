# queue = [lot, dog, log] 

# dog
# 1 : [h, d, l, c]
# cog

# 2 : [i, o]
# dig

# 3 : [t, g]

# visited = [hit, hot, dot, dog]
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_lookup = {}
        level_lookup = {}

        n = len(beginWord) # len(beginWord) == len(endWord)

        # mark all the word not visited
        for word in wordList:
            word_lookup[word] = False
        

        # get characters available at each level
        for i in range(n):
            level_lookup[i] = set()
            for word in wordList:
                level_lookup[i].add(word[i]) 

        for i in range(n):
            level_lookup[i].add(beginWord[i])


        # print(word_lookup)
        # print(level_lookup)

        queue = deque()
        queue.append((beginWord, 0))
        word_lookup[beginWord] = True

        while queue:
            # print(queue)
            curr, level = queue.popleft()
            if curr == endWord: return level + 1
            for i in range(n):
                for x in level_lookup[i]:
                    new_word = curr[:i] + x + curr[i+1:]
                    if new_word in word_lookup and not word_lookup[new_word]:
                        word_lookup[new_word] = True
                        queue.append((new_word, level + 1))
        return 0