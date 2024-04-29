# Reto-10

#### Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_10 en slack.

#### 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

``` python
# Lista para almacenar los números ingresados
numeros = []

# Función para calcular el promedio de una lista de números reales
def calcular_promedio(real):
    suma = 0
    for n in real:
        suma += n
    promedio = suma / len(real)
    return promedio

# Bucle para solicitar números al usuario
while True:
    try:

        # Solicita al usuario que ingrese un número o 'fin' para terminar
        n = input("Escribe un número real o escribe 'fin' para terminar: ")

        # Si el usuario escribe 'fin', termina el bucle
        if n.lower() == 'fin':
            break
        else:

            # Convierte la entrada del usuario a tipo float y la agrega a la lista de números
            n = float(n)
            numeros.append(n)

    # Manejo de excepciones para la conversión de la entrada a float
    except ValueError:
        print("Número o digitación no válida. Por favor ingrese un número real.")

# Si hay números en la lista, calcula y muestra el promedio
if numeros:
    promedio = calcular_promedio(numeros)
    print(f"El promedio de los números escritos es: {promedio}")
else:

    # Si no se escribió ningún número, muestra un mensaje indicando eso
    print("No se escribió ningún número.")
```


#### 2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/) de dos arreglos de números enteros (reales) de igual tamaño.

```python
# Función para solicitar al usuario que ingrese un vector
def ingresar_vector():
    inicio = input("Escribe tres o más números separados por comas para calcular el vector (por ejemplo, 1, 2, 3): ")
    try:

        # Convierte la entrada del usuario en una lista de números flotantes
        vec = [float(num) for num in inicio.split(",")]
        return vec
    except ValueError:

        # Si ocurre un error al convertir la entrada a flotante, solicita al usuario que vuelva a intentarlo
        print("Se ejecutó un error, escribe los números separados por coma.")
        return ingresar_vector()

# Función para calcular el producto punto entre dos vectores
def producto_punto(v1, v2):

    # Verifica si los vectores tienen la misma longitud
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma longitud")
    resultado = 0

    # Calcula el producto punto sumando el producto de los elementos correspondientes de los vectores
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]
    return resultado

# Solicita al usuario que ingrese los valores para el primer vector
print("Escriba los valores para el primer vector:")
vec1 = ingresar_vector()

# Solicita al usuario que ingrese los valores para el segundo vector
print("Escriba los valores para el segundo vector:")
vec2 = ingresar_vector()
try:

    # Calcula el producto punto entre los dos vectores ingresados por el usuario
    resultado_producto_punto = producto_punto(vec1, vec2)

    # Muestra el resultado del producto punto
    print(f"El producto punto entre {vec1} y {vec2} es: {resultado_producto_punto}")
except ValueError as e:

    # Si los vectores no tienen la misma longitud, muestra un mensaje de error
    print(e)
```


#### 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo

``` python
# Función para mover los ceros al final de un arreglo
def mover_zeros(ar):

    # Variable para almacenar la posición del último cero encontrado
    ultimo_cero = 0

    # Itera sobre el arreglo
    for i in range(len(ar)):

        # Si el elemento actual no es cero
        if ar[i] != 0:

            # Intercambia el elemento actual con el último cero encontrado (si lo hay)
            ar[ultimo_cero], ar[i] = ar[i], ar[ultimo_cero]

            # Incrementa la posición del último cero encontrado
            ultimo_cero += 1
    return ar

# Función para que el usuario escriba números
def escriba_numeros():
    arr = []
    while True:

        # Solicita al usuario que ingrese un número (o 'fin' para detenerse)
        num = input("Escriba los números (o 'fin' para detenerse): ")
        if num.lower() == 'fin':
            break
        try:

            # Convierte la entrada del usuario a tipo entero y la agrega al arreglo
            arr.append(int(num))
        except ValueError:

            # Si ocurre un error al convertir la entrada a entero, muestra un mensaje de error
            print("Por favor, escriba un número válido.")
    return arr

# Solicita al usuario que escriba los números
print("Escriba los números (puedes escribir 'fin' para detenerse):")
arreglo = escriba_numeros()

# Muestra el arreglo original ingresado por el usuario
print("Arreglo original:", arreglo)

# Aplica la función para mover los ceros al final del arreglo
arreglo_editado = mover_zeros(arreglo)

# Muestra el arreglo con los ceros movidos al final
print("Arreglo con ceros al final:", arreglo_editado)
```


#### 4. Revisar que son los algoritmos de sorting, entender bubble-sort ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).
