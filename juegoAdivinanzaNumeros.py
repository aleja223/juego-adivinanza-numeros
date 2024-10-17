import random


def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras lineas de juego
    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un número
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo pasamos de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f" El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos."
                )
        else:
            print("Por favor introduzca un número válido entre el 1 al 100")


juego_adivinanza()
