from abc import ABC, abstractmethod
from unittest import TestCase, main

class Calculadora:
    def calcular(self, valor1, valor2, operador):
        opera = OperacaoFabrica()
        operacao = opera.criar(operador)
        if(operador == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado


class OperacaoFabrica:
    def criar(self, operador):
        if(operador == "soma"):
            return Soma()
    
        elif(operador == "subtracao"):
            return Subtracao()

        elif(operador == "divisao"):
            return Divisao()

        elif(operador == "multiplicacao"):
            return Multiplicacao()
    


class Operacao(ABC):
    
    abstractmethod
    def executar(self, valor1, valor2):
        pass


class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Testes(TestCase):

    def testarSoma(self):
        resultado = Calculadora()
        self.assertEqual(resultado.calcular(58,2,"soma"),60)

    def testarSubtracao(self):
        resultado = Calculadora()
        self.assertEqual(resultado.calcular(15,10,"subtracao"),5)

    def testarMultiplicacao(self):
        resultado = Calculadora()
        self.assertEqual(resultado.calcular(21,21,"multiplicacao"),441)

    def testarDivisao(self):
        resultado = Calculadora()
        self.assertEqual(resultado.calcular(45,5,"divisao"),9)

    def testarNulo(self):
        resultado = Calculadora()
        self.assertEqual(resultado.calcular(14,5,None),0)
    

if __name__ == "__main__":
    main()