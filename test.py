from main import Funcionario

def test_funcionario():
    funcionario = Funcionario("Victor", 5000.0, 800.0, 1200.0)
    salario_liquido = funcionario.calcular_salario_liquido()
    assert salario_liquido == 4600.0, f"Salário líquido incorreto: {salario_liquido}"
    print("Teste 1 passou!")

def test_acrescimos_descontos():
    funcionario = Funcionario("Carlos", 7000.0, 500.0, 1000.0)
    funcionario.set_total_acrescimos(800.0)
    funcionario.set_total_descontos(1500.0)
    salario_liquido = funcionario.calcular_salario_liquido()
    assert salario_liquido == 6300.0, f"Salário líquido incorreto: {salario_liquido}"
    print("Teste 2 passou!")

if __name__ == "__main__":
    test_funcionario()
    test_acrescimos_descontos()
    print("Todos os testes passaram!")