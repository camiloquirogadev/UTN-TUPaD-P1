# 02_contar_digitos.py
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.


def contar_digitos(numero_str: str) -> int:
    # Excluye el signo si existe
    return len(numero_str.lstrip('-'))

def main():
    n = input("Ingresa un número entero: ")
    digitos = contar_digitos(n)
    print(f"El número {n} tiene {digitos} dígito{'s' if digitos != 1 else ''}.")

if __name__ == "__main__":
    main()