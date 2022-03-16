import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['Cases - cumulative total', 'Deaths - cumulative total']

mycolumn='Cases - cumulative total'
myheading1 = f"{mycolumn}!"
mygraphtitle = 'COVID Cases by Country'
mycolorscale = 'ylorrd' # Note: The error message will list possible color scales.
mycolorbartitle = "Human Count"
tabtitle = 'COVID 19'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/minul-islam/301-old-mcdonald'

########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/WHO-COVID-19-global-table-data.csv')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Country'})

fig = go.Figure(data=go.Choropleth(
    locations=df['Country'], # Spatial coordinates
    z = df[mycolumn].astype(float), # Data to be color-coded
    locationmode = 'country names', # set of locations match entries in `locations`
    colorscale = mycolorscale,
    colorbar_title = mycolorbartitle,
))

fig.update_layout(
    title_text = mygraphtitle,
    width=1200,
    height=800
)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
