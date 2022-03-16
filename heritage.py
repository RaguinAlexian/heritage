class Animal :
    def __init__(self, name, espece):
        self.__name = name
        self.__espece = espece

    def espece(self):
        return self.__espece

    def appelNom(self):
        return self.__name

    def comportement(self):
        txt = "Chaque animal à son propre comportement"
        return txt
    
class Chat(Animal):
    def __init__(self, name):
        Animal.__init__(self,name,"Chat")

    def comportement(self):
        text = "avec de nombreuses manières, vous emmerder."
        return text

class Ratel(Animal):
    def __init__(self, name):
        Animal.__init__(self,name,"Ratel")
        
    def comportement(self):
        text = "se défendre en arrachant les couilles avec sa gueule."
        return text
        
choixAnimal = input("Quel animal voulez-vous prendre ? 1-Chat 2-Ratel (choisissez le chiffre) : ")
if(choixAnimal == "1"):
    choixNom = input("Veuillez insérer le nom de votre animal : ")
    monAnimal = Chat(choixNom)
else :
    choixNom = input("Veuillez insérer le nom de votre animal : ")
    monAnimal = Ratel(choixNom)

print(monAnimal.appelNom() , "est un" , monAnimal.espece() , "et peut" , monAnimal.comportement())
if(isinstance(monAnimal,Ratel)):
    print(monAnimal.appelNom(),"semble particulièrement agressif, pensez à acheter des protèges tibia et une coque pour votre slip")
