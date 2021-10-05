import sys
from typing import List


class Cliente:
    def __init__(self, nome: str, cpf: str, profissao: str):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente: Cliente, agencia: int, numero: int):
        self._saldo = 100
        self._agencia = 0
        self._numero = 0

        self.cliente = cliente
        self._set_agencia(agencia)
        self._set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self._agencia

    def _set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("Valor não é um numero inteiro", value)
        if value <= 0:
            raise ValueError("Valor igual o inferior a zero não podem ser atribuidos")
        self._agencia = value

    @property
    def numero(self):
        return self._numero

    def _set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("Valor não é um numero inteiro")
        if value <= 0:
            raise ValueError("Valor igual o inferior a zero não podem ser atribuidos")
        self._numero = value

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("Valor não é um numero inteiro")
        if value <= 0:
            raise ValueError("Valor igual o inferior a zero não podem ser atribuidos")
        self._saldo = value

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)
        self.saldo -= valor

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


if __name__ == "__main__":
    # cliente_teste = Cliente('Jhon', '123.456.789-00', 'Desenvolvedor')
    # print(cliente_teste.__dict__)
    # conta_corrente = ContaCorrente(cliente_teste, 14, 101)
    # print(conta_corrente.__dict__)

    contas: List[ContaCorrente] = []
    while True:
        try:
            nome = input("Nome do cliente:\n")
            agencia = input("Numero da agencia:\n")
            numero = input("Número da conta corrente:\n")
            conta_corrente = ContaCorrente(nome, agencia, numero)
            contas.append(conta_corrente)
        except ValueError as E:
            print(E.args)
            sys.exit()
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas')
            sys.exit()

