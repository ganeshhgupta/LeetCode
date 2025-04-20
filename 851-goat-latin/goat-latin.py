class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        li = sentence.split(" ")  
        c = 1
        
        for i in range(len(li)):
            word = li[i]
            
            if word[0] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                li[i] = word + 'ma' + 'a' * c
            else:
                li[i] = word[1:] + word[0] + 'ma' + 'a' * c
                
            c += 1 
        
        return " ".join(li)

