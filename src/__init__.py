from src.leitura import ler_json, ler_csv, ler_txt
from src.validacao import validar_campos_obrigatorios, validar_email, validar_registro, validar_tempo, extrair_protocolos, extrair_telefones
from src.processamento import remover_duplicados, remover_espacos, tratar_dados, tratar_valores_ausentes, mapear_categorias, padronizar_datas, padronizar_textos
from src.analise import quantidade_total_atendimentos, quantidade_por_categoria, quantidade_por_status, tempo_medio_atendimento, categoria_mais_frequente, percentual_invalidos
from src.relatorios import grafico_por_categoria, grafico_distribuicao_tempo, grafico_por_status, exportar_csv, exportar_resumo_json

__version__ = '1.0.0'