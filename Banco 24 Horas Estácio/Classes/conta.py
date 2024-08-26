class Conta:
    def __init__ (self, numConta, titular, saldo):
        self.numConta = numConta
        self.titular = titular
        self.saldo = saldo

    def cadastrar (self) -> bool:
        try:
            self.numConta = self.numConta
            self.titular = self.titular
            self.saldo = self.saldo
            return True
        except:
            return False
        
    def depositar (self, valor) -> bool:
        try:
            self.saldo += valor
            return True
        except:
            return False
        
    def sacar (self, valor) -> bool:
        try:
            self.saldo -= valor
            return True
        except:
            return False
        
    def listarDados (self) -> str:
        dados = {
            "Número da Conta: ":self.numConta,
            "Titular: ":self.titular,
            "Saldo R$ ":self.saldo
        }
        return dados