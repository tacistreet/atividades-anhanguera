pacientes = []

def cadastrar_paciente():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")
    paciente = {"nome": nome, "idade": idade, "telefone": telefone}
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def mostrar_total():
    print("Total de pacientes cadastrados:", len(pacientes))

def mostrar_extremos():
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    print("Paciente mais novo:", mais_novo["nome"], "-", mais_novo["idade"], "anos")
    print("Paciente mais velho:", mais_velho["nome"], "-", mais_velho["idade"], "anos")

def buscar_paciente():
    nome = input("Digite o nome para buscar: ")
    encontrado = False
    for p in pacientes:
        if p["nome"].lower() == nome.lower():
            print("Paciente encontrado:", p["nome"], "-", p["idade"], "anos - Tel:", p["telefone"])
            encontrado = True
    if not encontrado:
        print("Paciente não encontrado.")

def listar_pacientes():
    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
    else:
        print("Lista de pacientes:")
        for p in pacientes:
            print(p["nome"], "-", p["idade"], "anos - Tel:", p["telefone"])

# Menu principal
while True:
    print("\n--- Menu ---")
    print("1 - Cadastrar paciente")
    print("2 - Mostrar total de pacientes")
    print("3 - Mostrar paciente mais novo e mais velho")
    print("4 - Buscar paciente por nome")
    print("5 - Listar todos os pacientes")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        mostrar_total()
    elif opcao == "3":
        mostrar_extremos()
    elif opcao == "4":
        buscar_paciente()
    elif opcao == "5":
        listar_pacientes()
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
