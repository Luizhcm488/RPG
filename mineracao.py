import random
import time
from persistencia import salvar_personagens

COOLDOWN_MINERACAO = 10 * 60
MAX_MINERACOES = 3

def mineracao(personagem):
    picareta_usada = None
    maior_nivel = -1

    for item, dados in personagem["inventario"].items():
        if dados["tipo"] == "picareta":
            nivel = dados["nivel"]

        if nivel > maior_nivel:
            maior_nivel = nivel
            picareta_usada = item

    if picareta_usada is None:
        print("Você precisa de uma picareta para minerar!")
        return

    coolCOOLDOWN_MINERACAOdown = 10 * 60
    agora = time.time()
    inicio_ciclo = personagem["inicio_ciclo_mineracao"]
    
    if inicio_ciclo is not None:
        tempo_passado = agora - inicio_ciclo
    
        if tempo_passado >= COOLDOWN_MINERACAO:
            personagem["mineracoes_restantes"] = MAX_MINERACOES
            personagem["inicio_ciclo_mineracao"] = None
            
    if personagem["mineracoes_restantes"] == 0:
        inicio_ciclo = personagem["inicio_ciclo_mineracao"]
    	
        tempo_passado = agora - inicio_ciclo
        tempo_restante = int(COOLDOWN_MINERACAO - tempo_passado)
        
        minutos, segundos = divmod(tempo_restante, 60)
    	
        print("Você minerou bastante, seus braços estão destruídos!")
        print(f"Você pode minerar novamente em {minutos}min {segundos}seg")
        return
    
    if personagem["inicio_ciclo_mineracao"] is None:
        personagem["inicio_ciclo_mineracao"] = agora

    chance = random.randint(1, 100)

    if chance <= 46:
        dados_picareta = personagem["inventario"][picareta_usada]

        ganho = random.randint(
            dados_picareta["ganho_min"],
            dados_picareta["ganho_max"]
        )

        personagem["dinheiro"] += ganho

        if ganho <= 100:
            print(
                f"Você minerou e teve a sorte de ganhar R${ganho}!\n"
                f"Hora de gastar!!"
            )

        elif ganho <= 200:
            print(
                f"UAU! Você minerou e ganhou R${ganho}! "
                f"Será você o barão do ouro?!"
            )

        else:
            print(
                f"PARABÉNS!! VOCÊ GANHOU R${ganho}!!!!!!! "
                f"Você está cada vez mais próximo da riqueza!!!"
            )

    elif chance <= 90:
        print("Você minerou... E não conseguiu nada... Que azar.")

    else:
        print(
            "Você minerou e conseguiu uma peça de ouro de 5KG "
            "avaliada em 1 MILHÃO DE REAIS!!!\n"
            "Mas um elfo maldito estava vendo tudo e te roubou..."
        )

    personagem["inventario"][picareta_usada]["durabilidade"] -= 1
    personagem["mineracoes_restantes"] -= 1
    print(f"Minerações Restantes: {personagem['mineracoes_restantes']}/{MAX_MINERACOES}")

    if personagem["inventario"][picareta_usada]["durabilidade"] <= 0:
        del personagem["inventario"][picareta_usada]
        print(f"Sua {picareta_usada} quebrou!")

    salvar_personagens()