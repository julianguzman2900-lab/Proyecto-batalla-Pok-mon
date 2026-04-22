
from abc import ABC, abstractmethod  # importa lo necesario para usar clases abstractas

class Pokemon(ABC):  # clase base de la que heredan todos los Pokémon
    def __init__(self, nombre, hp_maximo, energia_maxima):  # constructor que se ejecuta al crear el objeto
        self.nombre = nombre  # guarda el nombre del Pokémon para identificarlo
        self.__hp_actual = hp_maximo  # la vida actual inicia con el valor máximo
        self.__hp_maximo = hp_maximo  # guarda el límite máximo de vida
        self.__energia_actual = energia_maxima  # la energía actual inicia llena
        self.__energia_maxima = energia_maxima  # guarda el límite máximo de energía
        self.defendiendo = False  # indica si el Pokémon está en modo defensa

    @property
    def hp_actual(self):  # permite acceder a la vida como si fuera un atributo
        return self.__hp_actual  # devuelve el valor actual de vida

    @hp_actual.setter
    def hp_actual(self, valor_vida):  # controla cómo se modifica la vida
        if valor_vida < 0:  # si el nuevo valor es menor que cero
            self.__hp_actual = 0  # evita que la vida sea negativa
        elif valor_vida > self.__hp_maximo:  # si el valor supera el máximo permitido
            self.__hp_actual = self.__hp_maximo  # limita la vida al máximo
        else:
            self.__hp_actual = valor_vida  # si es válido, asigna el valor

    @property
    def energia_actual(self):  # permite leer la energía actual
        return self.__energia_actual  # devuelve la energía actual

    @energia_actual.setter
    def energia_actual(self, valor_energia):  # controla cambios en la energía
        if valor_energia < 0:  # si baja de cero
            self.__energia_actual = 0  # evita valores negativos
        elif valor_energia > self.__energia_maxima:  # si supera el máximo
            self.__energia_actual = self.__energia_maxima  # limita al máximo permitido
        else:
            self.__energia_actual = valor_energia  # asigna el valor si es válido

    def defender(self):  # método para activar defensa
        if self.energia_actual >= 5:  # revisa si tiene energía suficiente
            self.energia_actual -= 5  # descuenta el costo de defender
            self.defendiendo = True  # activa el estado de defensa
        else:
            print(f"{self.nombre} no tiene suficiente energía")  # avisa si no puede defender

    def descansar(self):  # método para recuperar energía
        self.energia_actual += 20  # suma energía al Pokémon

    @abstractmethod
    def atacar(self, oponente):  # método que cada tipo debe implementar
        pass  # no se define aquí porque cambia según el tipo


class PokemonAgua(Pokemon):  # clase para Pokémon tipo agua
    def atacar(self, oponente):  # método de ataque
        if self.energia_actual < 15:  # verifica si puede atacar
            print(f"{self.nombre} no tiene suficiente energía")  # mensaje si no puede
            return 0  # no hace daño

        self.energia_actual -= 15  # descuenta la energía usada en el ataque
        daño = 15  # daño base del ataque

        if isinstance(oponente, PokemonFuego):  # revisa si tiene ventaja de tipo
            daño *= 2  # duplica el daño por ventaja

        if oponente.defendiendo:  # revisa si el oponente se defendió
            daño //= 2  # reduce el daño recibido
            oponente.defendiendo = False  # quita el estado de defensa después del golpe

        oponente.hp_actual -= daño  # resta la vida del oponente
        return daño  # devuelve el daño causado


class PokemonFuego(Pokemon):  # clase para Pokémon tipo fuego
    def atacar(self, oponente):
        if self.energia_actual < 15:  # verifica energía suficiente
            print(f"{self.nombre} no tiene suficiente energía")
            return 0

        self.energia_actual -= 15  # descuenta energía
        daño = 15  # daño base

        if isinstance(oponente, PokemonPlanta):  # ventaja contra planta
            daño *= 2  # duplica daño

        if oponente.defendiendo:  # si el oponente está defendiendo
            daño //= 2  # reduce daño
            oponente.defendiendo = False  # quita defensa

        oponente.hp_actual -= daño  # aplica daño
        return daño  # retorna daño


class PokemonPlanta(Pokemon):  # clase para Pokémon tipo planta
    def atacar(self, oponente):
        if self.energia_actual < 15:  # verifica energía
            print(f"{self.nombre} no tiene suficiente energía")
            return 0

        self.energia_actual -= 15  # descuenta energía
        daño = 15  # daño base

        if isinstance(oponente, PokemonAgua):  # ventaja contra agua
            daño *= 2  # duplica daño

        if oponente.defendiendo:  # si el oponente está defendiendo
            daño //= 2  # reduce daño
            oponente.defendiendo = False  # quita defensa

        oponente.hp_actual -= daño  # aplica daño
        return daño  # retorna daño


class PokemonElectrico(Pokemon):  # clase para Pokémon tipo eléctrico
    def atacar(self, oponente):
        if self.energia_actual < 15:  # verifica energía
            print(f"{self.nombre} no tiene suficiente energía")
            return 0

        self.energia_actual -= 15  # descuenta energía
        daño = 15  # daño base

        if oponente.defendiendo:  # si el oponente está defendiendo
            daño //= 2  # reduce daño
            oponente.defendiendo = False  # quita defensa

        oponente.hp_actual -= daño  # aplica daño
        return daño  # retorna daño