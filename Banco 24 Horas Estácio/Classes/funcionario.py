from Classes.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, email, cpf, senha, idFuncionario):
        super().__init__(nome, email, cpf, senha)
        self.__idFuncionario = idFuncionario

    def cadastrar(self):
        nome = self.getNome()
        email = self.getEmail()
        cpf = self.getCpf()
        senha = self.getSenha()
        idFuncionario = self.__idFuncionario