import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
# from utils.auth import server 

# Create a Dash app
app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=False, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = html.Div([
    dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("Receipt Manager", href='/home/layout',style={'font-family':'Monospace','color':'#2E4F71'}),
                dbc.Nav(
                    [dbc.NavLink(page['name'], style={'font-family':'Monospace','color':'#2E4F71'},href=page['relative_path']) for page in dash.page_registry.values()],
                    className="ms-auto",  # ms-auto will push the navigation to the right
                    navbar=True
                )
            ],
            fluid=True,  # Use fluid to align content width to the screen width
        ),
        color="#C4CEE0",  # Background color
        style={"color":"#2E4F71"}     # Text color
    ),
    dash.page_container
])


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

