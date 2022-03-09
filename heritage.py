class Animal :
    def __init__(self, name, espece):
        self.__name = name
        self.__espece = espece

    def espece(self):
        print(self.__espece)

    def appelNom(self):
        print(self.__name)
    
class Chat(Animal):
    def __init__(self, name):
        Animal.__init__(self,name,"chat")

    def etreChiant(self):
        print("Un chat à de nombreuses manières de vous emmerder.")

class Ratel(Animal):
    def __init__(self, name):
        Animal.__init__(self,name, "Ratel")
        
    def croqueCouille(self):
        print("Oui oui, le Rattel se défend en arrachant les couilles avec sa gueule.")
        
unChat = Chat("Silvestre")
unRatel = Ratel("Une belle saloperie")

unRatel.espece()
unRatel.appelNom()
unRatel.croqueCouille()
unChat.espece()
unChat.appelNom()
unChat.etreChiant()