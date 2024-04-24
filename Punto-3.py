def mover_zeros(ar):
    ultimo_cero = 0
    for i in range(len(ar)):
        if ar[i] != 0:
            ar[ultimo_cero], ar[i] = ar[i], ar[ultimo_cero]
            ultimo_cero += 1
    return ar
def escriba_numeros():
    arr = []
    while True:
        num = input("Escriba los numero (o 'fin' para detenerse)")
        if num.lower() == 'fin':
            break
        try:
            arr.append(int(num))
        except ValueError:
            print("Por favor, escriba un numero valido")
    return arr
print("Escriba los numeros (puedes escribir 'fin' para detenerse):")
arreglo = escriba_numeros()
print("Arreglo original:", arreglo)
arreglo_editado = mover_zeros(arreglo)
print("Arreglo con ceros al final:", arreglo_editado)