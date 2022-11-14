class Solution:
    
    class TrieNode:
        def __init__(self):
            self.indeces = [None]*26
            self.isWord = False
    
    def addWord(self, root, word):
        for i in word:
            ind = ord(i) - ord('a')
            if root.indeces[ind] == None:
                root.indeces[ind] = self.TrieNode()
            root = root.indeces[ind]
        
        root.isWord = True
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # using Trie
        root = self.TrieNode()
        for word in wordDict:
            self.addWord(root, word)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            curr = root
            j = i
            while j <= n and curr != None:
                ind = ord(s[j-1])-ord('a')
                curr = curr.indeces[ind]
                if curr != None and curr.isWord and dp[i-1]:
                    dp[j] = True
                j += 1
            
            if dp[n]:
                break
        return dp[n]