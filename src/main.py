from pathlib import Path
import pandas as pd

from src.leitura import ler_json, ler_csv, ler_txt
from src.processamento import tratar_dados
from src.analise import (
    quantidade_total_atendimentos,
    quantidade_por_categoria,
    quantidade_por_status,
    tempo_medio_atendimento,
    categoria_mais_frequente,
    percentual_invalidos
)

from src.validacao import validar_registro

from src.relatorios import (
    grafico_por_categoria,
    grafico_por_status
)

def main():
    print("Sistema de Análise de Atendimentos de Suporte Técnico")

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

    total_original = len(atendimentos)

    atendimentos = tratar_dados(atendimentos, categorias)

    registros_validos = []
    registros_invalidos = []

    for _, registro in atendimentos.iterrows():
        registro_dict = registro.to_dict()
        resultado = validar_registro(registro_dict)

        if resultado["valido"]:
            registros_validos.append(registro_dict)
        else:
            registros_invalidos.append({
                "registro": registro_dict,
                "erros": resultado["erros"]
            })
    atendimentos_validos = pd.DataFrame(registros_validos)
    total_invalidos = len(registros_invalidos)        

    total_atendimentos = quantidade_total_atendimentos(atendimentos_validos)
    por_categoria = quantidade_por_categoria(atendimentos_validos)
    por_status = quantidade_por_status(atendimentos_validos)
    tempo_medio = tempo_medio_atendimento(atendimentos_validos)
    categoria_frequente = categoria_mais_frequente(atendimentos_validos)
    grafico_por_categoria(por_categoria, "graficos")
    grafico_por_status(por_status, "graficos")

    percentual = percentual_invalidos(
        total_original,
        total_invalidos
    )

    print("\n--- RESUMO ---")
    print(f"Total de atendimentos: {total_atendimentos}")
    print(f"Tempo médio: {tempo_medio:.2f} minutos")
    categorias_frequentes = ", ".join(categoria_frequente)
    print(f"Categoria(s) mais frequente(s): {categorias_frequentes}")
    print(f"Percentual de registros inválidos: {percentual:.2f}%")

    print("\n--- ATENDIMENTOS POR CATEGORIA ---")
    for categoria, quantidade in por_categoria.items():
        print(f"{categoria}: {quantidade}")

    print("\n--- ATENDIMENTOS POR STATUS ---")
    for status, quantidade in por_status.items():
        print(f"{status}: {quantidade}")


if __name__ == "__main__":
    main()