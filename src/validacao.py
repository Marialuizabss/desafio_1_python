import re
import pandas as pd


def validar_campos_obrigatorios(registro: dict) -> list:
    """
    Verifica se os campos obrigatórios estão preenchidos.
    Retorna uma lista com os motivos de invalidação.
    """

    erros = []

    campos_obrigatorios = [
        "protocolo",
        "data",
        "email",
        "categoria",
        "status",
        "tempo_minutos",
        "descricao"
    ]

    for campo in campos_obrigatorios:
        valor = registro.get(campo)

        if valor is None or pd.isna(valor) or str(valor).strip() == "":
            erros.append(f'Campo obrigatório "{campo}" não preenchido')

    return erros

def validar_email(email: str) -> bool:
    """
    Verifica se o e-mail possui um formato válido.
    """

    if not isinstance(email, str):
        return False

    padrao = r'[^@\s]+@[^@\s]+\.[^@\s]+'
    
    return bool(re.fullmatch(padrao, email))


def validar_tempo(tempo) -> bool:
    """
    Verifica se o tempo de atendimento é numérico e não negativo.
    """

    try:
        tempo = float(tempo)
        return tempo >= 0
    except (TypeError, ValueError):
        return False


def validar_registro(registro: dict) -> dict:
    erros = []

    erros.extend(validar_campos_obrigatorios(registro))

    email = registro.get("email")
    if email is not None and not pd.isna(email) and str(email).strip() != "":
        if not validar_email(email):
            erros.append("E-mail inválido")

    tempo = registro.get("tempo_minutos")
    if tempo is not None and not pd.isna(tempo) and str(tempo).strip() != "":
        if not validar_tempo(tempo):
            erros.append("Tempo de atendimento inválido")

    return {
        "valido": len(erros) == 0,
        "erros": erros
    }