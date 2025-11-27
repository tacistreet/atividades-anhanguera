from functools import total_ordering


def mostrar_menu():
    print("\n Menu ")
    print("1 - Cadastrar novo paciente")
    print("2 - Exibir todos os pacientes")
    print("3 - Buscar pacientes por nome")
    print("4 - Estatísticas dos pacientes")
    print("5 - Sair do programa")

def cadastrar_paciente():
    try:
        nome = input("Digite o nome do paciente: ") .strip()
        idade = input("Digite a idade do paciente: ") .strip()
        telefone = input("Digite o telefone do paciente: ") .strip()
        pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
        print(f"{nome} cadastrado com sucesso!")
    except ValueError:
        print("Erro: idade deve ser um número inteiro.")

def exibir_pacientes():
    if not pacientes:
        print("Nenhum paciente foi encontrado.")
    else:
        print("\n Lista de pacientes:")
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. {p['nome']} | {p['idade']} | {p['telefone']} ")
def buscar_paciente(pacientes=None, nome_busca=None):
    nome = input("Digite o nome do paciente: ") .strip().lower()
    encontrados = [p for p in pacientes if p["nome"] == nome.lower() == nome_busca]
    if encontrados:
        for p in encontrados:
            print(f"Encontrado: {p['nome']} | {p['idade']} | {p['telefone']}")
    else:
        print("Nenhum paciente foi encontrado.")


def total(pacientes):
    pass


def estatisticas(pacientes):
    if not pacientes:
        print("Nenhum paciente foi encontrado.")
        return
    total(pacientes)
    idades = [p["idade"] for p in pacientes]
    media = sum(idades) / total_ordering(idades)
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    print("\n Estatísticas dos pacientes:")
    print(f"Total de pacientes: {total}")
    print("Média de Idade dos pacientes: {media:.2f}")
    print(f"Paciente mais novo: {mais_novo ['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho [ 'nome']} ({mais_velho['idade']} anos))")

def main():
    pacientes = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            exibir_pacientes(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            estatisticas(pacientes)
        elif opcao == "5":
            print("Programa finalizado com sucesso!")
            break
        else:
            print("Opção inválida! Tente novamente!")

if __name__ == "__main__":
    main()