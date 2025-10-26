import pytest
from src.agendamento import Agendamento
from src.medico import Medico
from src.paciente import Paciente

def test_criacao_agendamento():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    a = Agendamento(p, m, "10:00")

    assert a.paciente == p
    assert a.medico == m
    assert a.horario == "10:00"
    assert a.status == "CRIADO"

def test_confirmar_agendamento_sucesso():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    a = Agendamento(p, m, "10:00")
 
    a.confirmar()

    assert a.status == "CONFIRMADO"
    assert "10:00" not in m.agenda

def test_confirmar_falha_paciente_inativo():
    p = Paciente("Maria", "12345678901", ativo=False)
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    a = Agendamento(p, m, "10:00")
 
    with pytest.raises(ValueError):
        a.confirmar()

def test_confirmar_falha_medico_indisponivel():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    a = Agendamento(p, m, "10:00")

    with pytest.raises(ValueError):
        a.confirmar()

def test_realizar_sucesso():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    a = Agendamento(p, m, "10:00")
    a.confirmar()

    a.realizar()

    assert a.status == "REALIZADO"

def test_realizar_falha_nao_confirmado():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    a = Agendamento(p, m, "10:00")

    with pytest.raises(ValueError):
        a.realizar()

def test_cancelar_sucesso_antes_realizar():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    a = Agendamento(p, m, "10:00")
    a.confirmar()

    a.cancelar()

    assert a.status == "CANCELADO"
    # horário deve voltar pra agenda
    assert "10:00" in m.agenda

def test_cancelar_nao_libera_horario_se_realizado():
    p = Paciente("Maria", "12345678901")
    m = Medico("João", "Cardiologia")
    m.adicionar_horario("10:00")
    a = Agendamento(p, m, "10:00")
    a.confirmar()
    a.realizar()

    a.cancelar()

    assert a.status == "CANCELADO"
    # horário não deve voltar à agenda
    assert "10:00" not in m.agenda
