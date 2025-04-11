class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        n = len(wordList)
        m = len(wordList[0])

        visited = set(wordList)

        q = deque([beginWord])
        count = 0

        while q:
            count += 1
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return count

                for k in range(m):
                    for j in range(ord('a'), ord('z') + 1):
                        if ord(word[k]) == j:
                            continue
                        next_word = word[:k] + chr(j) + word[k+1:]
                        if next_word in visited:
                            q.append(next_word)
                            visited.remove(next_word)

        return 0