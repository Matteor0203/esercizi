import math

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

if __name__ == "__main__":
    puntoUno = Punto(11, 10)
    puntoDue = Punto(7, 9)
    puntoUno.IsAscissa()
    puntoDue.IsOrdinata()
    dist = puntoUno.distanza(puntoDue)
    print("La distanza tra i due punti è", dist)
