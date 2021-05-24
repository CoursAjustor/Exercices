class Exercice4():

    def main(self, target):
        print("Exercice 4")
        counterEvent = self.countEven(target)
        print(counterEvent)
        return counterEvent

    def countEven(self, target):
        return list(range(2, target+1, 2)) 
