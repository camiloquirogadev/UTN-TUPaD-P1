def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    cuenta = 1 if ultimo == digito else 0
    return cuenta + contar_digito(numero // 10, digito)
