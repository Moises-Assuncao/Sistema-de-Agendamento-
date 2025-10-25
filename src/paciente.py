class Paciente:
    """Representa um paciente cadastrado no sistema."""
    def __init__(self, nome: str, cpf: str, ativo: bool = True):
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo
