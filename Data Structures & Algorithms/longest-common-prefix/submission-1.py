class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        prefix_set = set()
        longest_prefix = ""
        max_len = 0
        for ch in strs[0]:
            prefix += ch
            prefix_set.add(prefix)
            longest_prefix = prefix
            max_len += 1
        
        
        for word in strs[1:]:
            i = 0
            prefix = ""
            for i in range(len(word)):
                if word[:i+1] not in prefix_set or i+1 > max_len:
                    break
                prefix = word[:i+1]
                i+=1
            longest_prefix = prefix
            max_len = i
            
        
        return longest_prefix