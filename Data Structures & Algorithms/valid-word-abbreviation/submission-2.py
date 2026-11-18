class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0 
        k = len(word)
        p = len(abbr)
        
        while i < k and j < p:
          if abbr[j].isdigit():
             if abbr[j] == "0":
               return False
             b = 0 
             while j < p and abbr[j].isdigit():
                b = b*10 + int(abbr[j])
                j += 1 
             i += b
          else:
            if abbr[j] != word[i]:
                return False 
            i += 1 
            j += 1 
        return i == k and j == p