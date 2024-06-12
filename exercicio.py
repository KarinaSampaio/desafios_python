# Parte 1 imprime nome e idade
def imprimir_nome_idade(nome,idade):
    print(f"nome: {nome}, idade: {idade}")

# Parte 2: Variáveis para armazenar informações
nome = "Karina"
idade = 33
altura = 1.64
gosta_de_programacao = True

# Parte 3: Função para realizar operações matemáticas
def operacoes_basicas(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
    return soma, subtracao, multiplicacao, divisao

# Parte 4: Função que retorna o maior de dois números
def maior_numero(num1, num2):
    return num1 if num1 > num2 else num2


# Código principal
if __name__ == "__main__":
    # Imprimir nome e idade
    imprimir_nome_idade(nome, idade)

    # Solicitar dois números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realizar operações básicas
    soma, subtracao, multiplicacao, divisao = operacoes_basicas(num1, num2)
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

    # Encontrar e imprimir o maior número
    maior = maior_numero(num1, num2)
    print(f"O maior número entre {num1} e {num2} é: {maior}")

    # Informações adicionais
    print(f"Altura: {altura}")
    print("Gosta de programação: {}".format("Sim" if gosta_de_programacao else "Não"))