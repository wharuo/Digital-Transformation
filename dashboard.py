
import requests
from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px

app = Dash(__name__, external_stylesheets=[
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css"
])

app.layout = html.Div([
    html.H1("Fraud Detection Dashboard", className="text-center animate__animated animate__fadeInDown"),

    html.Div([
        dcc.Textarea(id="rules-input", placeholder="Enter rules here...", style={"width": "100%", "height": 100}),
        html.Button("Validate Rule", id="validate-btn", className="btn btn-primary animate__animated animate__pulse"),
        html.Div(id="validation-feedback", className="mt-3")
    ], className="container"),

    html.Div([
        dcc.Graph(id="issues-pie-chart", className="animate__animated animate__fadeInUp")
    ], className="container mt-4"),

    dcc.Interval(id="update-interval", interval=5000, n_intervals=0)
])

@app.callback(
    [Output("validation-feedback", "children"),
     Output("issues-pie-chart", "figure")],
    Input("validate-btn", "n_clicks"),
    State("rules-input", "value")
)
def validate_rules(n_clicks, rules):
    if not rules:
        return "Please enter a rule to validate.", px.scatter()

    response = requests.post("http://127.0.0.1:5000/validate", json={"rules": rules})
    data = response.json()
    issues = data.get("issues", [])
    status = "Success" if not issues else "Warning"

    fig = px.pie(names=["No Issues", "Issues"], values=[1, len(issues)], title="Validation Summary")
    return f"Status: {status}, Issues: {', '.join(issues)}", fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
