# Import dependencies 
import seaborn as sns
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objs as go
from plotly.graph_objs import Layout
from plotly.offline import init_notebook_mode, iplot, plot
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc

# import data
df = pd.read_csv("data.csv")

# Make new dataframe
list = ['Christopher Nolan', 'Martin Scorsese', 'Steven Spielberg', 'Quentin Tarantino','Tim Burton','Kathryn Bigelow','James Cameron','Spike Lee','Greta Gerwig', 'David Fincher']
df_Directors = df[df.Director.isin(list)]
df_Directors['Release Year'] = df_Directors['Release Year'].astype(int)

# Define layout and elements
#stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # load the CSS stylesheet

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR, dbc_css]) # initialize the app
server = app.server
#app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

# Define layout and elements
min_date = df_Directors['Release Year'].min()  # get the minimum value of year in the dataset
max_date = df_Directors['Release Year'].max()  # maximum value of year

app.layout = dbc.Container([
    html.Br(),
    html.Br(),
    html.Div(children = [
        dcc.Markdown(
            '''# Cinemaniac ''', 
        ),
        dcc.Markdown(
            '''##### Welcome to Cinemaniac! Use the interactive graph below to dive into our database and uncover trends, statistics, and insights into 10 top directors in the film industry. Whether you're a movie buff, industry professional, or simply curious about cinema, Cinemaniac offers a dynamic app to enrich your movie experience. ''', 
            style = {'color': 'rgba(226,217,243,255)'},
        ),
    ], className = 'text-center' ),
    html.Br(),
    html.Br(),
    html.Div(children = [
        dcc.Markdown(
            '''##### To get started, choose the director(s) you want to analyze from the dropdown menu then use the range slider to select release date years. ''', 
            style = {'color': 'rgba(226,217,243,255)'},
        ),
    ], className = 'text-center' ),
    html.Div(children = [   # Dropdown 
        html.Label('Select Director'),
        dcc.Dropdown(
            options = [{'label':director, 'value':director} for director in df_Directors['Director'].unique()],  # Options are all directors in dataset
            value = [],   # Making the default value an empty list of directors 
            multi = True,    # Can select more than one country
            # options=[{‘label’: i, ‘value’: i} for i in df.SOR_NM.unique()]
            id = 'director_dropdown',  
            ),
    ], style = {'width':'50%', 'display':'inline-block'}, className = 'dbc'),
    html.Div(children = [   # Slider 
        html.Label('Select Release Date Range'),    # Label for slider 
        dcc.RangeSlider( 
            min = min_date,
            max = max_date,
            value = [min_date, max_date],   # Make default value the whole range of years in dataset
            step = 1,    # Can go up/down by 1 
            marks = None,   # I don't want marks
            id = 'range_slider',
            tooltip={"placement": "bottom", "always_visible": True},
            allowCross = False,     # Prevent slider points from crossing over each other 
        ),
    ], style = {'width':'50%', 'display':'inline-block'}, className = 'dbc'),  # Take up half of screen 
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(children = [
        dcc.Markdown(
            '''### Bubble Plot of Gross Worldwide x Rating x Budget ''', 
            style = {'color': 'rgba(226,217,243,255)'},
        ),
        dcc.Markdown(
            '''###### The bubble plot below depicts each film as a bubble, colored by director, sized by film budget. The x-axis is gross worldwide in millions, and the y-axis is the average film audience rating. ''',
            style = {'color': 'rgba(226,217,243,255)'},
        ),
    ], className = 'text-center' ),
    html.Div(children = [   # Graph, so it knows when to place it 
        dcc.Graph(
            id='bubble_graph',
        ), ],
        className = 'twelve columns'),
        #style = {'width':'50%', 'display':'inline-block'}, className = 'dbc'),   # Take up whole screen 
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(children = [
        dcc.Markdown(
            '''### Treemap of Motion Picture Ratings by Director ''',
            style = {'color': 'rgba(226,217,243,255)'}
        ),
        dcc.Markdown(
            '''###### The treemap below plots motion picture ratings by director. Each rectangle (or “tile”) represents a director, and the size of the rectangle corresponds to the total number of movies he or she has directed. Within each director’s rectangle, smaller rectangles (sub-tiles) represent individual movie ratings. The color of these sub-tiles indicate the number of movies with this rating. Essentially, this graph is a hierarchical way to display both the overall distribution of directors and the breakdown of movie ratings within their filmography. ''', 
            style = {'color': 'rgba(226,217,243,255)'}
        ),
    ], className = 'text-center' ),
    html.Div(children = [ 
         dcc.Graph(
             id='treemap',
         )], 
         #className = 'twelve columns',
    className = 'twelve columns'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(children = [
        dcc.Markdown(
            '''### Heatmap of Genre Correlation ''',
            style = {'color': 'rgba(226,217,243,255)'}
        ),
        dcc.Markdown(
            '''###### The heatmap below provides a visual representation of the relationships between different movie genres. Each genre will correspond to a row and a column in the heatmap. The cells in the heatmap are filled with colors representing the correlation between genres. Genres with a higher correlation (in this case the lighter-colored cells) are more often shared by a film. ''', 
            style = {'color': 'rgba(226,217,243,255)'}
        ),
    ], className = 'text-center' ),
    html.Br(),
    html.Div(children = [
        dcc.Graph(
            id='heatmap',
        ),
    ], className = 'twelve columns'), 
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(children = [
        dcc.Markdown(
            '''### Bar Graph of Budget and Box Office Gross ''', 
        style = {'color': 'rgba(226,217,243,255)'}
    ),
    dcc.Markdown(
            '''###### The bar graph below plots the budget and box office gross worldwide for each film by a chosen director. Since this graph can get busy with more than one director's work included, please specify only one director using the dropdown below. ''',
            style = {'color': 'rgba(226,217,243,255)'},
        ),
    ], className = 'text-center' ),
    html.Div(children = [   # Dropdown 
        html.Label('Select Director'),
        dcc.Dropdown(
            options = [{'label':director, 'value':director} for director in df_Directors['Director'].unique()],  # Options are all directors in dataset
            value = [],   # Making the default value an empty list of directors 
            multi = False,    # Can select more than one country
            id = 'second_director_dropdown',  
            ),
    ], style = {'margin':'auto', 'width':'50%', 'display':'inline-block'}, className = 'dbc'),
    html.Br(),
    html.Div(children = [
        dcc.Graph(
            id='bar_graph',
        ), 
    ], className = 'twelve columns'), 
        #style = {'width':'50%', 'display':'inline-block'}, className = 'dbc'),
    html.Br(),
    html.Br(),
    html.Br(),
], className = 'dbc')   # Placement along row 


# Every function must have its own callback operator
@callback(
    Output('bubble_graph', 'figure'),   # Outputs
    Output('treemap', 'figure'),
    Output('heatmap', 'figure'),
    # Output('bar_graph', 'figure'), # allow_duplicate = True
    Input('director_dropdown', 'value'),   # Dropdown input 
    Input('range_slider', 'value'),   # Slider input 
    # Input('second_director_dropdown', 'value'),
    #prevent_initial_call=True   # May not need this, but fixed an error at one point 
)

def update_graph(selected_director, year_range):
    # create trace1 

    choices = df_Directors[df_Directors['Director'].isin(selected_director)]
    choices = choices[choices['Release Year'].astype(int).between(year_range[0], year_range[1])]

    fig1 = px.scatter(
        choices, 
        x="Gross worldwide (in millions)", 
        y="Rating (Out of 10)", 
        size="Budget (in millions)", 
        color='Director',
        hover_name='Title',
        opacity = 0.9,
        #color_discrete_sequence = 'Light24',
        #legend='full', 
    )

    fig1.update_layout(
        yaxis_range=[0,10],
        paper_bgcolor = 'rgba(37,13,73,1)',
        plot_bgcolor = 'rgba(37,13,73,1)',
        xaxis_gridcolor = 'rgba(37,13,73,255)',
        yaxis_gridcolor = 'rgba(37,13,73,255)',
        font = dict(
            color = 'rgba(226,217,243,255)',
        )
    )

    fig1.update_xaxes(
        #rangeslider_yaxis_rangemode="fixed",
        showgrid=False,
        showline = True,
        linewidth = 2,
        linecolor = 'rgba(226,217,243,255)'
    )

    fig1.update_yaxes(
        showgrid=False,
        zeroline = True,
        zerolinewidth = 2,
        zerolinecolor = 'rgba(226,217,243,255)'
    )

    director_rating_counts = choices.groupby(["Director", "Motion Picture Rating"]).size().reset_index(name="count")

    # Create the treemap
    fig2 = px.treemap(
        director_rating_counts,
        path=["Director", "Motion Picture Rating"],
        values="count",
        title="Motion Picture Ratings by Director",
        color="count",  # You can customize the color scale
    )

    fig2.update_layout(
        paper_bgcolor = 'rgba(37,13,73,255)',
        plot_bgcolor = 'rgba(37,13,73,255)',
        xaxis_gridcolor = 'rgba(37,13,73,255)',
        yaxis_gridcolor = 'rgba(37,13,73,255)',
        font = dict(
            color = 'rgba(226,217,243,255)',
        )
    )

    fig2.data[0].hovertemplate='%{label}<br>%{value}'

    genres_df = choices['Main Genres'].str.get_dummies(sep=',')

    # Calculate the correlation matrix
    corr_matrix = genres_df.corr()
    # Create the heatmap using Plotly
    heat = go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='agsunset',
        zmin=-1,
        zmax=1
    )

    layout = go.Layout(
        #title='Genre Correlation Matrix',
        xaxis_showgrid=False,
        yaxis_showgrid=False
    )

    fig3 = go.Figure(data=[heat], layout=layout)

    fig3.update_layout(
        paper_bgcolor = 'rgba(37,13,73,255)',
        plot_bgcolor = 'rgba(37,13,73,255)',
        xaxis_gridcolor = 'rgba(37,13,73,255)',
        yaxis_gridcolor = 'rgba(37,13,73,255)',
        font = dict(
            color = 'rgba(226,217,243,255)',
        )
    )

    return fig1, fig2, fig3, #fig4

@callback(
    Output('bar_graph', 'figure'), # allow_duplicate = True
    # Input('range_slider', 'value'),   # Slider input 
    Input('second_director_dropdown', 'value'),
    #prevent_initial_call=True   # May not need this, but fixed an error at one point 
)
def update_bar_graph(second_selected_director):
    second_choice = df_Directors[df_Directors['Director'] == second_selected_director]

    trace1 = go.Bar(
        x = second_choice['Title'],
        y = second_choice['Budget (in millions)'],
        name = "Budget",
        marker = dict(color = 'rgba(255,255,0,0.9)',
            line=dict(color='rgb(0,0,0)',width=1.5)),
    )
    #create trace2 
    trace2 = go.Bar(
        x = second_choice['Title'],
        y = second_choice['Gross worldwide (in millions)'],
        name = "Box Office Gross Worldwide",
        marker = dict(color = 'rgba(236,60,188,0.9)',
            line=dict(color='rgb(0,0,0)',width=1.5)),
        #text = df_Nolan.Title
        )  
    data = [trace2, trace1]
    layout = go.Layout(barmode = "group", xaxis={'categoryorder':'max descending'})
    fig4 = go.Figure(data = data, layout = layout)


    fig4.update_layout(
        xaxis_title='Film Title',
        yaxis_title='Dollars in Millions',
        paper_bgcolor = 'rgba(37,13,73,1)',
        plot_bgcolor = 'rgba(37,13,73,1)',
        xaxis_gridcolor = 'rgba(37,13,73,1)',
        yaxis_gridcolor = 'rgba(37,13,73,1)',
        font = dict(
            color = 'rgba(226,217,243,1)',
        )
    )
    
    fig4.update_xaxes(
        showgrid=False,
        showline = True,
        linewidth = 2,
        linecolor = 'rgba(226,217,243,5)'
    )

    fig4.update_yaxes(
        showgrid=False,
        zeroline = True,
        zerolinewidth = 2,
        zerolinecolor = 'rgba(226,217,243,5)'
    )

    return fig4

# Run app
if __name__ == '__main__':
    app.run_server(jupyter_mode='tab', debug=True)
