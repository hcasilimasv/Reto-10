def ingresar_vector():
    inicio = input("Escribe tres o mas numeros separados por comas para calcular el vector (por ejemplo, 1, 2, 3): ")
    try:
        vec = [float(num) for num in inicio.split(",")]
        return vec
    except ValueError:
        print("Se ejecuta un error, escibe los  numeros separados por coma")
        return ingresar_vector()
def producto_punto(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma longitud")
    resultado = 0
    for i in range(len(v1)):
        resultado += v1[i] * v2[i]
    return resultado
print("Escriba los valores para el primer vector:")
vec1 = ingresar_vector()
print("Escriba los valores para el segundo vector:")
vec2 = ingresar_vector()
try:
    resultado_producto_punto = producto_punto(vec1, vec2)
    print(f"El producto punto entre {vec1} y {vec2} es: {resultado_producto_punto}")
except ValueError as e:
    print(e)