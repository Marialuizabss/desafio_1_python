# Módulo que normaliza e padroniza os dados


import pandas as pd
import logging


logger = logging.getLogger(__name__)


def remover_espacos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove espaços vazios desnecessários das colunas de texto.
    """

    colunas = df.select_dtypes(include=["object", "string"]).columns
    
    for coluna in colunas:
        df[coluna] = df[coluna].str.strip()

    return df

def tratar_valores_ausentes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza valores ausentes para que possam ser identificados
    durante a validação.
    """
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    return df

def remover_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove registros com protocolo duplicado.
    Protocolos ausentes não são considerados duplicados.
    Mantém a primeira ocorrência.
    """

    possui_protocolo = (
        df["protocolo"].notna()
        & (df["protocolo"].astype(str).str.strip() != "")
    )

    duplicados = (
        possui_protocolo
        & df.duplicated(subset="protocolo", keep="first")
    )

    if duplicados.any():
        for protocolo in df.loc[duplicados, "protocolo"]:
            logger.warning(f"Protocolo duplicado removido: {protocolo}")

    df = df.loc[~duplicados].copy()

    return df


def mapear_categorias(df: pd.DataFrame, categorias: dict) -> pd.DataFrame:
    """
    Padroniza as categorias usando os nomes definidos em categorias.json.
    """

    categorias_possiveis = {}

    for original, variantes in categorias.items():
        categorias_possiveis[original.lower()] = original

        for variante in variantes:
            categorias_possiveis[variante.lower()] = original

    df["categoria"] = (
        df["categoria"]
        .str.strip()
        .str.lower()
        .map(categorias_possiveis)
    )

    return df


def padronizar_textos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza Status como Upper, Descrição como Capitalize
    e Email como Lower.
    """
    df["status"] = df["status"].str.upper()
    df["descricao"] = df["descricao"].str.capitalize()
    df["email"] = df["email"].str.lower()
    return df


def padronizar_datas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza diferentes formatos de data para datetime.
    Datas inválidas são convertidas para NaT.
    """

    def converter_data(valor):
        if pd.isna(valor):
            return pd.NaT

        valor = str(valor).strip()

        formatos = [
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%Y/%m/%d",
            "%d/%m/%Y"
        ]

        for formato in formatos:
            try:
                return pd.to_datetime(valor, format=formato)
            except ValueError:
                continue

        return pd.NaT

    df["data"] = df["data"].apply(converter_data)

    return df


def tratar_dados(df: pd.DataFrame, categorias: dict) -> pd.DataFrame:
    """
    Executa as etapas de tratamento de dados na ordem correta.
    """

    df = remover_espacos(df)
    df = tratar_valores_ausentes(df)
    df = mapear_categorias(df, categorias)
    df = padronizar_textos(df)
    df = padronizar_datas(df)
    df = remover_duplicados(df)

    return df