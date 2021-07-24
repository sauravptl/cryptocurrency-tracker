from pandas.io.formats import style
import requests
import pandas as pd
import mplfinance as mpf


def crypto_candles(start_time, base_currency, vs_currency, interval):
    url = f'https://dev-api.shrimpy.io/v1/exchanes/binance/candles'
    payload = {'interval': interval, 'baseTradingSymbol': base_currency,
               'quotetradingSymbol': vs_currency, 'startTime': start_time}
    response = requests.get(url, params=payload)
    data = response.json()

    open_p, close_p, high_p, low_p, time_p = [], [], [], [], []

    print(data)
    for candle in data:
        time_p.append(candle['time'])
        open_p.append(candle['open'])
        high_p.append(candle['high'])
        low_p.append(candle['low'])
        close_p.append(candle['close'])

    raw_data = {
        'Date': pd.DatetimeIndex(time_p),
        'Open': open_p,
        'High': high_p,
        'Low': low_p,
        'Close': close_p
    }

    df = pd.DataFrame(raw_data).set_index('Date')
    print(df)

    mpf.plot(df,type='candle',style='charles',title=base_currency,ylable=f'Price in {vs_currency}')
    mpf.show()

    return df
crypto_candles(start_time='2021-01-01',base_currency='BTC',vs_currency='EUR',interval='1h')
