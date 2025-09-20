class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch in "AEIOUaeiou"]
        vowels.sort()

        result = []
        j = 0
        for ch in s:
            if ch in "AEIOUaeiou":
                result.append(vowels[j])
                j += 1
            else:
                result.append(ch)

        return "".join(result)
