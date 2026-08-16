# Módulo responsável pela leitura dos arquivos 


import json
import logging
from pathlib import Path
import pandas as pd


logger = logging.getLogger(__name__)


def ler_json (caminho: Path) -> dict:
    '''
    Lê um arquivo no formato JSON e trata erros de leitura.
    Retorna o conteúdo como um dicionário.
    '''

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
            
    except FileNotFoundError:
        logger.error(f'Arquivo "{caminho}" não encontrado')
        raise
    
    except UnicodeDecodeError:
        logger.error(f'Erro de enconding para o arquivo "{caminho}"')
        raise
            
    except json.JSONDecodeError as e:
        logger.error(f'Arquivo "{caminho}" com formatação inválida: {e}')
        raise
    
    if not dados_json:
        logger.warning(f'O arquivo "{caminho}" está vazio')
    
    return dados_json


def ler_txt (caminho: Path) -> str:
    '''
    Lê um arquivo no formato TXT e trata erros de leitura..
    Retorna o conteúdo bruto como uma string.
    '''
    
    try:
        dados_txt = caminho.read_text(encoding='utf-8')
        
    except FileNotFoundError:
        logger.error(f'Arquivo "{caminho}" não encontrado')
        raise
    
    except UnicodeDecodeError:
        logger.error(f'Erro de enconding para o arquivo "{caminho}"')
        raise
    
    if not dados_txt.strip():
        logger.warning(f'Arquivo "{caminho}" está vazio')
    
    return dados_txt


def ler_csv (caminho: Path, separador: str) -> pd.DataFrame:
    '''
    Lê um arquivo no formato CSV e trata erros de leitura e de interpretação.
    Retorna os dados como um DataFrame do pandas.
    '''
    
    try:
        dados_csv = pd.read_csv(caminho, sep=separador, encoding='utf-8')
            
    except FileNotFoundError:
        logger.error(f'Arquivo "{caminho}" não encontrado')
        raise
            
    except UnicodeDecodeError:
        logger.error(f'Erro de enconding para o arquivo "{caminho}"')
        raise
    
    except pd.errors.ParserError:
        logger.error(f'Erro de interpretação para o arquivo "{caminho}"')
        raise
    
    except pd.errors.EmptyDataError:
        logger.error(f'O arquivo "{caminho}" está vazio')
        raise
    
    return dados_csv

        