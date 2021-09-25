def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve receber apenas argumentos inteiros")
    try:
        aux = dividendo/divisor
        return aux
    except ZeroDivisionError:
        print(f"Não se pode dividir {dividendo} por {divisor}")
        raise


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisão de 10 por {divisor} é {resultado}")


try:
    testa_divisao('e5r')
except ZeroDivisionError:
    print("Erro de divisão por zero")
# except Exception as erro_desconhecido:
#     print("Erro desconhecido")

print("Programa encerrado")
