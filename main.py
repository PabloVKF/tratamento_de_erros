class Cliente:
    def __init__(self, nome: str, cpf: str, profissao: str):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente: Cliente, agencia: str, numero: str):
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)
        self.saldo -= valor

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


if __name__ == "__main__":
    cliente_teste = Cliente('Jhon', '123.456.789-00', 'Desenvolvedor')
    print(cliente_teste.__dict__)
    conta_corrente = ContaCorrente(cliente_teste, '00', '101')
    print(conta_corrente.__dict__)
