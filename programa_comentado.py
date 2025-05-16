
import random  # Importa a biblioteca 'random' que permite gerar números aleatórios

def adivinhe_o_numero():  # Define uma função chamada 'adivinhe_o_numero' que contém toda a lógica do jogo
    print("Bem-vindo ao jogo de Adivinhe o Número!")  # Exibe uma mensagem de boas-vindas ao usuário
    print("Vou pensar em um número entre 1 e 100. Tente adivinhar qual é!")  # Explica as regras do jogo ao usuário

    # Gera um número aleatório entre 1 e 100 e armazena na variável 'numero_secreto'
    numero_secreto = random.randint(1, 100)
    tentativas = 0  # Inicializa a contagem de tentativas do usuário como zero

    while True:  # Inicia um laço de repetição que continuará até o usuário acertar o número
        try:  # Tenta executar o bloco de código abaixo, para capturar possíveis erros de entrada
            palpite = int(input("Digite seu palpite: "))  # Solicita ao usuário que insira um número e converte para inteiro
            tentativas += 1  # Incrementa a contagem de tentativas a cada tentativa do usuário

            # Verifica se o palpite está fora do intervalo permitido (1 a 100)
            if palpite < 1 or palpite > 100:
                print("Por favor, envie um número entre 1 e 100.")  # Pede para inserir um número válido
                continue  # Reinicia o loop sem contar essa tentativa inválida

            # Verifica se o palpite do usuário é igual ao número secreto
            if palpite == numero_secreto:
                # Caso seja igual, o usuário acertou o número
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")  # Mensagem de sucesso
                break  # Encerra o laço de repetição, finalizando o jogo
            # Caso o palpite seja menor que o número secreto
            elif palpite < numero_secreto:
                print("O número é maior que isso. Tente novamente.")  # Dica para o usuário tentar um número maior
            # Caso o palpite seja maior que o número secreto
            else:
                print("O número é menor que isso. Tente novamente.")  # Dica para o usuário tentar um número menor
        except ValueError:  # Caso o usuário insira algo que não seja um número válido
            print("Por favor, insira um número válido.")  # Pede para inserir um número válido

# Verifica se o arquivo está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    adivinhe_o_numero()  # Chama a função para iniciar o jogo