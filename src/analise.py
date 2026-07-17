"""
Otimização de doações da gincana — ranking de produtos e mercados
por razão pontos/preço.

Origem: numa gincana de doação no colégio, cada item de supermercado doado
valia uma quantidade fixa de pontos, e times competiam para arrecadar o
maior número de pontos. Comparando produtos e preços em diferentes
mercados, dava pra descobrir onde cada item "rendia" mais pontos por
real gasto — e assim doar mais pontuação gastando o mesmo dinheiro.

Este script recria essa lógica com pandas: carrega o dataset de produtos,
calcula a razão pontos/preço de cada item em cada mercado e gera dois
rankings — o melhor custo-benefício por produto e por mercado.
"""

import pandas as pd

CAMINHO_DADOS = "data/produtos.csv"


def carregar_dados(caminho: str = CAMINHO_DADOS) -> pd.DataFrame:
    df = pd.read_csv(caminho)
    df["razao_pontos_preco"] = df["pontos"] / df["preco"]
    return df


def melhor_opcao_por_produto(df: pd.DataFrame) -> pd.DataFrame:
    """Para cada produto, mostra o mercado com melhor razão pontos/preço."""
    idx = df.groupby("produto")["razao_pontos_preco"].idxmax()
    melhores = df.loc[idx].sort_values("razao_pontos_preco", ascending=False)
    return melhores[["produto", "mercado", "pontos", "preco", "razao_pontos_preco"]]


def ranking_mercados(df: pd.DataFrame) -> pd.DataFrame:
    """Compara mercados pela razão média pontos/preço entre todos os itens."""
    ranking = (
        df.groupby("mercado")["razao_pontos_preco"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"razao_pontos_preco": "razao_media_pontos_preco"})
    )
    return ranking


def top_produtos_gerais(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Top N combinações produto+mercado com melhor razão pontos/preço."""
    return df.sort_values("razao_pontos_preco", ascending=False).head(n)[
        ["produto", "mercado", "pontos", "preco", "razao_pontos_preco"]
    ]


def main() -> None:
    df = carregar_dados()

    print("=" * 60)
    print("Melhor mercado por produto (maior razão pontos/preço)")
    print("=" * 60)
    print(melhor_opcao_por_produto(df).to_string(index=False))

    print()
    print("=" * 60)
    print("Ranking de mercados (razão média pontos/preço)")
    print("=" * 60)
    print(ranking_mercados(df).to_string(index=False))

    print()
    print("=" * 60)
    print("Top 5 combinações produto+mercado (melhor custo-benefício)")
    print("=" * 60)
    print(top_produtos_gerais(df).to_string(index=False))


if __name__ == "__main__":
    main()
