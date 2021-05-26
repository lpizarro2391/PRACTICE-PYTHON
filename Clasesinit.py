class Figurasgeometricas:
    def __init__(self) -> None:
        print("rectangulo")
        self.base=int(input("dame el valor de la base :"))
        self.altura=int(input("dame el valor de la altura :"))
        self.costo=2500

rectangulo=Figurasgeometricas()
print("el area del terreno es: ", rectangulo.base*rectangulo.altura)
print("el costo  del lote es: ", rectangulo.base*rectangulo.altura*rectangulo.costo)
