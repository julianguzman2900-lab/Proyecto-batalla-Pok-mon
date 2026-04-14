class Pokemon:
    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
        self.nombre = nombre
        self.__hp = hp_actual
        self.__hp_maximo = hp_maximo
        self.__energia = energia_actual
        self.__energia_maxima = energia_maxima

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, nuevo_hp):
        if nuevo_hp < 0:
            self.__hp = 0
        elif nuevo_hp > self.__hp_maximo:
            self.__hp = self.__hp_maximo
        else:
            self.__hp = nuevo_hp

    @property
    def hp_maximo(self):
        return self.__hp_maximo

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, nueva_energia):
        if nueva_energia < 0:
            self.__energia = 0
        elif nueva_energia > self.__energia_maxima:
            self.__energia = self.__energia_maxima
        else:
            self.__energia = nueva_energia

    @property
    def energia_maxima(self):
        return self.__energia_maxima
    
class PokemonAgua(Pokemon):
        def __init__(self, nombre, hp_actual, hp_maximo, energia_actual, energia_maxima):
            super().__init__(nombre, hp_actual, hp_maximo, energia_actual, energia_maxima)