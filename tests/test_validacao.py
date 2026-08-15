import numpy as np

from src.validacao import (
    validar_campos_obrigatorios,
    validar_email,
    validar_tempo,
    validar_registro
)


def test_campos_obrigatorios_preenchidos():
    registro = {
        "protocolo": "SUP-2026-0001",
        "data": "2026-07-02",
        "email": "aluno@example.com",
        "categoria": "Senha",
        "status": "aberto",
        "tempo_minutos": 20,
        "descricao": "Problema com senha"
    }

    erros = validar_campos_obrigatorios(registro)

    assert erros == []

def test_campos_obrigatorios():
    registro = {
        "protocolo": "SUP-2026-0001",
        "data": "",
        "email": "aluno@example.com",
        "categoria": "Senha",
        "status": "aberto",
        "tempo_minutos": 20,
        "descricao": "Problema com senha"
    }

    erros = validar_campos_obrigatorios(registro)

    assert 'Campo obrigatório "data" não preenchido' in erros

def test_email_valido():
    assert validar_email("aluno@example.com") is True


def test_email_outro_dominio():
    assert validar_email("maria@gmail.com") is True


def test_email_com_br():
    assert validar_email("maria@empresa.com.br") is True


def test_email_sem_arroba():
    assert validar_email("mariagmail.com") is False


def test_email_sem_extensao():
    assert validar_email("maria@gmail") is False


def test_email_vazio():
    assert validar_email("") is False   

def test_tempo_valido():
    assert validar_tempo(30) is True


def test_tempo_decimal():
    assert validar_tempo(15.5) is True


def test_tempo_como_texto():
    assert validar_tempo("20") is True


def test_tempo_negativo():
    assert validar_tempo(-10) is False


def test_tempo_nao_numerico():
    assert validar_tempo("abc") is False


def test_tempo_nulo():
    assert validar_tempo(None) is False    

def test_campo_obrigatorio_nan():
    registro = {
        "protocolo": "SUP-2026-0001",
        "data": np.nan,
        "email": "aluno@example.com",
        "categoria": "Senha",
        "status": "aberto",
        "tempo_minutos": 20,
        "descricao": "Problema com senha"
    }

    erros = validar_campos_obrigatorios(registro)

    assert 'Campo obrigatório "data" não preenchido' in erros
    
def test_registro_valido():
    registro = {
        "protocolo": "SUP-2026-0001",
        "data": "2026-07-02",
        "email": "aluno@gmail.com",
        "categoria": "Senha",
        "status": "aberto",
        "tempo_minutos": 20,
        "descricao": "Problema com senha"
    }

    resultado = validar_registro(registro)

    assert resultado["valido"] is True
    assert resultado["erros"] == []


def test_registro_invalido():
    registro = {
        "protocolo": "SUP-2026-0001",
        "data": "",
        "email": "email-invalido",
        "categoria": "Senha",
        "status": "aberto",
        "tempo_minutos": -5,
        "descricao": "Problema com senha"
    }

    resultado = validar_registro(registro)

    assert resultado["valido"] is False
    assert 'Campo obrigatório "data" não preenchido' in resultado["erros"]
    assert "E-mail inválido" in resultado["erros"]
    assert "Tempo de atendimento inválido" in resultado["erros"]    