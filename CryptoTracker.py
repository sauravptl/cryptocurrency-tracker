# install liberaries before we use
# pip install shrimpy-python
# pip install pandas
# pip install plotly
# import the libraries
import shrimpy
import plotly.graph_objects as go

# Add your public and secret keys here
public_key = 'QZ9v6g04lHKeQIXEIPdvE8fv2Oy1232lMMZF8jajvLu7JpZYZ0aMesYlkaQ3je0Q'
secret_key = 'IJc2kKgwqcT26jNy0DPt0OZUZvmqKG28ph8fq3qoOy56Dv4W6hg3ZKGOKUuvM1Zu'

# create client using shrimpy
client = shrimpy.ShrimpyApiClient(public_key, secret_key)

# get the data for showing candles
candles = client.get_candles(
    'binance',  # exchange
    'XLM',      # base_trading_symbol
    'BTC',      # quote_trading_symbol
    '15m',      # interval
)

# Create lists to store data
dates = []
open_data = []
high_data = []
low_data = []
close_data = []

# convert shrimpy candlesticks to plotly graph
for candle in candles:
    dates.append(candle['time'])
    open_data.append(candle['open'])
    high_data.append(candle['high'])
    low_data.append(candle['low'])
    close_data.append(candle['close'])

# print the figure
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_data, high=high_data,
                                     low=low_data, close=close_data)])

# Add titles
fig.update_layout(
    title='Bitcoin Live Share Price',
    yaxis_title='Bitcoin Price')

# update time wise candles
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="minute", stepmode="backward"),
            dict(count=5, label="5m", step="minute", stepmode="backward"),
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=4, label="4h", step="hour", stepmode="backward"),
            dict(count=0, label="all", step="all", stepmode="backward")
        ])
    )
)

# show graph
fig.show()
