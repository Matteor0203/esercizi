#programma che gestisce nome, cognome, età di due persone

noma_prima = "Tommaso"
cognome_prima = "STRA"
eta_prima = 25 
noma_seconda = "Luigi"
cognome_seconda = "Rossi"
eta_seconda = 28

print("Età prima persona")
print(eta_prima)
print("Età seconda persona")
print(eta_seconda)

#uso degli oggetti

class Persona:
    def _int_(nome,cognome,eta,lavoro):     #costruttore che inizializza
        self.nome = nome    
        self.cognome = cognome
        self.eta = eta
        self.lavoro = lavoro
    def stampaEta(self):
        print(self.eta)
    def stampaLavoro(self):
        print(self.lavoro)
    def maggiorenne(self):
        if self.eta >= 18:
            print("Maggiorenne")
        else:
            print("Minorenne")
    
    
prima_persona = Persona("Tommaso","STRA",25,"Dottore")     #istanza della persona (specifico oggetto della classe persona)
seconda_persona = Persona("Luigi","Rossi",28,"Avvocato")
prima_persona.stampaEta()
seconda_persona.stampaEta()
prima_persona.stampaLavoro()
seconda_persona.stampaLavoro()






