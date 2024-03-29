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
    html.H1(children='Hilton Worldwide Holdings: ADR, Occupancy and Rooms By Hotel Brand', style={'text-align': 'left'}),
    html.H4(children='', style={'text-align': 'left'}),
    html.H4(children='This interactive bubble chart visualisation displays ADR (average daily rate), occupancy, and number of rooms by hotel brand for Hilton Worldwide Holdings based on Q4 2023 earnings data.', style={'text-align': 'left'}),
    html.H4(children='', style={'text-align': 'left'}),
    html.H4(children='Data sourced from:', style={'text-align': 'left'}),
    html.A(children='Hilton Worldwide Holdings: Q4 2023 Earnings Results', href='https://ir.hilton.com/~/media/Files/H/Hilton-Worldwide-IR-V3/quarterly-results/2024/q4-2023-earnings-release.pdf', style={'text-align': 'left'}),
    html.H4(children='', style={'text-align': 'left'}),
    
    html.Div([
        html.Label(['X'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='x',
            options=[
                {'label': 'adr', 'value': 'adr'},
                {'label': 'occupancy', 'value': 'occupancy'},
                {'label': 'rooms', 'value': 'rooms'},
                    ],
            value='adr',
            style={"width": "60%"}),
        html.Label(['Y'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='y',
            options=[
                {'label': 'adr', 'value': 'adr'},
                {'label': 'occupancy', 'value': 'occupancy'},
                {'label': 'rooms', 'value': 'rooms'},
                    ],
            value='adr',
            style={"width": "60%"}),
        html.Label(['Z (bubble size)'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='z',
            options=[
                {'label': 'adr', 'value': 'adr'},
                {'label': 'occupancy', 'value': 'occupancy'},
                {'label': 'rooms', 'value': 'rooms'},
                    ],
            value='adr',
            style={"width": "60%"}),
        
    html.Div(dcc.Graph(id='graph')),        
        ]),

])

# Define callback
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('x', 'value'),
     dash.dependencies.Input('y', 'value'),
     dash.dependencies.Input('z', 'value')]
)
def select_graph(x, y, z):
        fig = px.scatter(df, x=x, y=y, color="brand", size=z, size_max=45, log_x=True)
        return fig        

if __name__ == '__main__':
    app.run_server(debug=True)

# References:

# Deploying a Dash Application on Render: https://github.com/thusharabandara/dash-app-render-deployment
# Hilton Worldwide Holdings (Q4 2023 Earnings): https://ir.hilton.com/~/media/Files/H/Hilton-Worldwide-IR-V3/quarterly-results/2024/q4-2023-earnings-release.pdf
# Plotly - Link to an external site in a new browser tab: https://community.plotly.com/t/link-to-an-external-site-in-a-new-browser-tab/7249/2
# Stack Overflow - Connecting graphs with dropdown (Plotly Dash) - https://stackoverflow.com/questions/67401292/connecting-graphs-with-dropdown-plotly-dash
