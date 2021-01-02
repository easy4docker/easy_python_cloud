import pandas as pd
import yfinance as yf

from datetime import date

def fetchTicker(tickers, period="10y"):
    yTickers = yf.Tickers(" ".join(tickers))
    dataFrame = pd.DataFrame()
    for tindex in range(len(tickers)):
        history = yTickers.tickers[tindex].history(period=period)
        filtered = history.filter(items=['Open', 'Close', 'High', 'Low', 'Volume'])
        filtered.reset_index(inplace=True, col_level=0)
        filtered.insert(0, "Ticker", yTickers.tickers[tindex].ticker, True)

        dataFrame = pd.concat([dataFrame, filtered])
    return dataFrame

def export(dataFrame):
    dataFrame.to_csv(path_or_buf="/var/_localAppData/_output/{0}.csv".format(date.today().strftime("%b-%d-%Y")), index=False)

def fetchWatchlist(fileName):
    dataFrame = pd.read_csv(fileName)
    return dataFrame["Symbol"].tolist()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    watchList = fetchWatchlist('data/500.csv')
    toExport = fetchTicker(watchList[0:25])
    export(toExport)
