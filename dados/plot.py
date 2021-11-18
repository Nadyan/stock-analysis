import plotly.graph_objects as go

def plotaCandleStick(dados, sigla):
    trace1 = {
        'x': dados.index,
        'open': dados.Open,
        'close': dados.Close,
        'high': dados.High,
        'low': dados.Low,
        'type': 'candlestick',
        'name': sigla,
        'showlegend': False
    }
    
    data = [trace1]
    layout = go.Layout()
    
    fig = go.Figure(data=data, layout=layout)
    fig.show()