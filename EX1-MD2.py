contatos = {"sergio":190, "marta":186}
while True:
    mudar = input("escolha a opçao (A,B,C,D,F):Adicionar(A),Buscar(B),Remover(C),Listar(D),Sair(F)").upper()
    if mudar == "A":
        nome = input("digite o nome do contato:").lower()
        num = int(input("Digite o numero do contato:"))
        contatos [nome] = num
    elif mudar == "B":
        busca = input('Digite o nome que deseja buscar: ').lower()
        if busca in contatos:
           print(f'Telefone de {busca.title()}: {contatos[busca]}')
        else:
            print('Contato não encontrado.')
    elif mudar == "C":
        remover = input("quem quer remover?")
        if remover in contatos:
            del contatos[remover]
            print(contatos)
        else:
            print('Contato não encontrado.')
    elif mudar == "D":
        if contatos:
            for nome, num in contatos.items():
                print(f"{nome.title()}: {num}")
    
    elif mudar == "F":
        break