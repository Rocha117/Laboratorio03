import Cuenta_bancaria
import Persona


class Cajero_automatico(Persona):
    """
    Permite almacenar y autenticar a las personas registradas en el banco
    """

    personas = []  # Esta lista contendrá objetos de la clase Persona

    def __init__(self, dinero, personas=[]):
        """
        Constructor que nos permite inicializar al cajero automático
        """
        self.personas = personas
        self.dinero = dinero

    @property
    def dinero(self):
        """
        Permite editar la propiedad de cantidad total de dinero almacenada en la tarjeta bancaria de la persona
        """
        return self.dinero

    @dinero.setter
    # Ejecuta la operacion de depositar (1) o retirar (2) dinero de la tarjeta bancaria de la persona
    def dinero(self, operacion, n):
        if operacion == 1:
            self.dinero = self.dinero+int(n)
        elif operacion == 2:
            self.dinero = self.dinero-int(n)

    @property
    def person(self):
        return self.personas

    @person.setter
    def person(self, p):  # p será un objeto Persona
        self.personas.append(p)

    @property
    def cuenta(self):
        return self.personas
