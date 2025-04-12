class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #map where key is int list, val is string list

        for s in strs: # for every word in the input string list

            count = [0] * 26 #creating an int list of 26 zeros

            #00000000000000...

            for c in s: #for every char in the word, flip corr int list 0 to 1
                count[ord(c) - ord("a")] += 1

                '''
                for 'eat'
                index of the respective alphabet in count[] array:
                10001000..
                abcdef...
                '''

            res[tuple(count)].append(s)

            #key: 10001000 .. : will contain 'eat', 'ate', etc all the anangrams

        #print(res)
        #print(res.values())
        return list(res.values())