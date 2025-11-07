from ..main import ContaBancaria
import pytest

def test_efetuar_saque():
    conta = ContaBancaria(12345, "Alisson Deivison", 1000.0)
    conta.sacar(500.0)
    assert conta.saldo == 500.0
    
