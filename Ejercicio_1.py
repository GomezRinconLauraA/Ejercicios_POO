def CALCULO_EDALBERTO(Juan):
    Alberto = float(Juan*(2/3))
    return Alberto

def CALCULO_EDANA(Juan):
    Ana = float(Juan*(4/3))
    return Ana

def CALCULO_EDMAMA(Juan):
    Mama = Juan + Alberto + Ana
    return Mama

Juan=float(input("Ingrese la edad de Juan "))

Alberto = CALCULO_EDALBERTO(Juan)
Ana = CALCULO_EDANA(Juan)
Mama = CALCULO_EDMAMA(Juan)

print(f"La edad de cada uno es:\n Juan:{Juan} \n Alberto:{Alberto:.2f} \n Ana:{Ana:.2f} \n Mama:{Mama:.2f}")

