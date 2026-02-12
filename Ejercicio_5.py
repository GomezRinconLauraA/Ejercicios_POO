import math

def calc_area(radio):
    area = math.pi * (radio ** 2)
    return area

def calc_longitud(radio):
    longitud = 2 * math.pi * radio
    return longitud


radio = float(input("Ingrese el radio del círculo: "))

area = calc_area(radio)
longitud = calc_longitud(radio)

print(f"El radio es: {radio:.2f}")
print(f"El area es: {area:.2f}")
print(f"La longitud de la circunferencia es: {longitud:.2f}")
