from src.relatorios import (
    grafico_por_categoria,
    grafico_por_status
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