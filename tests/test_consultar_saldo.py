from ..main import ContaBancaria
import pytest

def test_consultar_saldo():
    conta = ContaBancaria(12345, "Alisson Deivison", 1000.0)
    assert conta.consultar_saldo() == 1000.0

