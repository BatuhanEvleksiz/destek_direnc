import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Destek ve direnç seviyelerini hesapla
def calculate_support_resistance(data, window=5):
    data['Support'] = data['Low'].rolling(window=window, center=True).min()
    data['Resistance'] = data['High'].rolling(window=window, center=True).max()
    return data

# Hisse senedi verilerini çek ve grafik çiz
def plot_stock_data(ticker, period):
    # Hisse senedi verilerini çek
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    # Destek ve direnç seviyelerini hesapla
    data = calculate_support_resistance(data)
    
    # Grafik çiz
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Kapanış Fiyatı', color='blue')
    plt.plot(data['Support'], label='Destek Seviyesi', color='green', linestyle='--')
    plt.plot(data['Resistance'], label='Direnç Seviyesi', color='red', linestyle='--')
    
    plt.title(f'{ticker} Hisse Senedi Fiyatları ve Destek/Direnç Seviyeleri ({period})')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat')
    plt.legend()
    plt.grid()
    plt.show()

# Kullanıcıdan girdi al
ticker = input("Hisse senedi sembolünü girin (örneğin TSLA): ").upper()
period = input("Zaman aralığını seçin (örneğin 1mo, 3mo, 6mo, 1y): ")

# Grafiği çiz
plot_stock_data(ticker, period)