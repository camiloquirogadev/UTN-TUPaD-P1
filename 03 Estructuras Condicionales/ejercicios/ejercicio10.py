hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingresá el mes (1-12): "))
dia = int(input("Ingresá el día (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte, estacion_sur = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte, estacion_sur = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte, estacion_sur = "Verano", "Invierno"
else:
    estacion_norte, estacion_sur = "Otoño", "Primavera"

if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio inválido")