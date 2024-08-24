class Pessoa:
    def __init__(self, nome, email, cpf, senha):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__senha = senha

    def getNome(self):
        return self.__nome
    
    def getEmail(self):
        return self.__email
    
    def getCpf(self):
        return self.__cpf
    
    def getSenha(self):
        return self.__senha