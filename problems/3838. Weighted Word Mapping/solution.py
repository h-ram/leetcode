class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
    
        def word_sum(word):
            sum_ = 0
            for char in word:
                sum_ += weights[ord(char) - 97]
            return sum_

        converter = "zyxwvutsrqponmlkjihgfedcba"
        answer = []
        for word in words:
            wsum = word_sum(word) % 26
            answer.append(converter[wsum])

        return "".join(answer)
            
            