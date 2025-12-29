import dash
from dash import Dash, html, dcc


app=dash.Dash(__name__)

app.layout=html.Div(
    children=[
        html.H1('Sales Dashboard'),dcc.Graph(
    figure={
        "data": [
            {
                "x": ["Jan", "Feb", "Mar", "Apr", "May"],
                "y": [12000, 15000, 17000, 16000, 20000],
                "type": "line",
                "name": "Total Sales"
            }
        ],
        "layout": {
            "title": "Monthly Sales Trend",
            "xaxis": {"title": "Month"},
            "yaxis": {"title": "Revenue ($)"}
        }
    }
)

    ] 
)
if __name__ == "__main__":
    app.run(debug=True)