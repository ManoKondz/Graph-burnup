import matplotlib.pyplot as plt

def criar_grafico_burn(dias, trabalho_total, trabalho_concluido):
    # Verificar se o comprimento das listas fornecidas é consistente
    if len(dias) != len(trabalho_concluido) or len(trabalho_total) != len(dias):
        print("Erro: As listas fornecidas devem ter o mesmo tamanho.")
        return

    # Burn-down chart (trabalho restante)
    trabalho_restante = [trabalho_total[0] - concluido for concluido in trabalho_concluido]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))

    # Gráfico Burn-up (trabalho concluído)
    plt.plot(dias, trabalho_concluido, label="Trabalho Concluído", color='green', marker='o')

    # Gráfico Burn-down (trabalho restante)
    plt.plot(dias, trabalho_restante, label="Trabalho Restante", color='red', marker='o')

    # Gráfico de referência (trabalho total)
    plt.plot(dias, trabalho_total, label="Trabalho Total", color='blue', linestyle='--')

    # Configurações do gráfico
    plt.title("Gráfico de Burn-up e Burn-down")
    plt.xlabel("Dias")
    plt.ylabel("Pontos de Trabalho")
    plt.legend()
    plt.grid(True)

    # Exibir o gráfico
    plt.show()

def obter_entrada_usuario():
    print("Bem-vindo à ferramenta de geração de gráficos Burn-up e Burn-down!")
    print("Por favor, siga as instruções para fornecer seus dados.\n")

    try:
        # Entrada dos dias
        dias_input = input("Digite os dias do projeto (exemplo: 1,2,3,4,5): ")
        dias = list(map(int, dias_input.split(',')))

        # Entrada do trabalho total
        trabalho_total_input = input("Digite o trabalho total esperado por dia (exemplo: 100,100,100,100,100): ")
        trabalho_total = list(map(int, trabalho_total_input.split(',')))

        # Entrada do trabalho concluído
        trabalho_concluido_input = input("Digite o trabalho concluído em cada dia (exemplo: 10,20,30,40,50): ")
        trabalho_concluido = list(map(int, trabalho_concluido_input.split(',')))

        # Validar e criar o gráfico
        criar_grafico_burn(dias, trabalho_total, trabalho_concluido)

    except ValueError:
        print("\nErro: Por favor, insira apenas números inteiros separados por vírgulas.")
        print("Exemplo correto: 1,2,3,4,5")
        print("Por favor, tente novamente.\n")
        obter_entrada_usuario()

# Iniciar a interação com o usuário
obter_entrada_usuario()

