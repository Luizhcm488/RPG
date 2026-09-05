from persistencia import salvar_personagens


opcoes_investimento = {
    "Ouro": {
        "cota": 219,
        "rendimento": 0.70
    },
    
    "Energia": {
        "cota": 63,
        "rendimento": 0.18
    },
    
    "Tecnologia": {
        "cota": 91,
        "rendimento": 0.36
    },
    
    "Cripto": {
        "cota": 258,
        "rendimento": 0.83
    },
    
    "Indústrias": {
        "cota": 25,
        "rendimento": 0.27
    },
    
    "Imóveis": {
        "cota": 120,
        "rendimento": 0.50
    },
    
    "Automóveis": {
    	"cota": 185,
    	"rendimento": 0.47
    }

}

opcoes_banco = ["Saldo",
                        "Depositar",
                        "Sacar",
                        "Extrato",
                        "Investir",
                        "Carteira de Investimentos",
                        "Sair"]


def saldo(personagem):
	print(f"O seu saldo bancário é de R${personagem['saldo']}!")



def depositar(personagem):
    print("Opção 'Depositar' selecionada!")
	
    try:
        deposito = int(input(f"Seu dinheiro: R${personagem['dinheiro']}\nQual quantia você gostaria de depositar? R$"))
	
    except ValueError:
        print("Digite apenas números!")
        return

    if deposito > personagem["dinheiro"]:
        print("Saldo insuficiente!")
        return
	
    if deposito <= 0:
        print("Valor inválido!")
        return
	
    personagem["dinheiro"] -= deposito
    personagem["saldo"] += deposito
	
    personagem["extrato"].append(f"Depósito Realizado: +{deposito:.2f}")
    salvar_personagens()
    print(f"A quantia de {deposito} foi depositada com sucesso!")
	
	
def sacar(personagem):
    print("Opção 'Sacar' selecionada!")

    try:
        saque = int(
            input(
                f"Seu saldo bancário atual é de R${personagem['saldo']}.\n"
                "Qual quantia você gostaria de sacar? R$"
            )
        )

    except ValueError:
        print("Digite apenas números!")
        return

    if saque > personagem["saldo"]:
        print("Saldo insuficiente!")
        return

    if saque <= 0:
        print("Quantia inválida!")
        return

    personagem["saldo"] -= saque
    personagem["dinheiro"] += saque

    
    personagem["extrato"].append(f"Saque Realizado: -{saque:.2f}")
    
    salvar_personagens()
    print(f"Você sacou R${saque} com sucesso!")
    
    
def mostrar_extrato(personagem):
    print("=================")
    print("     EXTRATO     ")
    print("=================")

    if not personagem["extrato"]:
        print("Nenhuma movimentação realizada!")
        return

    for numero, movimentacao in enumerate(
        personagem["extrato"],
        start=1
    ):
        print(f"{numero} - {movimentacao}")

    print(f"\nSaldo atual: R${personagem['saldo']:.2f}")
	

def investir(personagem):
    while True:
        print("\n======== INVESTIMENTOS ========")
        print(f"Saldo bancário: R${personagem['saldo']:.2f}")

        investimentos = list(opcoes_investimento)

        for numero, investimento in enumerate(investimentos, start=1):
            cota = opcoes_investimento[investimento]["cota"]
            rendimento = opcoes_investimento[investimento]["rendimento"]

            print(
                f"{numero} - {investimento} | "
                f"Cota: R${cota} | "
                f"Rendimento: {rendimento * 100:.0f}%"
            )

        print(f"{len(investimentos) + 1} - Sair")

        try:
            escolha = int(
                input(
                    f"Escolha um investimento "
                    f"(1-{len(investimentos) + 1}): "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(investimentos) + 1:
            print("Opção inválida!")
            continue

        if escolha == len(investimentos) + 1:
            break

        investimento_escolhido = investimentos[escolha - 1]

        valor_cota = opcoes_investimento[investimento_escolhido]["cota"]

        try:
            quantidade = int(
                input(
                    f"Quantas cotas de {investimento_escolhido} "
                    "você gostaria de comprar? "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        valor_total = quantidade * valor_cota

        if quantidade <= 0:
            print("Quantidade inválida!")
            continue

        if valor_total > personagem["saldo"]:
            print("Saldo bancário insuficiente!")
            continue

        personagem["saldo"] -= valor_total

        if investimento_escolhido not in personagem["investimentos"]:
            personagem["investimentos"][investimento_escolhido] = 0

        personagem["investimentos"][investimento_escolhido] += quantidade

        personagem["extrato"].append(
            f"Investimento em {investimento_escolhido}: "
            f"-R${valor_total:.2f}"
        )

        salvar_personagens()

        print(
            f"Você comprou {quantidade} cota(s) de "
            f"{investimento_escolhido} por R${valor_total:.2f}!"
        )
	

def carteira_investimentos(personagem):
    print("===============================")
    print("   CARTEIRA DE INVESTIMENTOS   ")
    print("===============================")

    if not personagem["investimentos"]:
        print("Nenhum investimento!")
        return

    for numero, investimento in enumerate(
        personagem["investimentos"],
        start=1
        ):
        quantidade = personagem["investimentos"][investimento]
        valor_cota = opcoes_investimento[investimento]["cota"]
        rendimento = opcoes_investimento[investimento]["rendimento"]

        valor_total = valor_cota * quantidade

        print(
            f"{numero} - {investimento}\n"
            f"    Cotas: {quantidade}\n"
            f"    Valor por cota: R${valor_cota:.2f}\n"
            f"    Total investido: R${valor_total:.2f}\n"
            f"    Rendimento: {rendimento * 100:.0f}%"
        )



def banco(personagem):
    while True:
        print("=====================")
        print("      BANCO RPG      ")
        print("=====================")
        for numero, opcao in enumerate(opcoes_banco, start=1):
            print(f"{numero} - {opcao}")

        try:
            escolha = int(
                input(
                    f"Escolha uma opção "
                    f"(1-{len(opcoes_banco)}): "
                )
            )

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha < 1 or escolha > len(opcoes_banco):
            print("Opção inválida!")
            continue
        
        if escolha == 1:
            saldo(personagem)
        	
        elif escolha == 2:
            depositar(personagem)
        
        elif escolha == 3:
            sacar(personagem)
        	
        elif escolha == 4:
            mostrar_extrato(personagem)
        	
        elif escolha == 5:
            investir(personagem)

        elif escolha == 6:
            carteira_investimentos(personagem)

        elif escolha == len(opcoes_banco):
            print("Saindo...\nAté logo!")
            break

