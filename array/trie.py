
class Contact {
    String firstName;
    String lastName;
    String email;
}


def autocomplete(input):
    list_of_contacts = []
    t = trie()
    c = Contact("Piyush", "Sharma", "p.s@gmail.com")
    c2 = Contact("Piyash", "Chawla", "p.c@gmail.com")
    t.insert("Piyush", c)
    t.insert("Piyash", c2)
    
    #t.insert("Piyush Singhai")
    #t.insert("Piyush Chawla")
    #t.insert("Yush")
    #t.search("Piy")
    
    return list_of_contacts

class trie():
    def __init__(self):
        self.root = dict()
        self.contacts = []
        
    def insert(self, word, contact):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end", contact)
        
    def search(self, word):
        contacts = []
        current = self.root        
        for letter in word:
            if letter not in current:
                return False, []
            current = current[letter]
             
        while "_end" not in current:
            
     
                  
        return True, contacts
        
        
        
        




c = {}
c[p] = {I: {}}
if p in c:
    current = c[p]
i
y
