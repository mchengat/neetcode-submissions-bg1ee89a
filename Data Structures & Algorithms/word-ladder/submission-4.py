class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        def neighbors(word):
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    yield word[:i] + c + word[i+1:]

        front = {beginWord}
        back = {endWord}
        level = 1
        visited = {beginWord, endWord}

        while front and back:
            if len(front) > len(back):
                front, back = back, front
            
            next_front = set()
            for word in front:
                for nei in neighbors(word):
                    if nei in back:
                        return level+1
                    if nei in wordSet and nei not in visited:
                        visited.add(nei)
                        next_front.add(nei)
            
            front = next_front
            level += 1
        
        return 0