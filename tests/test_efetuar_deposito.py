from ..main import ContaBancaria
import pytest

def test_efetuar_deposito():
    conta = ContaBancaria(12345, "Alisson Deivison", 0)
    conta.depositar(1000.0)
    assert conta.saldo == 1000.0
