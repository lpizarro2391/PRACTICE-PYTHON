class Calculadora:
    def __init__(self,n1,n2) -> None:
        n1=int(input("dame el primer numero"))
        n2=int(input("dame el primer numero"))
        self.suma= n1+n2
        self.resta= n1-n2
        self.multiplicacion= n1*n2
        self.division= n1/n2

operacion = Calculadora(2,4)
print(operacion.multiplicacion)





        