from ..main import ContaBancaria
import pytest

def test_criar_conta_zero_saldo():
    conta = ContaBancaria(12345, "Alisson Deivison", 0)
    assert conta.numero == 12345
    assert conta.nome == "Alisson Deivison"
    assert conta.saldo == 0.0

def test_criar_conta_com_saldo():
    conta = ContaBancaria(54321, "Anthony Gabriel", 1000.0)
    assert conta.numero == 54321
    assert conta.nome == "Anthony Gabriel"
    assert conta.saldo == 1000.0
    
def test_criar_conta_com_saldo_negativo():
    with pytest.raises(ValueError, match="Valor de saldo inicial deve ser maior ou igual a zero"):
        ContaBancaria(12345, "Alisson Deivison", -1000.0)
        
def test_criar_conta_com_saldo_em_string():
    with pytest.raises(ValueError, match="Valor de saldo inicial deve ser um número"):
        ContaBancaria(-12345, "Alisson Deivison", "1000")