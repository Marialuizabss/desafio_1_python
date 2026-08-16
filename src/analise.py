import pandas as pd
import numpy as np


def quantidade_total_atendimentos(df: pd.DataFrame) -> int:
    """
    Retorna a quantidade total de atendimentos.
    """
    return len(df)

def quantidade_por_categoria(df: pd.DataFrame) -> dict:
    """
    Retorna a quantidade de atendimentos por categoria.
    """
    return df["categoria"].value_counts().to_dict()    

def quantidade_por_status(df: pd.DataFrame) -> dict:
    """
    Retorna a quantidade de atendimentos por status.
    """
    return df["status"].value_counts().to_dict()

def tempo_medio_atendimento(df: pd.DataFrame) -> float:
    """
    Retorna o tempo médio de atendimento.
    Valores não numéricos são ignorados no cálculo.
    """

    tempos = pd.to_numeric(
        df["tempo_minutos"],
        errors="coerce"
    )

    tempos = tempos.dropna()

    if tempos.empty:
        return 0.0

    return float(np.mean(tempos.to_numpy()))

def categoria_mais_frequente(df: pd.DataFrame) -> list:
    """
    Retorna a(s) categoria(s) com maior quantidade de atendimentos.
    """

    contagem = df["categoria"].value_counts()

    if contagem.empty:
        return []

    maior_quantidade = contagem.max()

    return contagem[contagem == maior_quantidade].index.tolist()

def percentual_invalidos(total_registros: int, total_invalidos: int) -> float:
    """
    Retorna o percentual de registros inválidos ou incompletos.
    """

    if total_registros == 0:
        return 0.0

    return (total_invalidos / total_registros) * 100    
