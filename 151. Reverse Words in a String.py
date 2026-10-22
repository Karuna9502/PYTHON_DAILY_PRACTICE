class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        i = 0
        n = len(s)
        while i < n :
            while i < n and s[i] == " ":
                i = i + 1
            if i < n :
                word_start = i
                while  i < n and s[i] != " ":
                    i = i + 1 
                word.append(s[word_start:i])
        return " ".join(word[::-1])
