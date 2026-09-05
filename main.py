from personagens import criar_personagem, inventario, excluir
from persistencia import personagens
from trabalhos import trabalhar, escolher_trabalho
from loja import loja
from cassino import cassino
from mineracao import mineracao
from crime import crime, limpar_ficha
from banco import banco

OPCOES_MENU_PRINCIPAL = ["Iniciar", "Criar Personagem", "Tutorial", "Excluir Personagem", "Sair"]

OPCOES_MENU_JOGO = [
    "Trabalhar",
    "Trabalhos",
    "Mineração",
    "Loja",
    "Cassino",
    "Inventário",
    "Crime",
    "Fiança/Limpar Ficha",
    "Banco",
    "Pescar",
    "Sair"
]

def iniciar():
    if not personagens:
        print("Nenhum personagem criado!")
        return

    while True:
        print("\n=== PERSONAGENS ===")
        
        print("0 - Cancelar")
        for numero, personagem in enumerate(personagens, start=1):
            print(f"{numero} - {personagem}")

        try:
            escolha = int(
                input(
                    f"Por favor, escolha um personagem "
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
            return

        nomes = list(personagens)

        nome_escolhido = nomes[escolha - 1]

        personagem_escolhido = personagens[nome_escolhido]

        print(f"\nVocê escolheu {nome_escolhido}!")

        menu_jogo(personagem_escolhido)

        return


def menu_jogo(personagem):
    while True:
        print(f"\n======== {personagem['nome']} ========")

        for numero, opcao in enumerate(OPCOES_MENU_JOGO, start=1):
            print(f"{numero} - {opcao}")

        try:
            escolha = int(
                input(
                    f"Escolha uma opção "
                    f"(1-{len(OPCOES_MENU_JOGO)}): "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(OPCOES_MENU_JOGO):
            print("Opção inválida!")
            continue
        
        if escolha == 1:
            trabalhar(personagem)
            
        elif escolha == 2:
            escolher_trabalho(personagem)
        	
        elif escolha == 3:
            mineracao(personagem)
        	
        elif escolha == 4:
            loja(personagem)
        	
        elif escolha == 5:
            cassino(personagem)
        
        elif escolha == 6:
            inventario(personagem)
        	
        elif escolha == 7:
            crime(personagem)
        	
        elif escolha == 8:
            limpar_ficha(personagem)
        	
        elif escolha == 9:
            banco(personagem)

        elif escolha == 10:
            print("Pesca ainda não implementada!")
        
        elif escolha == len(OPCOES_MENU_JOGO):
            print("Saindo...\nAté logo!")
            break

def main():
    while True:
        print("====================")
        print("     RPG Python     ")
        print("====================")

        for numero, opcao in enumerate(OPCOES_MENU_PRINCIPAL, start=1):
            print(f"{numero} - {opcao}")

        try:
            escolha = int(
                input(
                    f"Por favor, escolha uma opção "
                    f"(1-{len(OPCOES_MENU_PRINCIPAL)}): "
                )
            )

        except ValueError:
            print("Opção inválida! Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(OPCOES_MENU_PRINCIPAL):
            print("Opção inválida, tente novamente.")
            continue

        if escolha == 1:
            iniciar()

        elif escolha == 2:
            criar_personagem(personagens)

        elif escolha == 3:
            print("Tutorial ainda não implementado!")
        
        elif escolha == 4:
            excluir(personagens)

        elif escolha == len(OPCOES_MENU_PRINCIPAL):
            print("Saindo...")
            break


if __name__ == "main":
    main()