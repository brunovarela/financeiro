# ETF Performance Analysis

Este projeto utiliza a biblioteca `yfinance` para coletar dados históricos de ETFs e calcular várias métricas de performance, como variação percentual diária, semanal, mensal, anual, dividend yield, entre outras. As tabelas resultantes são exportadas para um arquivo Excel com formatação personalizada, incluindo colorações alternadas nas linhas e cabeçalhos estilizados.

A (etfs_list) é criada pelo usuário com as ações que o mesmo deseja monitorar.

## Funcionalidades

- Coleta dados históricos de ETFs utilizando a API do Yahoo Finance (`yfinance`).
- Calcula variações percentuais de preços em diferentes períodos: 1 dia, 7 dias, 30 dias, ano atual e últimos 12 meses.
- Calcula o Dividend Yield dos ETFs.
- Exporta os resultados para um arquivo Excel com formatação estilizada, incluindo cores para cabeçalhos e alternância de cores nas linhas.
- Automatiza a criação de diretórios, garantindo que o arquivo seja salvo corretamente.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `pandas`
  - `openpyxl`
  - `yfinance`
  - `datetime`
  - `os`

### Instalação de dependências

Você pode instalar as dependências usando o seguinte comando:

```bash
pip install pandas openpyxl yfinance
