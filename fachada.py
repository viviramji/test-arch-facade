from subsistemas.pelarPapas import PelarPapas
from subsistemas.freir import Freir
from subsistemas.servir import Servir


class Fachada():
    numero_de_platos = 0

    def obtener_numero_platos(self):
        return f"El número de platos de la jornada fue {self.numero_de_platos}"
    
    def hacer_salchipapa(self):
        self.pelar_papas = PelarPapas()
        self.pelar_papas.pelar_papas()

        self.freir = Freir()
        self.freir.cocinar_salchipapa()

        self.servir = Servir()
        self.servir.servir_papas()

        self.numero_de_platos = self.numero_de_platos  + 1
