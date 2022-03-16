import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['Cases - cumulative total', 'Deaths - cumulative total',
                   'Cases - newly reported in last 7 days','Deaths - newly reported in last 7 days']

tabtitle = 'COVID 19'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/minul-islam/301-old-mcdonald'

########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/WHO-COVID-19-global-table-data.csv')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Country'})

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('COVID-19 Cases & Death as of 15 Mar 2022'),
    html.Div([
        html.Div([
                html.H6('Select a variable for analysis:'),
                dcc.Dropdown(
                    id='options-drop',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value='Cases - cumulative total'
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)



### define a function to create the chart 
@app.callback(Output('figure-1', 'figure'),
             [Input('options-drop', 'value')])

def create_chart(var1): 
    mygraphtitle = f'COVID {var1} by Country'
    mycolorscale = 'ylorrd' # Note: The error message will list possible color scales.
    mycolorbartitle = "Number of Person"

    fig = go.Figure(data=go.Choropleth(
        locations=df['Country'], # Spatial coordinates
        z = df[var1].astype(float), # Data to be color-coded
        locationmode = 'country names', # set of locations match entries in `locations`
        colorscale = mycolorscale,
        colorbar_title = mycolorbartitle,
    ))

    fig.update_layout(
        title_text = mygraphtitle,
        width=1200,
        height=800
    )

    return fig


############ Deploy
if __name__ == '__main__':
    app.run_server()
