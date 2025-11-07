class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        words_count = defaultdict(int)
        for word in words:
            words_count[word] += 1

        result = []
        for i in range(word_len):  # We can start at any position in the range of word length
            left = i
            right = i
            window_count = defaultdict(int)
            while right + word_len <= len(s):
                
                # Extract the current word from the string
                word = s[right:right + word_len]
                right += word_len  # Move right pointer by word length

                if word in words_count:
                    window_count[word] += 1

                    # If word count exceeds the required count, move left pointer
                    while window_count[word] > words_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        left += word_len
                    
                    # Check if the window has the exact count of words
                    if right - left == word_len * num_words:
                        result.append(left)
                else:
                    # If the word is not in the list of words, reset the window
                    window_count.clear()
                    left = right
        
        return result
