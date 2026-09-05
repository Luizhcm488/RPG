import json
from pathlib import Path
CAMINHO_PERSONAGENS = Path(__file__).parent / "personagens.json"



def salvar_personagens():
    with open(CAMINHO_PERSONAGENS, "w", encoding="utf-8") as arquivo:
        json.dump(
            personagens,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def carregar_personagens():
    try:
        with open(CAMINHO_PERSONAGENS, "r", encoding="utf-8") as arquivo:
            personagens_carregados = json.load(arquivo)

        for personagem in personagens_carregados.values():
            personagem.setdefault("dinheiro", 50)
            personagem.setdefault("xp", 0)
            personagem.setdefault("nivel", 1)
            personagem.setdefault("saldo", 0)
            personagem.setdefault("trabalho", None)
            personagem.setdefault("xp_trabalho", {})
            personagem.setdefault("ultimo_trabalho", None)
            personagem.setdefault("mineracoes_restantes", 3)
            personagem.setdefault("inicio_ciclo_mineracao", None)
            personagem.setdefault("extrato", [])
            personagem.setdefault("investimentos", {})
            personagem.setdefault("inventario", {})
            personagem.setdefault("ficha_criminal", 0)

        return personagens_carregados

    except FileNotFoundError:
        return {}

    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro: o arquivo de personagens está corrompido!")
        return {}

personagens = carregar_personagens()