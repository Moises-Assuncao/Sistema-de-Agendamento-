import pytest
from src.paciente import Paciente

def test_criacao_paciente_valido():
    p = Paciente("Maria", "12345678901")
    assert p.nome == "Maria"
    assert p.cpf == "12345678901"
    assert p.ativo is True

def test_cpf_invalido_menos_digitos():
    with pytest.raises(ValueError):
        Paciente("José", "123")

def test_paciente_inativo_nao_pode_agendar():
    p = Paciente("Carlos", "12345678901", ativo=False)
    assert p.ativo is False
