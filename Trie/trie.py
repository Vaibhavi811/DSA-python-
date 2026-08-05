class trienode:
    def __init__(self):
        self.children= [None]*26
        self.eow= False

class Trie:
    def __init__(self):
        self.root= trienode()
    
    def insert(self,word):
        ptr= self.root
        for key in word:
            index= ord(key)- ord('a')

            if ptr.children[index] is None:
                ptr.children[index]= trienode()

            ptr= ptr.children[index]
        
        ptr.eow= True

    def search(self,word):
        ptr= self.root
        for key in word:
            index= ord(key)- ord('a')

            if ptr.children[index] is None:
                return False
            
            ptr= ptr.children[index]

    
        return ptr.eow
        
    def prefix(self,word):
        ptr= self.root
        for key in word:
            index= ord(key)- ord('a')

            if ptr.children[index] is None:
                return False
            ptr= ptr.children[index]

        return True

t= Trie()   
words=["cat","can","dog","cow","catfish"]
for word in words:
    t.insert(word)

search_words=["can","do","cow","jellyfish"]
for word in search_words:
    print(t.search(word))

print()

prefix=["co","do","it","v"]
for word in prefix:
    print(t.prefix(word))


