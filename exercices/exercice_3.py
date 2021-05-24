class Exercice3():

    def main(self, target):
        print("Exercice 3")
        count = self.count(target)
        print(count)
        return count

    def count(self, target):
        return list(range(1, target+1)) 

