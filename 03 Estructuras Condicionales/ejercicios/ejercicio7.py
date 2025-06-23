texto = input("Ingresá una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)