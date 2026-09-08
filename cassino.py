import random
from persistencia import salvar_personagens

JACKPOTS = {
    "🍓": 300,
    "🍒": 500,
    "🍎": 700,
    "🍅": 900,
    "🌶️": 1100,
    "🍉": 1500,
    "💎": 2000
}

CUSTO_CASSINO = 50

def cassino(personagem):


    if personagem["dinheiro"] < CUSTO_CASSINO:
        print(
            "Pelo visto alguém tá liso e não tem "
            "R$50 pra jogar no cassino KKKKKKKKKKK"
        )
        return

    personagem["dinheiro"] -= CUSTO_CASSINO

    simbolos = list(JACKPOTS)

    slot1 = random.choice(simbolos)
    slot2 = random.choice(simbolos)
    slot3 = random.choice(simbolos)

    print(f"\n🎰 [ {slot1} ] [ {slot2} ] [ {slot3} ] 🎰")

    if slot1 == slot2 == slot3:
        premio = JACKPOTS[slot1]
        personagem["dinheiro"] += premio
        
        
        if slot1 == "🍓":
            print(
                f"É, até que você é sortudinho(a)... "
                f"R${premio} na conta."
            )

        elif slot1 == "🍒":
            print(
                f"Olha só! Parabéns, nunca vi ninguém "
                f"ganhar R${premio} fácil assim!"
            )

        elif slot1 == "🍎":
            print(
                f"Três iguais?! Você só pode ser um mago "
                f"ou algo assim! +R${premio}"
            )

        elif slot1 == "🍅":
            print(
                f"UM TOMATE?! KKKKKKKKK "
                f"Seja lá como isso vale dinheiro, +R${premio}!"
            )

        elif slot1 == "🌶️":
            print(
                f"UAU! Você pode ficar sem trabalhar o resto "
                f"da semana! R${premio} entrando na conta!"
            )

        elif slot1 == "🍉":
            print(
                f"VOCÊ É MUITO SORTUDO! "
                f"Toma aí seus R${premio}!!!"
            )

        elif slot1 == "💎":
            print(
                "JAAACKPOOOOOOT HAHAHAHA!!!\n"
                "AUMENTE O VOLUME, ISSO VAI SER UM FUNERAL "
                "PARA OS VIVOS!!!\n"
                f"+R${premio}"
            )

    else:
        
        print(
            "É... parece que não foi dessa vez... "
            "Mas tenta de novo, tenho certeza que na próxima "
            "você consegue..."
        )
    salvar_personagens()