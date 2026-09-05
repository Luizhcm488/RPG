import time
import random
from persistencia import salvar_personagens

COOLDOWN_TRABALHO = 5 * 60
PENALIDADE_FICHA = 10
BONUS_SALARIO_NIVEL = 0.10

TRABALHOS = {
    "Gari": {
        "salario": 90,
        "chance": 90
    },

    "Caixa": {
        "salario": 95,
        "chance": 80
    },

    "Professor": {
        "salario": 115,
        "chance": 65
    },

    "Mecânico": {
        "salario": 127,
        "chance": 55
    },

    "Programador": {
        "salario": 150,
        "chance": 50
    },
 
       
    "Médico": {
        "salario": 200,
        "chance": 48
    },
    
    
    "Engenheiro": {
        "salario": 200,
        "chance": 48
    },


    "Presidente": {
        "salario": 500,
        "chance": 12
    }
}

def escolher_trabalho(personagem):
    while True:
        print("\n======== TRABALHOS ========")

        nomes_trabalhos = list(TRABALHOS)

        for numero, trabalho in enumerate(nomes_trabalhos, start=1):
            salario = TRABALHOS[trabalho]["salario"]
            print(f"{numero} - {trabalho} | R$ {salario}")

        print(f"{len(nomes_trabalhos) + 1} - Sair")
        
        try:
            escolha = int(
        input(
            f"Escolha um trabalho "
            f"(1-{len(nomes_trabalhos) + 1}): "
        )
    )

        except ValueError:
            print("Digite apenas números!")
            continue
        
        if escolha < 1 or escolha > len(nomes_trabalhos) + 1:
            print("Opção inválida!")
            continue
           
        if escolha == len(nomes_trabalhos) + 1:
            break
            
        trabalho_escolhido = nomes_trabalhos[escolha - 1]
        
        chance_emprego = TRABALHOS[trabalho_escolhido]["chance"]
        penalidade = personagem["ficha_criminal"] * PENALIDADE_FICHA
        chance_final = chance_emprego - penalidade
        if chance_final < 0:
            chance_final = 0
        sorteio = random.randint(1, 100)
        
        if sorteio <= chance_final:
            personagem["trabalho"] = trabalho_escolhido
            
            salvar_personagens()
            
            print(f"Parabéns! Você conseguiu o emprego de {trabalho_escolhido}!")
            return

        else:
            print(f"Agradecemos o seu interesse na vaga de {trabalho_escolhido}. Entraremos em contato em até 5 dias úteis.")

def trabalhar(personagem):
    if not personagem["trabalho"]:
        print(
            "Você precisa de um trabalho para poder trabalhar! "
            "Hora de distribuir currículos por aí..."
        )
        return

    trabalho_atual = personagem["trabalho"]

    # Cria o progresso da profissão caso seja a primeira vez
    if trabalho_atual not in personagem["xp_trabalho"]:
        personagem["xp_trabalho"][trabalho_atual] = {
            "xp": 0,
            "nivel": 1
        }

    dados_trabalho = personagem["xp_trabalho"][trabalho_atual]

    nivel = dados_trabalho["nivel"]

    # Cooldown
    COOLDOWN_TRABALHO
    agora = time.time()

    ultimo_trabalho = personagem["ultimo_trabalho"]

    if ultimo_trabalho is not None:
        tempo_passado = agora - ultimo_trabalho

        if tempo_passado < COOLDOWN_TRABALHO:
            tempo_restante = int(COOLDOWN_TRABALHO - tempo_passado)

            minutos, segundos = divmod(tempo_restante, 60)

            print(
                f"Você trabalhou demais como {trabalho_atual} "
                "e tá todo quebrado agora!"
            )

            print(
                f"Você pode trabalhar em "
                f"{minutos}min {segundos}seg"
            )
            return

    # Salário baseado no nível
    salario_base = TRABALHOS[trabalho_atual]["salario"]

    salario_final = int(
        salario_base * (1 + BONUS_SALARIO_NIVEL * (nivel - 1))
    )

    personagem["dinheiro"] += salario_final

    # XP
    xp_ganho = random.randint(10, 30)

    dados_trabalho["xp"] += xp_ganho

    xp_necessario = nivel * 100

    if dados_trabalho["xp"] >= xp_necessario:
        dados_trabalho["xp"] -= xp_necessario
        dados_trabalho["nivel"] += 1

        print(
            f"🎉 Você subiu para o nível "
            f"{dados_trabalho['nivel']} como {trabalho_atual}!"
        )

    personagem["ultimo_trabalho"] = agora

    salvar_personagens()

    print(
        f"Você trabalhou como {trabalho_atual} "
        f"e recebeu R${salario_final}!"
    )

    print(f"Você ganhou {xp_ganho} XP!")

    xp_proximo_nivel = dados_trabalho["nivel"] * 100

    print(
        f"{trabalho_atual} Nv. {dados_trabalho['nivel']} | "
        f"XP: {dados_trabalho['xp']}/{xp_proximo_nivel}"
    )

