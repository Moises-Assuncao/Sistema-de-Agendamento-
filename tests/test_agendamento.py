import pytest
from src.agendamento import Agendamento
from src.medico import Medico
from src.paciente import Paciente

def test_criacao_agendamento():
    p = Paciente("Maria", "123")
    m = Medico("João", "Cardiologia")
    a = Agendamento(p, m, "10:00")

    assert a.paciente == p
    assert a.medico == m
    assert a.horario == "10:00"
    assert a.status == "CRIADO"