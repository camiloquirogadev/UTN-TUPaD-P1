nombre = input("Ingresá tu nombre: ")
opcion = int(input("Elegí una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera en mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")