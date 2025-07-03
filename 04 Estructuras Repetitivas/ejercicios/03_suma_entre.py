# 03_suma_entre.py
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

def sumar_entre(a: int, b: int) -> int:
    inicio, fin = sorted((a, b))
    return sum(range(inicio + 1, fin))

def main():
    a, b = map(int, input("Ingresa dos valores separados por espacio: ").split())
    total = sumar_entre(a, b)
    print(f"La suma de los enteros entre {a} y {b} (excluidos) es: {total}")

if __name__ == "__main__":
    main()