#programma che simula un piano cartesiano e che sia in grado di calcolare la distanza tra due punti
#verificare se i punti sono posizionati sugli assi appure no e su quale sono posizionati.
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distanza(self, secondoPunto):
        return math.sqrt((self.x - secondoPunto.x) ** 2 + (self.y - secondoPunto.y) ** 2)
        
    def IsAscissa(self):
        if self.x == 0:
            return True
        else:
            return False
            
    def IsOrdinata(self):
        if self.y == 0:
            return True
        else:
            return False
            
        
puntoUno = Punto(0, 5)
puntoDue = Punto(4, 0)  

if puntoUno.IsAscissa() == True:
    print("Il primo punto si trova sull'asse Y")
    
if puntoDue.IsOrdinata() == True:
    print("Il secondo punto si trova sull'asse X")
    
if puntoDue.IsAscissa() == True:
    print("Il secondo punto si trova sull'asse Y")
    
if puntoUno.IsOrdinata() == True:
    print("Il primo punto si trova sull'asse X")

dist = puntoUno.distanza(puntoDue)
print("La distanza tra i due punti è", dist)
