class Exercice4b():

    def main(self, target):
        print("Exercice 4b")
        counterOdd = self.counterOdd(target)
        print(counterOdd)
        return counterOdd

    def counterOdd(self, target):
        return list(range(1, target+1, 2)) 

