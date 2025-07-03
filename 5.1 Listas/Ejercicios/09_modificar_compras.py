def main():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    idx = compras[1].index("fideos")
    compras[1][idx] = "tallarines"
    compras[0].remove("pan")
    print(compras)

if __name__ == "__main__":
    main()