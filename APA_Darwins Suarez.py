'''Problema:
Queremos comer uma pizza mas ao mesmo tempo
não queremos sair de casa nem gastar dinheiro com entrega,
como podemos fazer?

Solução: Fazer uma pizza caseira'''


import time

def preparar_pizza_caseira():
    print("Problema: ")
    time.sleep(1)
    
    print("\nQueremos comer uma pizza.")
    time.sleep(1)
    
    print("mas ao mesmo tempo não queremos sair de casa,")
    print("nem gastar dinheiro com deliveri.")
    time.sleep(1)
    
    print("\ncomo podemos fazer?")
    time.sleep(2)
    
    print("Solução: Fazer uma pizza caseira")
    time.sleep(2)
    
   
    print("\nVou mostrar como preparar uma pizza caseira!")
    time.sleep(1)
    
    #Escolher a massa
    print("\nQue tipo de massa você tem ou quer?:")
    print("1. Prefiro massa comercial pré-cozida")
    print("2. Quero fazer Massa caseira")
    escolha_massa = input("Informe o número da sua escolha: ")
    time.sleep(1)
   
    
    #Preparar a massa
    if escolha_massa == "2":
        print("Amassando a massa...")
        time.sleep(2)  # Simulando o tempo de preparo
        print("A massa está pronta!")
        time.sleep(1)

    #Preparar o molho
    print("\nQue tipo de molho você quer:")
    print("1. Tenho Molho comprado")
    print("2. Gosto de Molho caseiro")
    escolha_molho = input("Informe o número da sua escolha: ")

    if escolha_molho == "2":
        print("Preparando o molho...")
        time.sleep(2)  # Simulando o tempo de preparo
        print("O molho está pronto!")
        time.sleep(1)


    #Escolher os ingredientes
    ingredientes = input("\nDigite os ingredientes separados por vírgula (ex: pepperoni, presunto, champignon): ").split(',')
    time.sleep(1)
    #queijo = "mozzarella"

    #Pré-aquecer o forno a 250°C
    while True:
        escolha_pre_aquecer = input("\nQuer pré-aquecer o forno a 250°C? (S/N): ").upper()
        
        if escolha_pre_aquecer == "S":
            print("Pré-aquecendo o forno a 250°C...")
            time.sleep(2)
            # Simulando o tempo de pré-aquecimento
            break
        elif escolha_pre_aquecer == "N":
            print("O forno não será pré-aquecido. Certifique-se de ajustar a temperatura conforme necessário.")
            break
        else:
            print("Escolha inválida. Responda com 'S' para Sim ou 'N' para Não.")
        time.sleep(1)    

    
    # Pré-assar a massa
    if escolha_massa == "2":
        print("Pre-assando a massa...")
        time.sleep(2)  # Simulando o tempo de pré-assar
        print("A massa está finalmente pré-assada!!")
        time.sleep(1)


    # Montar a pizza
    print("\nPara montar a pizza, espalhe a massa, acrescentar o molho e os ingredientes adicionais.")
    time.sleep(2)  # Simulando o tempo de montagem
    print(f"A pizza com {', '.join(ingredientes)} está pronta para assar!")
    time.sleep(1)

    # Assando a pizza
    tempo_assamento = 8 + len(ingredientes)
    # Tempo dinâmico baseado na quantidade de ingredientes
    print(f"Assando a pizza por {tempo_assamento} minutos...")
    time.sleep(1)
    print("Por favor espere...")
    time.sleep(1)
    print("\nVerificar o cozimento, cuidando do tempo e olhando pelo vidro do forno.")
    time.sleep(tempo_assamento)
    # Simulando o tempo de assamento, apenas esperar.
    print("\nA pizza está pronta para ser saboreada!")
    time.sleep(1)

    # Servir e aproveitar
    print("Retirar a pizza do forno e coloque-la no prato.")
    time.sleep(1)
    print("\nSirva uma bebida de sua preferência para acompanhar.")
    time.sleep(1)
    print("A pizza está pronta, finalmente, Bom apetite!")
    time.sleep(3)
    print("\nPor último, não esqueça de tirar a mesa e limpar tudo!")
    time.sleep(3)
    print("\nObrigado por executar o Algoritmo para preparar uma pizza caseira")

    
    print("░█████╗░██████╗░██████╗░██╗░██████╗░░█████╗░██████╗░░█████╗░")
    print("██╔══██╗██╔══██╗██╔══██╗██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗")
    print("██║░░██║██████╦╝██████╔╝██║██║░░██╗░███████║██║░░██║██║░░██║")
    print("██║░░██║██╔══██╗██╔══██╗██║██║░░╚██╗██╔══██║██║░░██║██║░░██║")
    print("╚█████╔╝██████╦╝██║░░██║██║╚██████╔╝██║░░██║██████╔╝╚█████╔╝")
    print("░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░")
    
#Executar o algoritmo
preparar_pizza_caseira()

    #Direitos autorais (c) Suarez Darwins 2024



