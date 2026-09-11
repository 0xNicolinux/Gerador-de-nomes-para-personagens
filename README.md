# Gerador de Nomes para Personagens

Um gerador simples de personagens de RPG feito em Python. A cada execução, o programa sorteia um nome, uma classe, uma raça e valores aleatórios para os atributos do personagem. Ao final, o programa também identifica qual é o maior atributo do personagem.

## Funcionalidades

* Sorteio de nomes de personagens
* Sorteio de classes de RPG
* Sorteio de raças fantásticas
* Geração de sete atributos com valores aleatórios de 1 a 20:

  * Força
  * Percepção
  * Resistência
  * Carisma
  * Inteligência
  * Agilidade
  * Sorte
* Exibição dos atributos no terminal
* Identificação do maior atributo e seu respectivo valor

## Requisitos

* Python 3.8 ou superior
* Nenhuma biblioteca externa

O projeto utiliza apenas a biblioteca padrão `random` do Python.

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

O maior atributo é Agilidade com 18 pontos!

Boa aventura!
```

Os resultados são gerados aleatoriamente, portanto cada execução pode produzir um personagem diferente.

## Estrutura do projeto

```text
.
├── main.py      # Código principal do gerador
├── README.md    # Documentação do projeto
└── .gitignore   # Arquivos ignorados pelo Git
```

## Conceitos praticados

Este projeto foi desenvolvido como exercício de aprendizado em Python e utiliza conceitos como:

* Variáveis e listas
* Dicionários
* Laços `for`
* Condicionais `if`
* Funções
* Retorno de múltiplos valores
* Métodos de dicionários, como `.items()`
* Formatação de strings com f-strings
* Geração de números aleatórios
* Organização do código em funções

## Licença

Este projeto é livre para estudo, uso e modificação.
