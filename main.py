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

        if accion == 1:  # opción atacar
            daño = jugador.atacar(oponente)  # ejecuta el ataque
            print(f"{jugador.nombre} hizo {daño} de daño")  # muestra el daño causado
            print("--------------------------------------")
            break  # termina el turno

        elif accion == 2:  # opción defender
            jugador.defender()  # activa defensa
            print(f"{jugador.nombre} se está defendiendo")  # mensaje
            print("--------------------------------------") 
            break  # termina el turno

        elif accion == 3:  # opción descansar
            jugador.descansar()  # recupera energía
            print(f"{jugador.nombre} recupera energía")  # mensaje
            print("--------------------------------------")
            break  # termina el turno

        else:
            print("Opción inválida, intenta otra vez")  # si la opción no es válida



def batalla(jugador1, jugador2, contra_cpu=False):  # controla toda la batalla
    print("\n¡COMIENZA LA BATALLA!\n")  # mensaje inicial
    print(f"{jugador1.nombre} VS {jugador2.nombre} ")  # muestra los Pokémon que van a pelear

    while jugador1.hp_actual > 0 and jugador2.hp_actual > 0:  # continúa mientras ambos tengan vida
        turno(jugador1, jugador2)  # turno del jugador 1

        if jugador2.hp_actual <= 0:  # si jugador 2 pierde toda su vida
            break  # termina la batalla

        turno(jugador2, jugador1, cpu=contra_cpu)  # turno del jugador 2 o CPU

    if jugador1.hp_actual > 0:  # verifica quién sigue con vida
        print(f"\n{jugador1.nombre} gana!")  # gana jugador 1
    else:
        print(f"\n{jugador2.nombre} gana!")  # gana jugador 2

def main():
    print("="*45)
    print("      SIMULADOR DE BATALLAS POKÉMON")
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

    mostrar_catalogo_disponible()  # muestra lista de Pokémon disponibles

    jugador1 = elegir_pokemon("Jugador 1")  # jugador 1 elige

    if opcion_batalla == 1:  # modo jugador vs jugador
        jugador2 = elegir_pokemon("Jugador 2")  # jugador 2 elige
        batalla(jugador1, jugador2)  # inicia batalla

    elif opcion_batalla == 2:
        # random.choice elige un elemento aleatorio de una lista
        # list(CATALOGO_POKEMON) convierte las claves del diccionario en lista
        numero = random.choice(list(CATALOGO_POKEMON))
        jugador2 = crear_pokemon(CATALOGO_POKEMON[numero])  # crea el Pokémon de la CPU
        print(f"La computadora eligió a {jugador2.nombre}")  # muestra elección
        batalla(jugador1, jugador2, contra_cpu=True)  # inicia batalla contra CPU

    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()