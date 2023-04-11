import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objs as go

df = pd.read_csv("winners_data")
df = df["player_style"].value_counts().to_frame().reset_index()

pStyle_data = (
    df
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Test"),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    go.Bar(pStyle_data, x='index', y='player_style')
                    
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)