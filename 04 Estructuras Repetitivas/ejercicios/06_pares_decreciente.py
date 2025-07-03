# 06_pares_decreciente.py
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.




def main():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    main()
