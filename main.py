class Funcionario:
    
    def __init__(self, nome, salario_bruto, total_acrescimos, total_descontos):
        self.__nome = nome
        self.__salario_bruto = salario_bruto
        self.__total_acrescimos = total_acrescimos
        self.__total_descontos = total_descontos

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_salario_bruto(self, salario_bruto):
        self.__salario_bruto = salario_bruto

    def get_salario_bruto(self):
        return self.__salario_bruto

    def set_total_acrescimos(self, total_acrescimos):
        self.__total_acrescimos = total_acrescimos

    def get_total_acrescimos(self):
        return self.__total_acrescimos

    def set_total_descontos(self, total_descontos):
        self.__total_descontos = total_descontos

    def get_total_descontos(self):
        return self.__total_descontos

    def calcular_salario_liquido(self):
        return self.__salario_bruto + self.__total_acrescimos - self.__total_descontos

    def __str__(self):
        return (f"Nome: {self.__nome}, Salário Bruto: R${self.__salario_bruto:.2f}, "
                f"Total de Acréscimos: R${self.__total_acrescimos:.2f}, "
                f"Total de Descontos: R${self.__total_descontos:.2f}, "
                f"Salário Líquido: R${self.calcular_salario_liquido():.2f}")
