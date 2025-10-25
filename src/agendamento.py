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