from medico import Medico

class Agendamento:
    """Controla o ciclo de vida de uma consulta médica."""
    def __init__(self, paciente, medico, horario: str):
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
        self.status = "CRIADO"

    def confirmar(self):
        """Confirma o agendamento se o médico estiver disponível e o paciente ativo"""
        if not self.paciente.ativo:
            raise ValueError("Paciente Inativo não pode realizar agendamentos.")
        if not self.medico.disponivel(self.horario):
            raise ValueError("Médico não está disponível neste horário.")
        
        self.medico.agenda.remove(self.horario)
        self.status = "CONFIRMADO"

    def realizar(self):
        """Realiza a consulta se o agendamento estiver confirmado"""
        if self.status != "CONFIRMADO":
            raise ValueError("A consulta só pode ser realizada se estiver  CONFIRMADA")
        self.status = "REALIZADO"

    def cancelar(self):
        """Cancela a consulta. Se não foi realizada, o horário pode ser liberado"""
        if self.status != "REALIZADO" and self.horario not in self.medico.agenda:
            #libera o horário
            self.medico.agenda.append(self.horario)
        self.status = "CANCELADO"