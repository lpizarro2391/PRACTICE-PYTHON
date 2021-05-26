class Figurasgeometricas:
    def __init__(self) -> None:
        self.base=int(input("dame el valor de la base :"))
        self.altura=int(input("dame el valor de la altura :"))
        self.costoterrenocuadrado=2500
        self.costoterrenotriangular=1000
print("rectangulo")
rectangulo=Figurasgeometricas()
print("triangulo")
triangulo=Figurasgeometricas()

print("el area del terreno rectangular es: ", rectangulo.base*rectangulo.altura)
print("el costo  del lote es: ", rectangulo.base*rectangulo.altura*rectangulo.costoterrenocuadrado)
print("el area del terreno triangular es: ", triangulo.base*triangulo.altura/2)
print("el costo del terreno triangular es: ", (triangulo.base*triangulo.altura/2)*triangulo.costoterrenotriangular)
