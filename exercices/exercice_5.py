class Exercice5():

    def main(self, target):
        print("Exercice 5")
        drawPyramid = self.drawPyramid(target)
        print()
        return drawPyramid

    
    def drawPyramid(self, target):
        stars = 1 
        spaces = target-stars
        for i in range(1, target +1):
            #print(f"espaces {spaces}, etoiles {stars}")
            print(" " * spaces + "*" * stars)
            spaces -=1
            stars +=2 