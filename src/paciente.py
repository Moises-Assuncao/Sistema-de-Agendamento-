class Paciente:
    """Representa um paciente cadastrado no sistema."""
    def __init__(self, nome: str, cpf: str, ativo: bool = True):
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos numéricos.")
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo
