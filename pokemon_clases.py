from abc import ABC, abstractmethod 
import random

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.__hp_actual = hp_maximo
        self.__hp_maximo = hp_maximo
        self.__energia_actual = energia_maxima
        self.__energia_maxima = energia_maxima
        self.defendiendo = False
     

    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self.__hp_actual = 0
        elif valor > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo
        else:
            self.__hp_actual = valor

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        else:
            self.__energia_actual = valor

    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True

    def descansar(self):
        self.energia_actual += 20

    @abstractmethod
    def atacar(self, oponente):
        pass

class PokemonAgua(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15:
            return 0

        self.energia_actual -= 15
        daño = 15

        if isinstance(oponente, PokemonFuego):
            daño *= 2

        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False

        oponente.hp_actual -= daño
        return daño
    
class PokemonFuego(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15:
            return 0

        self.energia_actual -= 15
        daño = 15

        if isinstance(oponente, PokemonPlanta):
            daño *= 2

        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False

        oponente.hp_actual -= daño
        return daño
    
class PokemonPlanta(Pokemon):
    def atacar(self, oponente):
        if self.energia_actual < 15:
            return 0

        self.energia_actual -= 15
        daño = 15

        if isinstance(oponente, PokemonAgua):
            daño *= 2

        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False

        oponente.hp_actual -= daño
        return daño

class PokemonElectrico(Pokemon):
    def atacar(self, oponente):
      
        if self.energia_actual < 15:
            return 0
        self.energia_actual -= 15
        daño = 15
        if oponente.defendiendo:
            daño //= 2
            oponente.defendiendo = False

        oponente.hp_actual -= daño
        return daño
            