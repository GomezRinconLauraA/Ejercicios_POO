def calc_cuadrado(numero):
    cuadrado = float(numero**2)
    return cuadrado

def calc_cubo(numero):
    cubo = float(numero**3)
    return cubo


numero = float(input("Ingrese un número: "))

cuadrado = calc_cuadrado(numero)
cubo = calc_cubo(numero)

print(f"El número es: {numero:.2f}")
print(f"El cuadrado es: {cuadrado:.2f}")
print(f"El cubo es: {cubo:.2f}")