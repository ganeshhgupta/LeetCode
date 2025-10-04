class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)        
        res = sorted(count.keys(), key=lambda x: (-count[x], x))        
        return res[:k]
