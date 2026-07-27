class Pedido: #Define objetos tipo Pedido de un restaurante que consta de diferentes platos y que tiene un determinado valor

    def calcular_pedido(self, *args):
        # Si recibe 4 argumentos: Primer plato y bebida
        if len(args) == 4:
            primer_plato, costo_primer_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_bebida
            print(f"El costo de {primer_plato} y {bebida} es = ${total}")

        # Si recibe 6 argumentos: Primer plato, segundo plato y bebida
        elif len(args) == 6:
            primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            print(f"El costo de {primer_plato} + {segundo_plato} + {bebida} es = ${total}")

        # Si recibe 8 argumentos: Primer plato, segundo plato, postre y bebida
        elif len(args) == 8:
            primer_plato, costo_primer_plato, segundo_plato, costo_segundo_plato, postre, costo_postre, bebida, costo_bebida = args
            total = costo_primer_plato + costo_segundo_plato + costo_postre + costo_bebida
            print(f"El costo de {primer_plato} + {segundo_plato} + {bebida} + {postre} es = ${total}")

# Pruebas
if __name__ == "__main__":
    pedido1 = Pedido()
    pedido1.calcular_pedido("Sancocho", 5000.0, "Gaseosa", 2000.0)

    pedido2 = Pedido()
    pedido2.calcular_pedido("Crema de verduras", 5000.0, "Churrasco", 6000.0, "Gaseosa", 2000.0)

    pedido3 = Pedido()
    pedido3.calcular_pedido("Crema de espinacas", 5000.0, "Salmón", 10000.0, "Tiramisú", 5000.0, "Gaseosa", 2000.0)