import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like # to make pandas_datareader cooperate
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([
    html.H1('Crypto Ticker'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Snap', 'value': 'SNAP'},
            {'label': 'Facebook', 'value': 'FB'},
            {'label': 'Twitter', 'value': 'TWTR'},
            {'label': 'Salesforce', 'value': 'CRM'},
        ],
        value='SNAP'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(selected_dropdown_value, data_source='robinhood')
    return {
        'data': [{
            'x': df.index,
            'y': df.close_price
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
