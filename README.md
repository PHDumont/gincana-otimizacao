# Otimização de Doações — da Gincana ao Pandas

## Por que fiz esse projeto

Anos atrás, ainda na escola, participei de uma gincana em que cada time
precisava arrecadar produtos de supermercado para doação — e cada item
valia uma quantidade fixa de pontos. Sem saber que aquilo tinha nome, eu
montei uma planilha comparando preços dos mesmos produtos em diferentes
mercados e calculando qual rendia mais pontos por real gasto. Isso
permitia decidir onde comprar cada item para maximizar a pontuação do
time gastando o mesmo orçamento.

Anos depois, ao estudar Ciência da Computação, percebi que aquilo era, na
prática, um mini projeto de otimização de dados. Este repositório recria
a ideia original com Python e pandas, como projeto de portfólio na
transição para Ciência de Dados.

## O que faz

- Carrega um dataset de produtos (nome, categoria, pontos, preço) vendidos
  em três mercados diferentes.
- Calcula a razão pontos/preço de cada item em cada mercado.
- Rankeia:
  - o melhor mercado para comprar cada produto (maior razão pontos/preço);
  - os mercados no geral, pela razão média entre todos os itens;
  - as 5 melhores combinações produto+mercado (melhor custo-benefício).

## Stack

- Python 3
- pandas

## Estrutura

```
gincana-otimizacao/
├── data/
│   └── produtos.csv       # dataset de produtos, pontos e preços por mercado
├── src/
│   └── analise.py         # script de análise e ranking
└── README.md
```

> Nota: o dataset (`data/produtos.csv`) é fictício — a planilha original da
> escola não foi preservada. Os valores foram recriados para reproduzir a
> mesma lógica de comparação (pontos por real gasto) usada no projeto real.

## Como rodar

```bash
pip install pandas
python src/analise.py
```

## Principal desafio técnico

Modelar a comparação de forma que funcionasse tanto por produto (qual
mercado é melhor para *esse* item) quanto por mercado (qual mercado é
melhor *no geral*), sem duplicar lógica — resolvido agrupando o mesmo
DataFrame de duas formas diferentes com `groupby` do pandas.

## Próximos passos possíveis

- Adicionar mais mercados e categorias de produto.
- Testar um modelo simples de regressão/classificação sobre o dataset
  (ex.: prever a melhor faixa de preço por categoria).
- Expor os rankings em uma pequena interface web.
