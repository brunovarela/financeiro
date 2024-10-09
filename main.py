import yfinance as yf
import datetime

# Defina o ticker da ação, data de início e data de fim
ticker = "BBDC4.SA"  # Exemplo: Apple
start_date = "2024-08-12"
end_date = "2024-09-05"

# Baixe os dados históricos
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Exiba os valores de fechamento
print(stock_data['Close'].iloc[0])

stock_data['Ações'][0] = None

print(stock_data['Ações'].iloc[0])