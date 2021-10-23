import sys
from typing import List
from leitor import LeitorArquivo

from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError


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
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
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
        self._saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor não pode ser inferior a zero")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidas += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser inferior a zero")
        elif self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', self.saldo, valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


# if __name__ == "__main__":
#     # cliente_teste = Cliente('Jhon', '123.456.789-00', 'Desenvolvedor')
#     # print(cliente_teste.__dict__)
#     # conta_corrente = ContaCorrente(cliente_teste, 14, 101)
#     # print(conta_corrente.__dict__)
#
#     contas_teste: List[ContaCorrente] = []
#     while True:
#         try:
#             nome_teste = input("Nome do cliente:\n")
#             agencia_teste = input("Numero da agencia:\n")
#             numero_teste = input("Número da conta corrente:\n")
#             conta_corrente_teste = ContaCorrente(nome_teste, agencia_teste, numero_teste)
#             contas_teste.append(conta_corrente_teste)
#         except ValueError as E:
#             print(E.args)
#             sys.exit()
#         except KeyboardInterrupt:
#             print(f'\n\n{len(contas_teste)}(s) contas criadas')
#             sys.exit()

# conta_corrente1 = ContaCorrente(None, 24, 563)
# conta_corrente1.depositar(50)
# conta_corrente1.sacar(15)
#
# conta_corrente2 = ContaCorrente(None, 45, 278)
# conta_corrente2.depositar(50)
# conta_corrente2.sacar(5)
#
# print('Saldo:', conta_corrente1.saldo)
# print('Saldo:', conta_corrente2.saldo)
# try:
#     conta_corrente1.transferir(1000, conta_corrente2)
# except OperacaoFinanceiraError as E:
#     import traceback
#     print(E.saldo)
#     print(E.valor)
#     print("Exceção do tipo:", E.__class__.__name__)
#     traceback.print_exc()
# print('Saldo:', conta_corrente1.saldo)
# print('Saldo:', conta_corrente2.saldo)

with LeitorArquivo("arquivp.txt") as leitor_teste:
    leitor_teste.ler_proxima_linha()
