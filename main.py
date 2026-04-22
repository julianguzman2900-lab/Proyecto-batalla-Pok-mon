from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible  # importa el catálogo y función para mostrarlo
from pokemon_clases import *  # importa clases de Pokémon
import random  # permite usar funciones aleatorias

def crear_pokemon(datos_pokemon):  # crea un Pokémon según su tipo
    tipo = datos_pokemon["tipo"]  # obtiene el tipo

    if tipo == "Fuego":
        return PokemonFuego(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    elif tipo == "Agua":
        return PokemonAgua(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    elif tipo == "Planta":
        return PokemonPlanta(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    elif tipo == "Electrico":
        return PokemonElectrico(datos_pokemon["nombre"], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])


def elegir_pokemon(jugador):
    while True:  # while True crea un ciclo infinito que solo termina cuando se usa return
        try:
            opcion = int(input(f"{jugador}, elige tu Pokémon: "))  # intenta convertir la entrada a número

            # str(opcion) convierte el número a texto porque las claves del diccionario son strings
            # si no se convierte no coincidiría porque 1 es distinto a "1"
            if str(opcion) in CATALOGO_POKEMON:
                pokemon = crear_pokemon(CATALOGO_POKEMON[str(opcion)])
                print(f"Has seleccionado a {pokemon.nombre}")
                return pokemon  # return rompe el while True y termina la función

            else:
                print("Número no válido, intenta otra vez")

        except:
            # try/except evita que el programa se caiga si se escribe letras o símbolos
            print("Debes ingresar un número, no letras")


def turno(jugador, oponente, cpu=False):
    print(f"\nTURNO DE {jugador.nombre}")
    print(f"[HP: {jugador.hp_actual}] | [EP: {jugador.energia_actual}]")

    while True:  # se repite hasta que se elige una acción válida
        if cpu:
            accion = random.randint(1, 3)  # genera un número aleatorio entre 1 y 3
            print(f"Computadora elige: {accion}")
        else:
            try:
                accion = int(input("\n1.Atacar (Costo: 15 EP)\n2.Defender (Costo: 5 EP)\n3.Descansar (Restaura: 20 EP)\nOpción: "))
            except:
                print("Debes ingresar un número")
                accion = 0  # fuerza una opción inválida para repetir el ciclo

        if accion == 1:
            daño = jugador.atacar(oponente)
            print(f"{jugador.nombre} hizo {daño} de daño")
            break  # break rompe el while True y termina el turno

        elif accion == 2:
            jugador.defender()
            print(f"{jugador.nombre} se está defendiendo")
            break

        elif accion == 3:
            jugador.descansar()
            print(f"{jugador.nombre} recupera energía")
            break

        else:
            print("Opción inválida, intenta otra vez")


def batalla(jugador1, jugador2, contra_cpu=False):
    print("\n¡COMIENZA LA BATALLA!\n")

    while jugador1.hp_actual > 0 and jugador2.hp_actual > 0:
        turno(jugador1, jugador2)

        if jugador2.hp_actual <= 0:
            break

        turno(jugador2, jugador1, cpu=contra_cpu)

    if jugador1.hp_actual > 0:
        print(f"\n{jugador1.nombre} gana!")
    else:
        print(f"\n{jugador2.nombre} gana!")


def main():
    print("="*45)
    print("SIMULADOR DE BATALLAS POKÉMON")
    print("="*45)

    print("Seleccione el modo de juego")
    print("1. Jugador vs Jugador")
    print("2. Jugador vs Computadora")

    try:
        opcion_batalla = int(input("Opción: "))  # elige una opcion
    except:
        # evita que el programa falle si el usuario escribe algo inválido
        print("Debes ingresar un número")
        return

    mostrar_catalogo_disponible()

    jugador1 = elegir_pokemon("Jugador 1")

    if opcion_batalla == 1:
        jugador2 = elegir_pokemon("Jugador 2")
        batalla(jugador1, jugador2)

    elif opcion_batalla == 2:
        # random.choice elige un elemento aleatorio de una lista
        # list(CATALOGO_POKEMON) convierte las claves del diccionario en lista
        numero = random.choice(list(CATALOGO_POKEMON))
        jugador2 = crear_pokemon(CATALOGO_POKEMON[numero])
        print(f"La computadora eligió a {jugador2.nombre}")
        batalla(jugador1, jugador2, contra_cpu=True)

    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()