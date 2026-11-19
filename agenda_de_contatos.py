def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone do contato: ").strip()
    email = input("Digite o e-mail do contato: ").strip()

    if not nome:
        print("O nome do contato não pode ficar vazio.")
        return

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False,
    }

    contatos.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")


def listar_contatos(contatos, apenas_favoritos=False):
    contatos_encontrados = False

    print("\nLista de contatos:")

    for indice, contato in enumerate(contatos, start=1):
        if apenas_favoritos and not contato["favorito"]:
            continue

        contatos_encontrados = True
        favorito = "★" if contato["favorito"] else " "
        print(
            f"{indice}. [{favorito}] {contato['nome']} | "
            f"Telefone: {contato['telefone']} | E-mail: {contato['email']}"
        )

    if not contatos_encontrados:
        if apenas_favoritos:
            print("Nenhum contato favorito encontrado.")
        else:
            print("Nenhum contato cadastrado.")


def obter_indice_contato(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return None

    try:
        numero_contato = int(input("Digite o número do contato: "))
        indice = numero_contato - 1

        if indice < 0 or indice >= len(contatos):
            print("Número de contato inválido.")
            return None

        return indice
    except ValueError:
        print("Digite apenas o número do contato.")
        return None


def editar_contato(contatos):
    listar_contatos(contatos)
    indice = obter_indice_contato(contatos)

    if indice is None:
        return

    contato = contatos[indice]

    novo_nome = input("Digite o novo nome: ").strip()
    novo_telefone = input("Digite o novo telefone: ").strip()
    novo_email = input("Digite o novo e-mail: ").strip()

    if not novo_nome:
        print("O nome do contato não pode ficar vazio.")
        return

    contato["nome"] = novo_nome
    contato["telefone"] = novo_telefone
    contato["email"] = novo_email

    print("Contato atualizado com sucesso!")


def alternar_favorito(contatos):
    listar_contatos(contatos)
    indice = obter_indice_contato(contatos)

    if indice is None:
        return

    contato = contatos[indice]
    contato["favorito"] = not contato["favorito"]

    if contato["favorito"]:
        print(f"Contato '{contato['nome']}' marcado como favorito!")
    else:
        print(f"Contato '{contato['nome']}' removido dos favoritos!")


def apagar_contato(contatos):
    listar_contatos(contatos)
    indice = obter_indice_contato(contatos)

    if indice is None:
        return

    contato_removido = contatos.pop(indice)
    print(f"Contato '{contato_removido['nome']}' apagado com sucesso!")


contatos = []

while True:
    print("\nAgenda de contatos:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Listar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        adicionar_contato(contatos)
    elif escolha == "2":
        listar_contatos(contatos)
    elif escolha == "3":
        editar_contato(contatos)
    elif escolha == "4":
        alternar_favorito(contatos)
    elif escolha == "5":
        listar_contatos(contatos, apenas_favoritos=True)
    elif escolha == "6":
        apagar_contato(contatos)
    elif escolha == "7":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
