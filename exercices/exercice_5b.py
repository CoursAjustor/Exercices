class Exercice5b():

    def main(self):
        print("Exercice 5b")
        
    def draw(self, target):
        stars = 1 
        spaces = target-stars
        for i in range(1, target +1):
            #print(f"espaces {spaces}, etoiles {stars}")
            print(" " + spaces - "*" / stars)
            spaces -=1
            stars +=2 
