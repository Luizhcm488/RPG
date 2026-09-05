import random
from persistencia import salvar_personagens

CUSTO_LIMPAR_FICHA = 500

def crime(personagem):
    chance = random.randint(1, 100)
    if chance <= 34:
        ganho = random.randint(10, 700)
        personagem["dinheiro"] += ganho
		
        salvar_personagens()
		
        if ganho <= 100:
            print(f"Você roubou senhorinhas na rua e ganhou R${ganho}! Que sem coração...")
        elif ganho <= 300:
            print(f"Você subiu no crime e vendeu substâncias ilícitas. Você ganhou {ganho}!")
        elif ganho <= 600:
            print(f"Você começou a roubar bancos e ganhou {ganho}! Cuidado, nessa vida, quanto maior o degrau, maior a queda...")
        else:
            print(f"Você virou o chefão da zorra toda! Seu nome é Carl Jhonson e você tá milionário! {ganho} pila estourando no bolso!")
    elif chance <= 67:
        print("Você ia roubar uma senhoria que estava atravessando a rua, mas uma mulher começou a gritar. Você saiu correndo, tropeçou e conseguiu fugir. A única coisa que você perdeu foi sua dignidade.")
    else:
        print("Você foi pego tentando roubar. As pessoas em volta te bateram e você foi preso e perdeu tudo o que você tinha antes. Boa sorte tentando arrumar emprego!")
        personagem["dinheiro"] = 0
        personagem["ficha_criminal"] += 1
        salvar_personagens()

def limpar_ficha(personagem):
    if personagem["ficha_criminal"] == 0:
        print("Você é um cidadão honesto, não tem ficha pra limpar!")

    else:
        if personagem["dinheiro"] < CUSTO_LIMPAR_FICHA:
            print(
                f"Tá liso dorme fi. Precisa de R${CUSTO_LIMPAR_FICHA} pra limpar a ficha, "
                f"aparentemente você só tem R${personagem['dinheiro']}"
            )

        else:
            personagem["ficha_criminal"] = 0
            personagem["dinheiro"] -= CUSTO_LIMPAR_FICHA
            
            salvar_personagens()
            
            print(f"Você gastou R${CUSTO_LIMPAR_FICHA} para limpar sua ficha criminal!")
            print(
                "Agora que você tem a ficha limpa, talvez eles leiam "
                "seu currículo ao invés de só jogar fora..."
            )