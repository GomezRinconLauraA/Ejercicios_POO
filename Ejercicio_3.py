def calc_bruto(horas, valor_hora):
    bruto = int(horas * valor_hora)
    return bruto

def calc_retencion(bruto):
    retencion = int(bruto * 0.125)
    return retencion

def calc_neto(bruto, retencion):
    neto = int(bruto - retencion)
    return neto


horas = 48
valor_hora = 5000

bruto = calc_bruto(horas, valor_hora)
retencion = calc_retencion(bruto)
neto = calc_neto(bruto, retencion)

print("El salario bruto es:", bruto)
print("La retención es:", retencion)
print("El salario neto es:", neto)
