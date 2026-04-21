class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        reachable = {}
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in reachable:
                    reachable[pattern] = []
                reachable[pattern].append(word)
        
        print(reachable)

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                        return res

                print(word)
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for new_word in reachable[pattern]:
                        print(f"new_word:{new_word}")
                        if new_word not in visited:
                            q.append(new_word)
                            visited.add(new_word)
            res += 1
        
        return 0
