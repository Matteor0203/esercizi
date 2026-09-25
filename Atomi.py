class Atomo:
    def __init__(self, simbolo, numero_atomico, massa): #tutti gli attributi nella classe si definiscono pubblici o public (posso accedere ad attributi della classe dall'esterno)
        if numero_atomico <= 0:
            raise ValueError("Il numero atomico deve essere maggiore di zero")
        
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico  
        self.massa = massa
        self.neutroni = round(massa) - numero_atomico
        self.__orbitale = "2p" #L'attributo orbitale è privato. Non lo posso utilizzare dall'esterno della classe.

    def stabile(self):
        protoni = self.numero_atomico
        
        rapporto = self.neutroni / protoni
        
        if 0.8 <= rapporto <= 1.6:
            print("L'atomo è stabile")
        else:
            print("L'atomo è instabile")
    
    def printOrbitale(self):
        print(self.__orbitale)
        
    def new_massa(self):
        self.massa = float(input("Inserisci la nuova massa"))
        
    def new_orbitale(self):
        self.__orbitale = int(input("Inserisci il nuomo numero di orbitali "))
        
    def nobile(self):
         ####primo metodo
        if self.numero_atomico == 2 or self.numero_atomico= 10 or self.numero_atomico == 18 or self.numero_atomico == 36 or == self.numero_atomico 54 or self.numero_atomico == 118:
            return True
        ####secondo metodo con lista
        nobili= [2,10,18...]  
        for numero in nobili:
            if numero == self.numero_atomico:
                return True
        ####terzo metodo
            if self.numero_atomico in nobili:
                return True

print(idrogeno.new_massa())
print(idrogeno.new_orbitale())

idrogeno = Atomo("H", 1, 1.008)
ferro = Atomo("Fe", 26, 55.845)

idrogeno.stabile()
ferro.stabile()

print(idrogeno.simbolo) #simbolo è un attributo e non una funzione, attributo pubblico che richiamo da esterno.
print(idrogeno.printOrbitale())

if idrogeno.nobile() == True:
    print("Gas Nobile")
else:
    print("Gas non nobile")



