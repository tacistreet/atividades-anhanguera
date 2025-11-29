fila_urgente = []
fila_normal = []
medicos_disponiveis = 0

def definir_medicos():
    global medicos_disponiveis
    medicos_disponiveis = int(input("Digite o número de médicos disponíveis: "))
    print("Médicos disponíveis definidos:", medicos_disponiveis)

def registrar_chegada():
    nome = input("Nome do paciente: ")
    agendamento = input("Tem agendamento? (s/n): ")
    adimplente = input("Está adimplente? (s/n): ")
    documentos = input("Documentação em dia? (s/n): ")

    if agendamento == "s" and adimplente == "s" and documentos == "s" and medicos_disponiveis > 0:
        urgente = input("Consulta é urgente? (s/n): ")
        if urgente == "s":
            fila_urgente.append(nome)
            print("Paciente colocado na fila URGENTE.")
        else:
            fila_normal.append(nome)
            print("Paciente colocado na fila NORMAL.")
    else:
        print("Paciente não pode ser atendido no momento.")

def atender_proximo():
    global medicos_disponiveis
    if medicos_disponiveis <= 0:
        print("Não há médicos disponíveis.")
        return
    if len(fila_urgente) > 0:
        paciente = fila_urgente.pop(0)
        print("Atendendo paciente URGENTE:", paciente)
    elif len(fila_normal) > 0:
        paciente = fila_normal.pop(0)
        print("Atendendo paciente NORMAL:", paciente)
    else:
        print("Nenhum paciente na fila.")
        return
    medicos_disponiveis -= 1

def finalizar_atendimento():
    global medicos_disponiveis
    medicos_disponiveis += 1
    print("Atendimento finalizado. Médicos disponíveis:", medicos_disponiveis)

def mostrar_filas():
    print("Fila URGENTE:", fila_urgente)
    print("Fila NORMAL:", fila_normal)

# Menu principal
while True:
    print("\n--- Menu Controle ---")
    print("1 - Definir médicos disponíveis")
    print("2 - Registrar chegada de paciente")
    print("3 - Atender próximo paciente")
    print("4 - Finalizar atendimento")
    print("5 - Mostrar filas")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        definir_medicos()
    elif opcao == "2":
        registrar_chegada()
    elif opcao == "3":
        atender_proximo()
    elif opcao == "4":
        finalizar_atendimento()
    elif opcao == "5":
        mostrar_filas()
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
