class Exercice2():

    def main(self,age):
        print("Exercice 1")
        is_legal = self.checkAge(age)
        print(is_legal)
        return is_legal

    def checkAge(self, age):
        if age > 21 :
            return "oui"

        elif age < 18 :
            return "non"

        return"oui sauf EU"
