class Solution:
    def equalFrequency(self, word: str) -> bool:

        counter = Counter(word)

        for c in list(counter.keys()):
            counter[c]-=1
            if counter[c]==0:
                del counter[c]
            
            if len(set(counter.values()))==1:
                return True 
            counter = Counter(word)

        return False

            





        