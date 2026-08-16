import pandas as pd

from src.analise import (
    quantidade_total_atendimentos,
    quantidade_por_categoria,
    quantidade_por_status,
    tempo_medio_atendimento,
    categoria_mais_frequente,
    percentual_invalidos
)

def test_quantidade_total_atendimentos():
    df = pd.DataFrame({
        "protocolo": ["SUP-001", "SUP-002", "SUP-003"]
    })

    resultado = quantidade_total_atendimentos(df)

    assert resultado == 3

def test_quantidade_por_categoria():
    df = pd.DataFrame({
        "categoria": [
            "Senha",
            "Senha",
            "Acesso ao AVA",
            "Configuração do Python",
            "Senha"
        ]
    })

    resultado = quantidade_por_categoria(df)

    assert resultado == {
        "Senha": 3,
        "Acesso ao AVA": 1,
        "Configuração do Python": 1
    }    

def test_quantidade_por_status():
    df = pd.DataFrame({
        "status": [
            "ABERTO",
            "RESOLVIDO",
            "ABERTO",
            "EM ANDAMENTO",
            "RESOLVIDO"
        ]
    })

    resultado = quantidade_por_status(df)

    assert resultado == {
        "ABERTO": 2,
        "RESOLVIDO": 2,
        "EM ANDAMENTO": 1
    }    

def test_tempo_medio_atendimento():
    df = pd.DataFrame({
        "tempo_minutos": [10, 20, 30]
    })

    resultado = tempo_medio_atendimento(df)

    assert resultado == 20    

def test_categoria_mais_frequente():
    df = pd.DataFrame({
        "categoria": [
            "Senha",
            "Acesso ao AVA",
            "Senha",
            "Configuração do Python",
            "Senha"
        ]
    })

    resultado = categoria_mais_frequente(df)

    assert resultado == ["Senha"]

def test_percentual_invalidos():
    resultado = percentual_invalidos(100, 15)

    assert resultado == 15.0


def test_percentual_invalidos_sem_registros():
    resultado = percentual_invalidos(0, 0)

    assert resultado == 0.0    

def test_categoria_mais_frequente_com_empate():
    df = pd.DataFrame({
        "categoria": [
            "Senha",
            "Senha",
            "Acesso ao AVA",
            "Acesso ao AVA",
            "Configuração do Python"
        ]
    })

    resultado = categoria_mais_frequente(df)

    assert set(resultado) == {"Senha", "Acesso ao AVA"}    