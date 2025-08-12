from persona import Persona
from tamagotchi import Tamagotchi

def menu_interactivo():
    print("=== Bienvenido a tu Tamagotchi ===")
    nombre_persona = input("Ingresa tu nombre: ")
    apellido_persona = input("Ingresa tu apellido: ")
    nombre_tamagotchi = input("Nombre de tu Tamagotchi: ")
    color_tamagotchi = input("Color de tu Tamagotchi: ")

    tamagotchi = Tamagotchi(nombre_tamagotchi, color_tamagotchi)
    persona = Persona(nombre_persona, apellido_persona, tamagotchi)

    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Ver estado del Tamagotchi")
        print("2. Darle de comer")
        print("3. Jugar con él")
        print("4. Curarlo")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            tamagotchi.mostrar_estado()
        elif opcion == "2":
            persona.darle_comida()
        elif opcion == "3":
            persona.jugar_con_tamagotchi()
        elif opcion == "4":
            persona.curarlo()
        elif opcion == "5":
            print("¡Hasta luego! Gracias por cuidar de tu Tamagotchi.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_interactivo()