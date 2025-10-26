import pytest
from src.medico import Medico

def test_criacao_medico():
    m = Medico("João", "Cardiologia")
    assert m.nome == "João"
    assert m.especialidade == "Cardiologia"
    assert m.agenda == []

def test_adicionar_horario():
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    assert "10:00" in m.agenda

def test_adicionar_horario_duplicado():
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    m.adicionar_horario("10:00")
    assert m.agenda.count("10:00") == 1 

def test_disponibilidade_horario():
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    assert m.disponivel("10:00") is True
    assert m.disponivel("11:00") is False

def test_remover_horario_existente():
    m = Medico("João", "Cardiologia")
    with pytest.raises(ValueError):
        m.remover_horario("10:00")

def test_remover_horario_inexistente():
    m = Medico("João", "Cardiologia")
    with pytest.raises(ValueError):
        m.remover_horario("10:00")
