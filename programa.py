import random

def adivinhe_o_numero():
    print("Bem-vindo ao jogo de Adivinhe o Número!")
    print("Vou pensar em um número entre 1 e 100. Tente adivinhar qual é!")

    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, envie um número entre 1 e 100.")
                continue

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("O número é maior que isso. Tente novamente.")
            else:
                print("O número é menor que isso. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    adivinhe_o_numero()