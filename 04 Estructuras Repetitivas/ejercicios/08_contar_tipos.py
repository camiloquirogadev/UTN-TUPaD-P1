# 08_contar_tipos.py
# 
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).


def main():
    pares = impares = negativos = positivos = 0
    cantidad = 100  # Cambiar este valor para probar con menos elementos

    for i in range(cantidad):
        x = int(input(f"Número {i+1}/{cantidad}: "))
        if x % 2 == 0:
            pares += 1
        else:
            impares += 1
        if x > 0:
            positivos += 1
        elif x < 0:
            negativos += 1

    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")

if __name__ == "__main__":
    main()