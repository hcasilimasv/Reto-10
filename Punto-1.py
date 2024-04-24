numeros = []
def calcular_promedio(real):
    suma = 0
    for n in real:
        suma += n
    promedio = suma / len(real)
    return promedio
while True:
    try:
        n = input("Escibe un numero real o escriba 'fin' para terminar: ")
        if n.lower() == 'fin':
            break
        else:
            n = float(n)
            numeros.append(n)
    except ValueError:
        print("Numero o digitación no valida. Por favor ingrese un número real.")
if numeros:
    promedio = calcular_promedio(numeros)
    print(f"El promedio de los numeros escrito es: {promedio}")
else:
    print("No se escribio ningun numeros.")