# Import libraries

import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__)
server = app.server

# Data
d = {'adr': [515.05,539.07,312.61,220.43,187.14,232.65,139.91,178.06,175.16,143.17,126.36,122.66,153.26,135.94], 'rooms': [9840,1774,16950,6940,226015,31000,154708,14719,61844,149130,327690,24755,61624,75069], 'occupancy': [64.9,49.3,75.9,70.9,68.6,69.2,66.7,66.1,69.5,67.5,68.6,66.4,75.1,74.0], 'brand': ['Waldorf Astoria Hotels & Resorts', 'LXR Hotels & Resorts', 'Conrad Hotels & Resorts', 'Canopy by Hilton', 'Hilton Hotels & Resorts', 'Curio Collection by Hilton', 'DoubleTree by Hilton', 'Tapestry Collection by Hilton', 'Embassy Suites by Hilton', 'Hilton Garden Inn', 'Hampton by Hilton', 'Tru by Hilton', 'Homewood Suites by Hilton', 'Home2 Suites by Hilton']}
df = pd.DataFrame(data=d)

# Define dashboard layout
app.layout = html.Div(children=[
    html.H1(children='Hilton Worldwide Holdings: Q4 2023 Earnings Results', style={'text-align': 'left'}),
    html.H3(children='Data sourced from:', style={'text-align': 'left'}),
    html.H4(children='https://ir.hilton.com/~/media/Files/H/Hilton-Worldwide-IR-V3/quarterly-results/2024/q4-2023-earnings-release.pdf', style={'text-align': 'left'}),
    
    html.Div([
        html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'adr (x) - occupancy (y) - rooms (z)', 'value': 'graph1'},
                {'label': 'rooms (x) - occupancy (y) - adr (z)', 'value': 'graph2'},
                {'label': 'adr (x) - rooms (y) - occupancy (z)', 'value': 'graph3'},
                    ],
            value='graph1',
            style={"width": "60%"}),
        
    html.Div(dcc.Graph(id='graph')),        
        ]),

])

# Define callback
@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def select_graph(value):
    if value == 'graph1':
        fig = px.scatter(df, x="adr", y="occupancy", color="brand", size="rooms", size_max=45, log_x=True)
        return fig
    elif value == 'graph2':
        fig1 = px.scatter(df, x="rooms", y="occupancy", color="brand", size="adr", size_max=45, log_x=True)
        return fig1
    else:
        fig2 = px.scatter(df, x="adr", y="rooms", color="brand", size="occupancy", size_max=45, log_x=True)
        return fig2        
    
if __name__ == '__main__':
    app.run_server(debug=True)

# References:

# Deploying a Dash Application on Render: https://github.com/thusharabandara/dash-app-render-deployment
# Hilton Worldwide Holdings (Q4 2023 Earnings): https://ir.hilton.com/~/media/Files/H/Hilton-Worldwide-IR-V3/quarterly-results/2024/q4-2023-earnings-release.pdf
# Stack Overflow - Connecting graphs with dropdown (Plotly Dash) - https://stackoverflow.com/questions/67401292/connecting-graphs-with-dropdown-plotly-dash
