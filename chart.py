
import plotly.graph_objects as go
import av
df=av.Sdata

candlestick = go.Candlestick(
    x=df.index,
    open=df['1. open'],
    high=df['2. high'],
    low=df['3. low'],
    close=df['4. close']
)


fig = go.Figure(data=[candlestick])
fig.update_layout(
    title='MRIN',
    yaxis_title='$/share')
fig.show()