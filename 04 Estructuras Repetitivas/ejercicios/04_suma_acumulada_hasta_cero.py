# 04_suma_acumulada_hasta_cero.py
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.


def main():
    total = 0
    while True:
        n = int(input("Ingresa un número (0 para finalizar): "))
        if n == 0:
            break
        total += n
    print(f"Total acumulado: {total}")

if __name__ == "__main__":
    main()