class Wordplay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, length):
        for word in self.words:
            if length == len(word):
                print(word)

    def starts_with(self, letter):
        for word in self.words:
            if word[0] == letter:
                print(word)

    def ends_with(self, letter):
        for word in self.words:
            if word[len(word) - 1] == letter:
                print(word)

    def palindromes(self):
        for word in self.words:
            rev = word[::-1]
            if word == rev:
                print(word)

    def only(self, L):
        a = []
        for word in self.words:
            flag = True
            for Lletter in L:
                if Lletter in word:
                    continue
                else:
                    flag = False
                    break
            if flag:    
                a.append(word)
        print(a)

    def avoids(self, L):
        a = []
        for word in self.words:
            flag = True
            for Lletter in L:
                if Lletter in word:
                    flag = False
                    break
                else:
                    continue
            if flag:    
                a.append(word)
        print(a)


a = ['house', 'shelter', 'car', 'university', 'cat', 'word', 'man', 'horse', 'qazaq', 'lol']
wordplay = Wordplay(a)
wordplay.words_with_length(3)
print()
wordplay.starts_with('h')
print()
wordplay.ends_with('r')
print()
wordplay.palindromes()
print()
wordplay.only(['s', 'h'])
print()
wordplay.avoids(['c', 'a'])