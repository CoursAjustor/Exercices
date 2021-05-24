class Exercice1():

    def main(self,age):
        print("Exercice 1")
        is_legal = self.checkAge(age)
        print(is_legal)
        return is_legal

    def checkAge(self, age):
        if age > 21 :
            return "oui"

        return "non"