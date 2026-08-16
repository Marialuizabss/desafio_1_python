from pathlib import Path
import matplotlib.pyplot as plt


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