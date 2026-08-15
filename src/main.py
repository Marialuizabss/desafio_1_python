from pathlib import Path

from src.leitura import ler_json, ler_csv, ler_txt


def main():

    config = ler_json(Path("data/config.json"))

    atendimentos = ler_csv(
        Path(config["arquivo_atendimentos"]),
        config["separador_csv"]
    )

    categorias = ler_json(
        Path(config["arquivo_categorias"])
    )

    observacoes = ler_txt(
        Path(config["arquivo_observacoes"])
    )

    print("\n--- ATENDIMENTOS ---")
    print(atendimentos.head())

    print("\n--- CATEGORIAS ---")
    print(categorias)

    print("\n--- OBSERVAÇÕES ---")
    print(observacoes)


if __name__ == "__main__":
    main()