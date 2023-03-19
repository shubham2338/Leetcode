class Trie:
    def __init__(self):
        self.ch={}
        self.word=False

class WordDictionary(object):

    def __init__(self):
        self.root = Trie()

    def addWord(self, word):
        cur=self.root
        for c in word:
            if c not in cur.ch:
                cur.ch[c]=Trie()
            cur=cur.ch[c]
        cur.word=True
        
    def search(self, word):
        def dfs(j,root):
            cur=root
            for i in range(j,len(word)):
                c=word[i]
                if c=='.':
                    for child in cur.ch.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.ch:
                        return False
                    cur=cur.ch[c]
            
            return cur.word
        return dfs(0,self.root)
            
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)