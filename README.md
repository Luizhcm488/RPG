#RPG em Python

RPG de terminal desenvolvido em Python com o objetivo de praticar lógica de programação, modularização, persistência de dados e desenvolvimento de sistemas.

O jogador pode criar personagens, trabalhar, evoluir em profissões, minerar, comprar equipamentos, apostar no cassino, utilizar serviços bancários e realizar outras atividades dentro do jogo.

O projeto começou como um programa concentrado em poucos arquivos e posteriormente foi refatorado para uma estrutura modular, separando cada sistema de acordo com sua responsabilidade.

##Funcionalidades

- Criação e exclusão de personagens
- Persistência de dados utilizando JSON
- Sistema de inventário
- Loja de equipamentos
- Sistema de mineração
- Diferentes níveis de ferramentas
- Durabilidade de equipamentos
- Sistema de empregos
- Chance de contratação
- Penalidade de contratação por ficha criminal
- Progressão e XP individual por profissão
- Aumento de salário conforme o nível profissional
- Cooldown entre trabalhos
- Sistema de crimes
- Sistema de ficha criminal
- Cassino com caça-níquel
- Sistema bancário
  - Depósitos
  - Saques
  - Extrato
  - Investimentos
  - Carteira de investimentos
- Compatibilidade com personagens criados em versões anteriores
- Sistema de pesca em desenvolvimento

##Estrutura do projeto

```text
RPG/
├── main.py
├── personagens.py
├── persistencia.py
├── itens.py
├── trabalhos.py
├── crime.py
├── mineracao.py
├── pesca.py
├── loja.py
├── cassino.py
├── banco.py
└── personagens.json
```

### Responsabilidade dos módulos

- `main.py` — menus principais e fluxo do jogo
- `personagens.py` — criação, exclusão e inventário dos personagens
- `persistencia.py` — carregamento e salvamento dos dados
- `itens.py` — catálogo e atributos dos equipamentos
- `trabalhos.py` — empregos, trabalho e progressão profissional
- `crime.py` — crimes e sistema de ficha criminal
- `mineracao.py` — sistema de mineração
- `pesca.py` — sistema de pesca
- `loja.py` — compra de equipamentos
- `cassino.py` — sistema de caça-níquel
- `banco.py` — banco, extrato e investimentos

##Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub

##Como executar

Clone o repositório:

git clone git@github.com:Luizhcm488/RPG.git

Entre na pasta:


cd RPG

Execute:

python3 main.py


O projeto utiliza apenas bibliotecas padrão do Python, portanto não é necessário instalar dependências externas.

##Persistência de dados

Os personagens e seus respectivos dados são armazenados em JSON, permitindo que o progresso seja mantido mesmo após fechar o programa.

Entre os dados persistidos estão:

- Dinheiro
- Saldo bancário
- Inventário
- Trabalho atual
- XP e nível das profissões
- Investimentos
- Extrato bancário
- Ficha criminal
- Cooldowns e atividades

##Em desenvolvimento

Algumas funcionalidades ainda estão sendo desenvolvidas ou planejadas, como:

- Sistema completo de pesca
- Novos itens e equipamentos
- Expansão das atividades disponíveis
- Melhorias no balanceamento da economia
- Novos eventos e sistemas de progressão

##Objetivo do projeto

Este projeto foi desenvolvido durante meus estudos de Python e Análise e Desenvolvimento de Sistemas.

Além da prática de lógica de programação, o projeto também é utilizado para estudar conceitos como:

- Separação de responsabilidades
- Modularização
- Manipulação de dicionários e listas
- Funções
- Imports entre módulos
- Tratamento de exceções
- Persistência de dados
- Estruturação e manutenção de projetos

##Autor

Desenvolvido por **Luiz Henrique**.

GitHub: [@candeany](https://github.com/candeany)
