from loja import ARMAZEM
from persistencia import salvar_personagens

def criar_personagem(personagens):
    nome = input("Por favor, escolha o nome do seu personagem: ").strip()

    if not nome:
        print("O nome não pode estar vazio!")
        return
    if nome in personagens:
        print("Já existe um personagem com esse nome!")
        return
    
    jogador = {
        "nome": nome,
        "dinheiro": 50,
        "xp": 0,
        "nivel": 1,
        "saldo": 0,
        "trabalho": None,
        "xp_trabalho": {},
        "ultimo_trabalho": None,
        "mineracoes_restantes": 3,
        "inicio_ciclo_mineracao": None,
        "extrato": [],
        "investimentos": {},
        "inventario": {},
        "ficha_criminal": 0
    }

    personagens[nome] = jogador
    
    salvar_personagens()
    
    return jogador

def excluir(personagens):
    if not personagens:
        print("Nenhum personagem criado!")
        return

    while True:
        print("\n=== PERSONAGENS ===")
        
        print("0 - Cancelar")
        for numero, nome in enumerate(personagens, start=1):
            print(f"{numero} - {nome}")

        try:
            escolha = int(
                input(
                    f"Por favor, escolha o personagem que deseja excluir "
                    f"(0-{len(personagens)}): "
                )
            )

        except ValueError:
            print("Opção inválida! Digite apenas números!")
            continue

        if escolha < 0 or escolha > len(personagens):
            print("Opção inválida, tente novamente.")
            continue
        
        if escolha == 0:
            print("Cancelando...")
            break

        nomes = list(personagens)

        nome_escolhido = nomes[escolha - 1]

        del personagens[nome_escolhido]

        salvar_personagens()

        print(f'Personagem "{nome_escolhido}" excluído com sucesso!')
        return

def inventario(personagem):
    if not personagem["inventario"]:
        print(f"{personagem['nome']} está com o inventário vazio!")
        return

    print(f"\nInventário de {personagem['nome']}:")

    for item, dados in personagem["inventario"].items():

        if dados.get("tipo") in ("picareta", "vara_pesca"):
            durabilidade_maxima = ARMAZEM[item]["durabilidade"]

            print(
                f"{item} | Durabilidade: "
                f"{dados['durabilidade']}/{durabilidade_maxima}"
            )

        else:
            print(
            f"{item} - Quantidade: "
            f"{dados['quantidade']}"
        )