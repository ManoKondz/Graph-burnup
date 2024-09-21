import matplotlib.pyplot as plt

def criar_grafico_burndown(dias, trabalho_total, trabalho_concluido):
    # Verificar se o comprimento das listas fornecidas é consistente
    if len(dias) != len(trabalho_concluido) or len(trabalho_total) != len(dias):
        print("Erro: As listas fornecidas devem ter o mesmo tamanho.")
        return

    # Linha planejada (trabalho total distribuído ao longo dos dias)
    trabalho_planejado = [trabalho_total[0] - (i * (trabalho_total[0] / (len(dias) - 1))) for i in range(len(dias))]

    # Trabalho restante real (trabalho total menos trabalho concluído cumulativo)
    trabalho_restante = [trabalho_total[0] - sum(trabalho_concluido[:i+1]) for i in range(len(trabalho_concluido))]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))

    # Linha planejada
    plt.plot(dias, trabalho_planejado, label="Planejado", color='teal', linestyle='-', marker='o')

    # Linha real (trabalho restante)
    plt.plot(dias, trabalho_restante, label="Real", color='orange', linestyle='-', marker='o')

    # Configurações do gráfico
    plt.title("Gráfico de Burndown")
    plt.xlabel("Tempo (dias)")
    plt.ylabel("Esforço (trabalho restante)")
    plt.legend()
    plt.grid(True)

    # Exibir o gráfico
    plt.show()

def obter_entrada_usuario():
    print("\nVamos criar seu gráfico Burndown!")
    try:
        # Entrada dos dias
        dias_input = input("Digite os dias do projeto (exemplo: 1,2,3,4,5): ")
        dias = list(map(int, dias_input.split(',')))

        # Entrada do trabalho total
        trabalho_total_input = input("Digite o total de trabalho inicial (exemplo: 100): ")
        trabalho_total = [int(trabalho_total_input)] * len(dias)

        # Entrada do trabalho concluído
        trabalho_concluido_input = input("Digite o trabalho concluído em cada dia (exemplo: 10,20,30,40,50): ")
        trabalho_concluido = list(map(int, trabalho_concluido_input.split(',')))

        # Validar e criar o gráfico
        criar_grafico_burndown(dias, trabalho_total, trabalho_concluido)

    except ValueError:
        print("\nErro: Por favor, insira apenas números inteiros separados por vírgulas.")
        print("Exemplo correto: 1,2,3,4,5")
        print("Por favor, tente novamente.\n")
        obter_entrada_usuario()

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Criar Gráfico Burndown")
        print("2. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            obter_entrada_usuario()
        elif opcao == '2':
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida, por favor escolha novamente.")

# Iniciar o programa
menu_principal()
