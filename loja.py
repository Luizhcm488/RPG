from persistencia import salvar_personagens
from itens import ARMAZEM

def loja(personagem):
    while True:
        print("\n======== LOJA ========")
        print(f"Dinheiro: R${personagem['dinheiro']:.2f}")

        itens = list(ARMAZEM)

        for numero, item in enumerate(itens, start=1):
            preco = ARMAZEM[item]["preco"]
            print(f"{numero} - {item} | R${preco:.2f}")

        print(f"{len(itens) + 1} - Sair")

        try:
            escolha = int(
                input(
                    f"Escolha um item "
                    f"(1-{len(itens) + 1}): "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(itens) + 1:
            print("Opção inválida!")
            continue

        if escolha == len(itens) + 1:
            break

        item_escolhido = itens[escolha - 1]
        preco = ARMAZEM[item_escolhido]["preco"]

        if item_escolhido in personagem["inventario"]:
            print(f"Você já possui {item_escolhido}!")
            continue

        if personagem["dinheiro"] >= preco:
            personagem["dinheiro"] -= preco

            personagem["inventario"][item_escolhido] = (
        ARMAZEM[item_escolhido].copy()
    )

            personagem["inventario"][item_escolhido].pop("preco")
            
            salvar_personagens()
            
            print(f"Você comprou {item_escolhido}!")

        else:
            print("Dinheiro insuficiente!")
