# Gerador de Nomes para Personagens

Um gerador simples de personagens de RPG feito em Python. A cada execução, o programa sorteia um nome, uma classe, uma raça e valores aleatórios para os atributos do personagem.

## Funcionalidades

- Sorteio de nomes de personagens
- Sorteio de classes de RPG
- Sorteio de raças fantásticas
- Geração de sete atributos com valores de 1 a 20:
  - Força
  - Percepção
  - Resistência
  - Carisma
  - Inteligência
  - Agilidade
  - Sorte
- Exibição do personagem diretamente no terminal

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa

## Como executar

1. Clone ou baixe este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python3 main.py
```

No Windows, também é possível usar:

```bash
python main.py
```

## Exemplo de saída

```text
======================================
       GERADOR DE PERSONAGENS
======================================
Seu novo personagem está pronto!

Nome: Ayla
Classe: Arqueiro
Raça: Elfo

Atributos:
Força: 14
Percepção: 9
Resistência: 17
Carisma: 12
Inteligência: 15
Agilidade: 18
Sorte: 6

Boa aventura!
```

Os resultados são aleatórios, portanto cada execução pode gerar um personagem diferente.

## Estrutura do projeto

```text
.
├── main.py      # Código principal do gerador
├── README.md    # Documentação do projeto
└── .gitignore   # Arquivos ignorados pelo Git
```

## Licença

Este projeto é livre para estudo, uso e modificação.
