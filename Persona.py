import Cuenta_bancaria
import Tarjeta_bancaria


class Persona(Tarjeta_bancaria.Tarjeta_bancaria, Cuenta_bancaria.Cuenta_bancaria):
    """
    Permite asignarle a las personas una cuenta y una tarjeta bancaria
    """

    def __init__(self, nombre, dni, edad, num_tarj, estado, num_unico, clave):
        """
        Constructor que nos permite inicializar a una persona
        """
        self._nombre = nombre
        self._dni = dni
        self._edad = edad
        Tarjeta_bancaria.Tarjeta_bancaria.__init__(self, num_tarj, estado)
        Cuenta_bancaria.Cuenta_bancaria.__init__(self, num_unico, clave)
        #self.__tarjeta = tarjeta
        #self.__cuenta = cuenta

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, n):
        assert (len(n) < 12), "El nombre debe ser menor a 12 letras"
        self._nombre = n

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, n):
        assert (len(n) == 8), "El número de DNI debe ser de 8 dígitos"
        self._dni = n

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, n):
        assert (n > 0 and n < 100), "La edad de la persona debe ser entre 0 y 100 años"
        self._edad = n

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, n):
        pass

    @property
    def cuenta(self):
        return self.__cuenta

    @cuenta.setter
    def cuenta(self, n):
        pass
