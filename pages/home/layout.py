import dash_bootstrap_components as dbc
from dash import dcc, html, register_page
# from .callbacks import *

register_page(__name__, name="HOME", relative_path="/home")

def layout():
    return dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Receipt Manager", className="my-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.H2("Empowering You to Take Control of Your Finances", className="my-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                dbc.CardImg(
                    src="/static/images/background.png",
                    top=True,
                    style={"opacity": 1,'magrin-bottom':'20px'},
                ),
                width = 12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    "Welcome to Receipt Manager, your personal assistant for tracking spending habits and gaining more control over your finances.Our app is designed to help you manage your receipts effortlessly and keep a close eye on your expenses. Our goal is to make it easier for you to understand where your money goes and make informed financial decisions.",
                    className="lead"
                ),
                width=12
            )
        ),
      
        dbc.Row(
                [
                    html.H3("Key Features", className="my-4"),
                    
                    dbc.Col([
                            dbc.CardImg(
                                src="/static/images/receipt.png",
                                top=True,
                                style={"opacity": 1,'height':'30%','width':'30%'},
                            ),
                            html.P(
                                "Capture and upload receipts with ease",
                                className="lead"
                             
                            ),
                        ],
                        width=6, lg=3
                    ),
                    dbc.Col([
                        dbc.CardImg(
                                src="/static/images/wallet2.png",
                                top=True,
                                style={"opacity": 1,'height':'30%','width':'30%'},
                            ),
                        html.P(
                            "Organize and categorize your expenses",
                            className="lead"
                        ),
                        ],
                        width=6, lg=3
                    ),
                    dbc.Col([
                        dbc.CardImg(
                                src="/static/images/analysis2.png",
                                top=True,
                                style={"opacity": 1,'height':'30%','width':'30%'},
                            ),
                        html.P(
                            "Detailed analytics to track spending patterns",
                            className="lead"
                        ),
                        ],
                        width=6, lg=3
                    ),
                    dbc.Col([
                        dbc.CardImg(
                                src="/static/images/database.png",
                                top=True,
                                style={"opacity": 1,'height':'30%','width':'30%'},
                            ),
                        html.P(
                            "Secure cloud storage for all your receipts",
                            className="lead"
                        ),],
                        width=6, lg=3
                    )
                ],
                style={"text-aligh":"center"}
            
            ),
        dbc.Row(
            dbc.Col(
                [
                    html.H3("Our Vision", className="my-4"),
                    html.P(
                        "We envision a world where everyone has complete control over their finances. Our mission is to continuously improve Receipt Manager to provide more insightful and actionable data, helping you save money and make smarter financial decisions. We are committed to your financial well-being and aim to be your trusted partner in this journey.",
                        className="lead"
                    ),
                ],
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    dcc.Link("Ready to take control of your finances? Sign up now and start using Receipt Manager today!", href="/signup", className="btn btn-primary"),
                    className="text-center my-4"
                ),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    "Contact us: support@receiptmanager.com",
                    className="text-center my-4"
                ),
                width=12
            )
        ),
    ],
    fluid=True,
    style={'text-align':'center', 'width':'50%'}
)
