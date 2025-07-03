# 05_juego_adivinar.py
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.



import random

def main():
    secreto = random.randint(0, 9)
    intentos = 0

    while True:
        intento = int(input("Adivina el número (0–9): "))
        intentos += 1
        if intento == secreto:
            print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
            break
        else:
            print("Incorrecto, vuelve a intentar.")

if __name__ == "__main__":
    main()