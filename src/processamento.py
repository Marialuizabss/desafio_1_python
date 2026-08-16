# Módulo que normaliza e padroniza os dados


import pandas as pd
import logging


logger = logging.getLogger(__name__)


def remover_vazios(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove espaços vazios desnecessários das colunas de texto.
    """

    colunas = df.select_dtypes(include="object").columns
    for coluna in colunas:
        df[coluna] = df[coluna].str.strip()

    return df


def remover_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove linhas duplicadas com base no protocolo.
    Mantém a primeira ocorrência e remove as demais.
    """

    duplicados = df[df.duplicated(subset="protocolo", keep="first")]
    if not duplicados.empty:
        for protocolo in duplicados["protocolo"]:
            logger.warning(f"Protocolo duplicado removido: {protocolo}")

    df = df.drop_duplicates(subset="protocolo", keep="first")
    return df


def mapear_categorias(df: pd.DataFrame, categorias: dict) -> pd.DataFrame:
    """
    Mapeia variantes de categoria para o nome original definido em categorias.json.
    """
    categorias_possiveis = {
        variante: original
        for original, variantes in categorias.items()
        for variante in variantes
    }

    df["categoria"] = df["categoria"].str.lower().map(categorias_possiveis)
    return df


def padronizar_textos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza os textos das colunas Categoria e Status como Upper,
    Descrição como Capitalize e Email como Lower.
    """
    df["categoria"] = df["categoria"].str.upper()
    df["status"] = df["status"].str.upper()
    df["descricao"] = df["descricao"].str.capitalize()
    df["email"] = df["email"].str.lower()
    return df


def padronizar_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza as datas no formato yyyy-mm-dd.
    """

    df["data"] = pd.to_datetime(df["data"], format="mixed", dayfirst=True)
    return df


def tratar_dados(df: pd.DataFrame, categorias: dict) -> pd.DataFrame:
    """
    Executa as etapas de tratamento de dados na ordem correta.
    """

    df = remover_vazios(df)
    df = mapear_categorias(df, categorias)
    df = padronizar_textos(df)
    df = padronizar_datas(df)
    df = remover_duplicados(df)
    return df
