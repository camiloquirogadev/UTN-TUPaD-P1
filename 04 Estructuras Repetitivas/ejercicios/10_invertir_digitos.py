# 10_invertir_digitos.py 
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

def invertir_digitos(n_str: str) -> str:
    signo = "-" if n_str.startswith("-") else ""
    digitos = n_str.lstrip("-")
    return signo + digitos[::-1]

def main():
    n = input("Ingresa un número: ")
    invertido = invertir_digitos(n)
    print(f"El número invertido es: {invertido}")

if __name__ == "__main__":
    main()