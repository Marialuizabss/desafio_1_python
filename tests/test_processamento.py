import pandas as pd

from src.processamento import (
    remover_espacos,
    tratar_valores_ausentes,
    remover_duplicados,
    mapear_categorias,
    padronizar_datas
)


def test_remover_espacos():
    df = pd.DataFrame({
        "email": ["  maria@gmail.com  "]
    })

    resultado = remover_espacos(df)

    assert resultado.loc[0, "email"] == "maria@gmail.com"


def test_valor_vazio_vira_na():
    df = pd.DataFrame({
        "email": ["   "]
    })

    resultado = tratar_valores_ausentes(df)

    assert pd.isna(resultado.loc[0, "email"])


def test_categoria_variante():
    categorias = {
        "Senha": ["senha", "password"]
    }

    df = pd.DataFrame({
        "categoria": ["PASSWORD"]
    })

    resultado = mapear_categorias(df, categorias)

    assert resultado.loc[0, "categoria"] == "Senha"


def test_categoria_ja_padronizada():
    categorias = {
        "Senha": ["senha", "password"]
    }

    df = pd.DataFrame({
        "categoria": ["Senha"]
    })

    resultado = mapear_categorias(df, categorias)

    assert resultado.loc[0, "categoria"] == "Senha"


def test_data_invalida_nao_quebra_programa():
    df = pd.DataFrame({
        "data": ["banana"]
    })

    resultado = padronizar_datas(df)

    assert pd.isna(resultado.loc[0, "data"])


def test_remover_protocolo_duplicado():
    df = pd.DataFrame({
        "protocolo": ["SUP-001", "SUP-001", "SUP-002"]
    })

    resultado = remover_duplicados(df)

    assert len(resultado) == 2


def test_protocolos_ausentes_nao_sao_removidos():
    df = pd.DataFrame({
        "protocolo": [pd.NA, pd.NA, "SUP-001"]
    })

    resultado = remover_duplicados(df)

    assert len(resultado) == 3

def test_data_invalida_nao_interrompe_outras_datas():
    df = pd.DataFrame({
        "data": [
            "2026-08-01",
            "data-invalida",
            "2026-08-03"
        ]
    })

    resultado = padronizar_datas(df)

    assert pd.notna(resultado.loc[0, "data"])
    assert pd.isna(resultado.loc[1, "data"])
    assert pd.notna(resultado.loc[2, "data"])  

def test_padronizar_formatos_de_data():
    df = pd.DataFrame({
        "data": [
            "2026-07-02",
            "03-07-2026",
            "2026/07/04",
            "05/07/2026"
        ]
    })

    resultado = padronizar_datas(df)

    assert resultado.loc[0, "data"].strftime("%Y-%m-%d") == "2026-07-02"
    assert resultado.loc[1, "data"].strftime("%Y-%m-%d") == "2026-07-03"
    assert resultado.loc[2, "data"].strftime("%Y-%m-%d") == "2026-07-04"
    assert resultado.loc[3, "data"].strftime("%Y-%m-%d") == "2026-07-05"      