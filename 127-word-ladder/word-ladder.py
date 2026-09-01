class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # ≈ O(N × L²), O(N)
        
        words = set(wordList)

        if endWord not in words:
            return 0
        
        q = deque([(beginWord, 1)])

        words.discard(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word in words:
                        words.discard(new_word)
                        q.append((new_word, steps + 1))

        return 0

