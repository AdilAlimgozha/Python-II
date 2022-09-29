class Investment:
    def __init__(self, stavka, summa):
        self.stavka = stavka
        self.summa = summa
    
    def value_after(self,n):
        return (self.summa + self.stavka*0.1)

    def __str__(self):#overload print
        return f'summa(self,summa)'

deposit1 = Investment(10. 2000)
print(deposit