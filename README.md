# RentSmart — Sistema de Orçamento de Locação

## Sobre o projeto

O RentSmart é um sistema desenvolvido em Python para a R.M Imóveis, com o objetivo de automatizar a elaboração de orçamentos de locação de imóveis.

O projeto utiliza Programação Orientada a Objetos (POO), organizando suas funcionalidades em classes e métodos.

## Funcionalidades

- Cadastro do nome do cliente.
- Identificação da presença de crianças.
- Seleção do tipo de imóvel.
- Definição da quantidade de quartos e vagas de garagem.
- Cálculo automático do aluguel.
- Aplicação de adicionais e descontos.
- Parcelamento da taxa contratual de R$ 2.000,00 em até 5 vezes.
- Geração de relatório CSV com projeção financeira de 12 meses.

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos (POO)
- Biblioteca CSV
- Biblioteca OS

## Estrutura do projeto

```text
RentSmart/
├── documentacao/
├── relatorios/
│   └── projecao_12_meses.csv
├── cliente.py
├── imovel.py
├── main.py
├── orcamento.py
└── README.md
```

## Como executar

1. Tenha o Python instalado.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no VS Code.
4. Execute o arquivo principal:

```bash
python main.py
```

## Relatórios

O sistema gera automaticamente o arquivo `projecao_12_meses.csv`, armazenado na pasta `relatorios`.

O relatório apresenta:
- Mês;
- Valor do aluguel;
- Parcela da taxa contratual;
- Total mensal.

## Objetivo acadêmico

Este projeto foi desenvolvido com a finalidade de aplicar conceitos de lógica de programação e Programação Orientada a Objetos, utilizando classes, objetos, atributos, métodos e manipulação de arquivos CSV.
