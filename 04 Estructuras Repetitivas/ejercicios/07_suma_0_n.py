# 07_suma_0_n.py
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.


def sumar_hasta(n: int) -> int:
    return sum(range(n + 1))

def main():
    n = int(input("Ingresa un entero positivo: "))
    total = sumar_hasta(n)
    print(f"La suma de 0 a {n} es: {total}")

if __name__ == "__main__":
    main()