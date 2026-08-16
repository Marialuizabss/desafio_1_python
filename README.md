# Sistema de Análise de Atendimentos de Suporte Técnico

DESAFIO 01 FIC_DEV MÓDULO PYTHON - TURMA NOTURNA
Projeto desenvolvido para realizar a leitura, validação, processamento, análise e geração de relatórios a partir de dados de atendimentos de suporte técnico.

## Integrantes

- Maria Luiza Batista de Souza
- Gabriele Pereira da Silva

## Funcionalidades

O sistema realiza:

- leitura de arquivos CSV, JSON e TXT;
- tratamento e padronização dos dados;
- remoção de registros com protocolo duplicado;
- validação de campos obrigatórios;
- validação de e-mails utilizando expressões regulares;
- validação do tempo de atendimento;
- extração de protocolos e telefones do arquivo de observações utilizando expressões regulares;
- separação entre registros válidos e inválidos;
- cálculo de indicadores dos atendimentos;
- geração de gráficos;
- exportação dos dados processados para CSV;
- exportação do resumo das análises para JSON;
- registro de avisos e erros em arquivo de log;
- testes automatizados utilizando pytest.

## Estrutura do projeto

```text
desafio_1_python/
├── data/
│   ├── atendimentos.csv
│   ├── categorias.json
│   ├── config.json
│   └── observacoes.txt
├── graficos/
│   ├── atendimentos_por_categoria.png
│   ├── atendimentos_por_status.png
│   └── distribuicao_tempo_atendimento.png
├── logs/
│   └── erros.log
├── output/
│   ├── atendimentos_processados.csv
│   └── resumo.json
├── src/
│   ├── __init__.py
│   ├── analise.py
│   ├── leitura.py
│   ├── main.py
│   ├── processamento.py
│   ├── relatorios.py
│   └── validacao.py
├── tests/
│   ├── test_analise.py
│   ├── test_processamento.py
│   ├── test_relatorios.py
│   └── test_validacao.py
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.12 ou superior
- pandas
- numpy
- matplotlib
- pytest

As dependências utilizadas pelo projeto estão disponíveis no arquivo `requirements.txt`.

## Criação do ambiente virtual

Para criar um ambiente virtual:

```bash
python -m venv .venv
```

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## Instalação das dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

## Execução

Na raiz do projeto, execute:

```bash
python -m src.main
```

O programa realiza o processamento dos dados e gera os arquivos de saída e os gráficos.

## Validação dos dados

Os registros são verificados antes das análises.

São considerados inválidos registros que apresentem problemas como:

- campos obrigatórios não preenchidos;
- e-mail em formato inválido;
- tempo de atendimento negativo ou não numérico.

Registros inválidos não são utilizados no cálculo dos indicadores.

Os motivos de rejeição são registrados no arquivo:

```text
logs/erros.log
```

Protocolos duplicados também são identificados durante o processamento. A primeira ocorrência é mantida e as demais são removidas.

## Processamento dos dados

Durante o processamento são realizadas operações como:

- remoção de espaços desnecessários;
- padronização de valores ausentes;
- padronização das categorias;
- conversão de status para letras maiúsculas;
- conversão de e-mails para letras minúsculas;
- padronização das descrições;
- conversão e padronização das datas;
- remoção de protocolos duplicados.

## Análises

O sistema calcula:

- quantidade total de atendimentos válidos;
- quantidade de atendimentos por categoria;
- quantidade de atendimentos por status;
- tempo médio de atendimento;
- categoria ou categorias mais frequentes;
- percentual de registros inválidos.

## Expressões regulares

Expressões regulares são utilizadas para:

- validar o formato dos endereços de e-mail;
- extrair protocolos do arquivo `observacoes.txt`;
- extrair números de telefone do arquivo `observacoes.txt`.

## Gráficos

São gerados três gráficos:

1. atendimentos por categoria;
2. atendimentos por status;
3. distribuição dos tempos de atendimento.

Na análise da distribuição dos tempos, valores extremos são identificados pelo método do intervalo interquartil (IQR). Dessa forma, valores discrepantes podem ser destacados sem prejudicar a visualização da distribuição dos demais atendimentos.

Os gráficos são armazenados no diretório `graficos/`.

## Arquivos de saída

Após a execução são gerados:

```text
output/atendimentos_processados.csv
output/resumo.json
```

O CSV contém os registros válidos após o tratamento e a validação.

O JSON apresenta um resumo dos principais indicadores calculados pelo sistema.

## Testes

Os testes automatizados foram implementados utilizando `pytest`.

Para executá-los:

```bash
python -m pytest
```

Os testes verificam funções de processamento, validação, análise e geração dos relatórios.

## Uso de ferramentas de IA

Ferramentas de inteligência artificial foram utilizadas como apoio durante o desenvolvimento do projeto, principalmente para esclarecimento de dúvidas, revisão de código, identificação de possíveis casos de teste e auxílio na documentação.

As sugestões obtidas foram analisadas e adaptadas antes de serem incorporadas ao projeto. A implementação, os testes e a validação do funcionamento do sistema foram realizados pela equipe.