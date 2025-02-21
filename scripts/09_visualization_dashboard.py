import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/match_history.csv")
win_rate = df.groupby("P1_Move")["Result"].value_counts(normalize=True).unstack()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=px.imshow(win_rate, labels=dict(x="Move", y="Outcome", color="Win Rate"))),
    dcc.Graph(figure=px.line(pd.read_csv("outputs/strategy_elo_progression.csv")))
])

if __name__ == "__main__":
    app.run_server(debug=True)