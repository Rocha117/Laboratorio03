import Tarjeta_bancaria
import Cuenta_bancaria


class Persona(Tarjeta_bancaria, Cuenta_bancaria):
    """
    Permite asignarle a las personas una cuenta y una tarjeta bancaria
    """

    def __init__(self, nombre, dni, edad,  num_tarj, estado, num_unico, clave):
        """
        Constructor que nos permite inicializar a una persona
        """
        self._nombre = nombre
        self._dni = dni
        self._edad = edad
        Tarjeta_bancaria.__init__(self, num_tarj, estado)
        Cuenta_bancaria.__init__(self, num_unico, clave)

    @property
    def nombre(self):
        """
        Permite editar la propiedad de nombre a la persona
        """
        return self._nombre

    @nombre.setter
    def nombre(self, n):  # Establece un límite de 12 letras para el nombre
        assert (len(n) < 12), "El nombre debe ser menor a 12 letras"
        self._nombre = n

    @property
    def dni(self):
        """
        Permite editar la propiedad de DNI a la persona
        """
        return self._dni

    @dni.setter
    def dni(self, n):  # Establece un límite de 8 dígitos para el DNI
        assert (len(n) == 8), "El número de DNI debe ser de 8 dígitos"
        self._dni = n

    @property
    def edad(self):
        """
        Permite editar la propiedad de edad a la persona
        """
        return self._edad

    @edad.setter
    def edad(self, n):  # Establece un rango para la edad entre 18 y 100 años
        assert (n >= 18 and n <=
                100), "La edad de la persona debe ser entre 18 y 100 años"
        self._edad = n
