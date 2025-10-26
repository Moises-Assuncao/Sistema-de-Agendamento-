class Medico:
    """Representa um médico e sua agenda de horários."""
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
        self.agenda = []

    def adicionar_horario(self, horario: str):
        """Adiciona um horário à agenda."""
        if horario not in self.agenda:
            self.agenda.append(horario)

    def disponivel(self, horario: str) -> bool:
        """Retorna True se o horário estiver disponível."""
        return horario in self.agenda

    def remover_horario(self, horario: str):
        """Remove um horário da agenda, se existir."""
        if horario not in self.agenda:
            raise ValueError("Horário não encontrado na agenda.")
        self.agenda.remove(horario)
