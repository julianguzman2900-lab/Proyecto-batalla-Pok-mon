from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import *
import random


def crear_pokemon(datos_pokemon):
    tipo = datos_pokemon["tipo"]

    if tipo == "Fuego":
        return PokemonFuego(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    elif tipo == "Agua":
        return PokemonAgua(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    elif tipo == "Planta":
        return PokemonPlanta(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    elif tipo == "Electrico":
        return PokemonElectrico(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])


def elegir_pokemon(jugador):
    while True:
        try:
            opcion = input(f"{jugador}, elige tu Pokémon: ")
            if opcion in CATALOGO_POKEMON:
                pokemon = crear_pokemon(CATALOGO_POKEMON[opcion])
                print(f"Has seleccionado a {pokemon.nombre}")
                return pokemon
        except:
            print("Entrada inválida")


def turno(jugador, oponente, computadora=False):
    print(f"\nTURNO DE {jugador.nombre}")
    print(f"[HP: {jugador.hp_actual}] | [EP: {jugador.energia_actual}]")

    if computadora:
        accion = random.randint(1, 3)
        print(f"Computadora elige: {accion}")
    else:
        try:
            accion = int(input("1.Atacar 2.Defender 3.Descansar: "))
        except:
            print("Entrada inválida")
            return

    if accion == 1:
        daño = jugador.atacar(oponente)
        print(f"{jugador.nombre} hizo {daño} de daño")

    elif accion == 2:
        jugador.defender()
        print(f"{jugador.nombre} se está defendiendo")

    elif accion == 3:
        jugador.descansar()
        print(f"{jugador.nombre} recupera energía")


