#programma che simula un piano cartesiano e che sia in grado di calcolare la distanza tra due punti
#verificare se i punti sono posizionati sugli assi appure no e su quale sono posizionati.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanza(self, secondoPunto):
        return math.sqrt((self.x - secondoPunto.x) ** 2 + (self.y - secondoPunto.y) ** 2)
        
    def IsAscissa(self):
        if self.x == 0:
            print("Il punto si trova sull'asse Y")
            
     def IsOrdinata(self):
        if self.y == 0:
            print("Il punto si trova sull'asse X")
            
if __name__ == "main":
        
puntoUno = Punto(0, 5) 
puntoDue = Punto(4, 0)  

dist = puntoUno.distanza(puntoDue)
print("La distanza tra i due punti è", dist)
