from Classes.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, email, cpf, senha):
        super().__init__(nome, email, cpf, senha)

    def cadastrar(self):
        nome = self.getNome()
        email = self.getEmail()
        cpf = self.getCpf()
        senha = self.getSenha()