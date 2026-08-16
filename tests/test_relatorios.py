import pandas as pd

from src.relatorios import (
    grafico_por_categoria,
    grafico_por_status,
    exportar_csv,
    exportar_resumo_json,
    grafico_distribuicao_tempo
)

def test_grafico_por_categoria(tmp_path):
    dados = {
        "Senha": 10,
        "Acesso ao AVA": 8,
        "Configuração do Python": 5
    }

    grafico_por_categoria(dados, tmp_path)

    arquivo = tmp_path / "atendimentos_por_categoria.png"

    assert arquivo.exists()

def test_grafico_por_status(tmp_path):
    dados = {
        "RESOLVIDO": 20,
        "ABERTO": 15,
        "EM ANDAMENTO": 10
    }

    grafico_por_status(dados, tmp_path)

    arquivo = tmp_path / "atendimentos_por_status.png"

    assert arquivo.exists()    

def test_exportar_csv(tmp_path):
    import pandas as pd

    df = pd.DataFrame({
        "protocolo": ["SUP-2026-0001"],
        "status": ["RESOLVIDO"]
    })

    exportar_csv(df, tmp_path)

    arquivo = tmp_path / "atendimentos_processados.csv"

    assert arquivo.exists()    

def test_exportar_resumo_json(tmp_path):
    resumo = {
        "total_atendimentos": 140,
        "tempo_medio": 107.84,
        "percentual_invalidos": 6.0
    }

    exportar_resumo_json(resumo, tmp_path)

    arquivo = tmp_path / "resumo.json"

    assert arquivo.exists()    

def test_grafico_distribuicao_tempo(tmp_path):

    df = pd.DataFrame({
        "tempo_minutos": [10, 20, 30, 40, 50]
    })

    grafico_distribuicao_tempo(df, tmp_path)

    arquivo = tmp_path / "distribuicao_tempo_atendimento.png"

    assert arquivo.exists()    