from pathlib import Path
import matplotlib.pyplot as plt
import json
import pandas as pd


def grafico_por_categoria(dados: dict, diretorio: str) -> None:
    """
    Gera um gráfico de barras com a quantidade de atendimentos por categoria.
    """

    caminho_saida = Path(diretorio)
    caminho_saida.mkdir(parents=True, exist_ok=True)

    categorias = list(dados.keys())
    quantidades = list(dados.values())

    cores = [
    "#007BFF",  
    "#FF6B00", 
    "#32CD32", 
    "#FF2D55",  
    "#9B30FF"   
    ]

    plt.figure(figsize=(10, 6))

    barras = plt.bar(
        categorias,
        quantidades,
        color=cores[:len(categorias)]
    )

    plt.title(
        "Atendimentos por Categoria",
        fontsize=16,
        fontweight="bold"
    )

    plt.ylabel("Quantidade de atendimentos")
    plt.xticks(rotation=30, ha="right")

    plt.bar_label(barras, padding=3)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.tight_layout()

    plt.savefig(
        caminho_saida / "atendimentos_por_categoria.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def grafico_distribuicao_tempo(df, diretorio: str) -> None:
    """
    Gera um histograma dos tempos de atendimento.
    Valores muito extremos são destacados separadamente.
    """

    caminho_saida = Path(diretorio)
    caminho_saida.mkdir(parents=True, exist_ok=True)

    tempos = pd.to_numeric(
        df["tempo_minutos"],
        errors="coerce"
    ).dropna()

    q1 = tempos.quantile(0.25)
    q3 = tempos.quantile(0.75)
    iqr = q3 - q1

    limite_superior = q3 + 1.5 * iqr

    tempos_normais = tempos[tempos <= limite_superior]
    outliers = tempos[tempos > limite_superior]

    plt.figure(figsize=(10, 6))

    plt.hist(
        tempos_normais,
        bins=10,
        color="#00BFFF",
        edgecolor="white"
    )

    plt.title(
        "Distribuição dos Tempos de Atendimento",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Tempo de atendimento (minutos)")
    plt.ylabel("Quantidade de atendimentos")

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    if not outliers.empty:
        plt.text(
            0.98,
            0.95,
            f"Valor(es) extremo(s): {', '.join(map(str, outliers.astype(int)))} min",
            transform=plt.gca().transAxes,
            ha="right",
            va="top",
            fontsize=10,
            fontweight="bold"
        )

    plt.tight_layout()

    plt.savefig(
        caminho_saida / "distribuicao_tempo_atendimento.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def grafico_por_status(dados: dict, diretorio: str) -> None:
    """
    Gera um gráfico de barras com a quantidade de atendimentos por status.
    """

    caminho_saida = Path(diretorio)
    caminho_saida.mkdir(parents=True, exist_ok=True)

    status = list(dados.keys())
    quantidades = list(dados.values())

    cores_status = {
        "ABERTO": "#FF2D55",
        "EM ANDAMENTO": "#FF9500",
        "RESOLVIDO": "#32CD32"
    }

    cores = [
        cores_status.get(item, "#007BFF")
        for item in status
    ]

    plt.figure(figsize=(8, 5))

    barras = plt.bar(
        status,
        quantidades,
        color=cores
    )

    plt.title(
        "Atendimentos por Status",
        fontsize=16,
        fontweight="bold"
    )

    plt.ylabel("Quantidade de atendimentos")

    plt.bar_label(barras, padding=3)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.tight_layout()

    plt.savefig(
        caminho_saida / "atendimentos_por_status.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

def exportar_csv(df, diretorio: str) -> None:
    """
    Exporta os dados tratados para um arquivo CSV.
    """

    caminho_saida = Path(diretorio)
    caminho_saida.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        caminho_saida / "atendimentos_processados.csv",
        index=False,
        encoding="utf-8"
    )   

def exportar_resumo_json(resumo: dict, diretorio: str) -> None:
    """
    Exporta o resumo dos indicadores para um arquivo JSON.
    """

    caminho_saida = Path(diretorio)
    caminho_saida.mkdir(parents=True, exist_ok=True)

    with open(
        caminho_saida / "resumo.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(
            resumo,
            arquivo,
            ensure_ascii=False,
            indent=4
        )     