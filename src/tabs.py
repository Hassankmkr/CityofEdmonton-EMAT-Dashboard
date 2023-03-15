import dash_daq as daq
import pathlib
import plotly
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from controls import UNCERTAINTIES, LEVERS
from helpers import  info_modal, landuse_modal, AB_modal, C_modal, D_modal, E2_modal, E5_modal, levers_modal, uncertainties_modal

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
plotly.io.json.config.default_engine = 'orjson'
## Load data
df = pd.read_csv(
    DATA_PATH.joinpath("outFeb17.csv"),
)

BCM_df = pd.read_csv(
    DATA_PATH.joinpath("BCM - Revised.csv"),
)
def main_tab():
    child = [
        info_modal,
        landuse_modal,
        AB_modal,
        C_modal,
        D_modal,
        E2_modal,
        E5_modal,
        levers_modal,
        uncertainties_modal,
        html.Div(
            dcc.Store(
                id="item_range_list",
                data=df.to_dict("records")
            ),
        ),
        html.Div(
            dcc.Store(
                id="BCM_range_list",
                data=BCM_df.to_dict("records")
            ),
        ),
        html.Div(
            html.Div(
                [
                    html.Div(
                        html.H4("Policy Levers and Uncertainties",
                        id="policy_levers_title_box",
                        className="pretty_container twelve columns",
                        style={"font-weight":"bold", 'textAlign': 'center', 'backgroundColor':'rgb(47, 99, 173)', "margin": "3px"},
                        ),
                    ),
                    html.Div(
                        [
                            # html.Img(
                            #     id="open-landuse-modal",
                            #     src="assets/question-circle-solid.svg",
                            #     n_clicks=0,
                            #     style={"display": "inline-block", "height": "2.2rem", "width": "2.2rem", "margin": "0.5rem", "float": "right", "cursor": "pointer"}
                            # ),
                            html.H6(
                                "Growth Management Policies, Actions and Levers",
                                style={"text-align": "center" ,"font-weight":"bold"},
                            ),
                            html.Div(
                                [
                                    html.P("Delayed Land Release + Upzonning in Redeveloping Areas", className="nine columns"),
                                    daq.BooleanSwitch(
                                        on=False,
                                        color="rgba(0, 126, 93, 1)",
                                        id="Policy AB",
                                        className="two columns"
                                    ),
                                    html.Img(
                                        id="open-AB-modal",
                                        src="assets/question-circle-solid.svg",
                                        n_clicks=0,
                                        style={"display": "inline-block", "height": "2.18rem", "width": "2.18rem", "margin": "0rem", "float": "right", "cursor": "pointer"}
                                    ),
                                    
                                    html.P("Differential Residential Tax", className="nine columns"),
                                    daq.BooleanSwitch(
                                        on=False,
                                        color="rgba(0, 126, 93, 1)",
                                        id="Policy C",
                                        className="two columns"
                                    ),
                                    html.Img(
                                        id="open-C-modal",
                                        src="assets/question-circle-solid.svg",
                                        n_clicks=0,
                                        style={"display": "inline-block", "height": "2.18rem", "width": "2.18rem", "margin": "0rem", "float": "right", "cursor": "pointer"}
                                    ),
                                    
                                    html.P("Upzoning in Nodes and Corridors", className="nine columns"),
                                    daq.BooleanSwitch(
                                        on=False,
                                        color="rgba(0, 126, 93, 1)",
                                        id="Policy D",
                                        className="two columns"
                                    ),
                                    html.Img(
                                        id="open-D-modal",
                                        src="assets/question-circle-solid.svg",
                                        n_clicks=0,
                                        style={"display": "inline-block", "height": "2.18rem", "width": "2.18rem", "margin": "0rem", "float": "right", "cursor": "pointer"}
                                    ),
                                    
                                    html.P("Increase in Automobile Operating Cost (2x)", className="nine columns"),
                                    daq.BooleanSwitch(
                                        on=False,
                                        color="rgba(0, 126, 93, 1)",
                                        id="Policy 2E",
                                        className="two columns"
                                    ),
                                    html.Img(
                                        id="open-E2-modal",
                                        src="assets/question-circle-solid.svg",
                                        n_clicks=0,
                                        style={"display": "inline-block", "height": "2.18rem", "width": "2.18rem", "margin": "0rem", "float": "right", "cursor": "pointer"}
                                    ),
                                    
                                    html.P("Increase in Automobile Operating Cost (5x)", className="nine columns"),
                                    daq.BooleanSwitch(
                                        on=False,
                                        color="rgba(0, 126, 93, 1)",
                                        id="Policy 5E",
                                        className="two columns"
                                    ),
                                    html.Img(
                                        id="open-E5-modal",
                                        src="assets/question-circle-solid.svg",
                                        n_clicks=0,
                                        style={"display": "inline-block", "height": "2.18rem", "width": "2.18rem", "margin": "0rem", "float": "right", "cursor": "pointer"}
                                    ),
                                ],
                                className="twelve columns",
                                style={"padding": "15px"}
                            ),
                        ],
                        className="twelve columns",
                        style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"},
                        id="Land Use/Growth Policies-div"
                    ),
                    html.Div(
                        [
                            html.Img(
                                id="open-levers-modal",
                                src="assets/question-circle-solid.svg",
                                n_clicks=0,
                                style={"display": "inline-block", "height": "2.2rem", "width": "2.2rem", "margin": "0.5rem", "float": "right", "cursor": "pointer"}
                            ),
                            html.H6(
                                "Mobility Policies, Actions and Levers",
                                style={"font-weight":"bold", 'textAlign': 'center'},
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P("Changes in Transit Fare", className="five columns"),
                                            html.Div(
                                                dcc.RangeSlider(
                                                    id=LEVERS[0]+"-slider",
                                                    min=0,
                                                    max=2.5,
                                                    value=[0, 2.5],
                                                    marks={
                                                        0: '0.1x',
                                                        0.5: '0.5x',
                                                        1: '1x',
                                                        1.5: '1.5x',
                                                        2: '2x',
                                                        2.5: "2.5x",
                                                    },
                                                    tooltip={
                                                        "placement": "bottom",
                                                        "always_visible": False
                                                    },    
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            ),
                                        ],className="pretty-container twelve columns",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Changes in Parking Cost", className="five columns"),
                                            html.Div(
                                                dcc.RangeSlider(
                                                    id=LEVERS[1]+"-slider",
                                                    min=0,
                                                    max=2.5,
                                                    value=[0,2.5],
                                                    marks={
                                                        0: '0.1x',
                                                        0.5: '0.5x',
                                                        1: '1x',
                                                        1.5: '1.5x',
                                                        2: '2x',
                                                        2.5: "2.5x"
                                                    },
                                                    tooltip={
                                                        "placement": "bottom",
                                                        "always_visible": False
                                                    }
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            ),
                                        ],className="pretty-container twelve columns",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Emergence of Shared Mobility Services", className="five columns"),
                                            html.Div(
                                                dcc.RangeSlider(
                                                    id=LEVERS[3]+"-slider",
                                                    step=None,
                                                    min=-10,
                                                    max=25,
                                                    marks={
                                                        -10: 'Low',
                                                        -5: '',
                                                        0: 'Current',
                                                        4: '',
                                                        8: 'Moderate',
                                                        12: '',
                                                        16: 'High',
                                                        20.5: '',
                                                        25: 'Extreme'
                                                    },
                                                    value=[-10,25]
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            ),
                                        ],className="pretty-container twelve columns",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Investment in Transit and Active Mode Infrastructure", className="five columns"),
                                            html.Div(
                                                dcc.Dropdown(
                                                    id=LEVERS[2]+"-dropdown",
                                                    options=[{'label': 'Limited', 'value': "BNR"},{'label': 'Aspirational', 'value': "MTN"}],
                                                    value=["BNR", "MTN"],
                                                    placeholder="Transit Network",
                                                    multi=True,
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            )
                                        ],className="pretty-container twelve columns",
                                    )   
                                ],
                                className="twelve columns",
                                style={"padding": "15px"}   
                            )
                        ],
                        className="twelve columns",
                        style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"}    
                    ),
                    html.Div(
                        [
                            html.Img(
                                id="open-uncertainties-modal",
                                src="assets/question-circle-solid.svg",
                                n_clicks=0,
                                style={"display": "inline-block", "height": "2.2rem", "width": "2.2rem", "margin": "0.5rem", "float": "right", "cursor": "pointer"}
                            ),
                            html.H6(
                                "Uncertainties",
                                style={"font-weight":"bold", 'textAlign': 'center'},
                            ), 
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.P("Economic Diversification", className="ten columns"),
                                            daq.BooleanSwitch(
                                                on=False,
                                                color="rgba(0, 126, 93, 1)",
                                                id="Policy F",
                                                className="two columns"
                                            ),
                                        ],
                                        className="pretty-container twelve columns",  
                                    ),
                                    html.Div(
                                        [
                                            html.P("Emergence of Hybrid Work", className="five columns"),
                                            html.Div(
                                                dcc.RangeSlider(
                                                    id=UNCERTAINTIES[0]+"-slider",
                                                    min=5,
                                                    max=40,
                                                    value=[5,40],
                                                    marks={
                                                        5: '5%',
                                                        10: '10%',
                                                        20: '20%',
                                                        30: '30%',
                                                        40: "40%"
                                                    },
                                                    tooltip={
                                                        "placement": "bottom",
                                                        "always_visible": False
                                                    },    
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            ),
                                        ],
                                        style={"margin-top": "10px"},
                                        className="pretty-container twelve columns",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Changes in Citizens' Perception Towards Transit", className="five columns"),
                                            html.Div(
                                                dcc.RangeSlider(
                                                    id=UNCERTAINTIES[6]+"-slider",
                                                    step=None,
                                                    min=-10,
                                                    max=10,
                                                    marks={
                                                        -10: 'Very Low',
                                                        -7.5: '',
                                                        -5: 'Low',
                                                        -2.5: '',
                                                        0: 'Current',
                                                        2.5: '',
                                                        5: 'High',
                                                        7.5: '',
                                                        10: "Extreme"
                                                    },
                                                    value=[-10,10]
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            ),
                                        ],
                                        style={"margin-top": "10px"},
                                        className="pretty-container twelve columns",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Emergence of Micromobility", className="five columns"),
                                            html.Div(
                                                dcc.RangeSlider(
                                                    id=UNCERTAINTIES[8]+"-slider",
                                                    step=None,
                                                    min=0,
                                                    max=10,
                                                    marks={
                                                        0: 'Current',
                                                        1.25: '',
                                                        2.5: 'Low',
                                                        3.75: '',
                                                        5: 'Moderate',
                                                        6.25: '',
                                                        7.5: 'High',
                                                        8.75: '',
                                                        10: "Extreme"
                                                    },
                                                    value=[0,10]
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            ),
                                        ],
                                        style={"margin-top": "5px"},
                                        className="pretty-container twelve columns",
                                    ),
                                    html.Div(
                                        [
                                            html.P("Market Adoption of Electric Vehicles", className="five columns"),
                                            html.Div(
                                                dcc.Dropdown(
                                                    id=UNCERTAINTIES[7]+"-dropdown",
                                                    options=[{'label': 'Minimal', 'value': "Base"},{'label': 'High (26%)', 'value': "EV"}],
                                                    value="Base",
                                                    multi=False,
                                                ),
                                                style={"display": "inline-block", "width": "55%", "float": "right"}
                                            )
                                        ],
                                        style={"margin-top": "10px"},
                                        className="pretty-container twelve columns",
                                    )
                                ],
                                className="twelve columns",
                                style={"padding": "15px"}
                            )
                        ],
                        className="twelve columns",
                        style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"}
                    )
                ],
                style={"position": "block", "overflow": "scroll", "pointer-events": "auto", "height": "100vh"},
                id="policy-div",
            ),
            className="pretty_container four columns",
            style={"position": "sticky", "top": "0px", "float": "left", "display": "inline-block"},
        ),
        html.Div(
            [
                html.Div(
                    html.H4("BCM - A Rebuildable City",
                    className="pretty_container twelve columns",
                    style={"font-weight":"bold", 'textAlign': 'center', 'backgroundColor':'rgba(65, 154, 197, 0.5)', "margin": "3px"},
                    ),
                ),
                # html.Div(
                #     [
                #         dcc.Graph(
                #             id="A Rebuildable City-graph",
                #             figure=go.Figure(
                #             ),
                #             className="pretty-container twelve columns",
                #         ),
                #     ],
                #     className="pretty-container twelve columns",
                #     style={"border-style":"double", "border-color": "rgba(189, 195, 199, 1)", "margin-top": "5px"}
                # ),
                html.Div(
                    [
                        html.H4("% of Net New Units Added Through Infill (2 Million City Target: 50%)",
                            id="50% Net New Units will be added through Infill City wide",
                            style={'textAlign': 'center', "font-weight":"bold"},
                        ),
                        dcc.Graph(
                            id="50% Net New Units will be added through Infill City wide-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgba(189, 195, 199, 1)", "margin-top": "5px"} 
                ),
                html.Div(
                    [
                        html.H4("Additional Residents Welcomed into the Redeveloping Areas (2 Million City Target: 600k)",
                            id="600k additional residents will be welcomed within redeveloping Area", 
                            style={'textAlign': 'center', "font-weight":"bold"},
                        ),
                        dcc.Graph(
                            id="600k additional residents will be welcomed within redeveloping Area-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        )
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgba(189, 195, 199, 1)", "margin-top": "5px"} 
                ),
                html.Div(
                    html.H4("BCM - Catalyze and Converge",
                    className="pretty_container twelve columns",
                    style={"font-weight":"bold", 'textAlign': 'center', 'backgroundColor':'rgba(65, 154, 197, 0.5)', "margin": "3px", "margin-top": "5px"},
                    ),
                ),
                # html.Div(
                #     [
                #         dcc.Graph(
                #             id="Catalyze and Converge-graph",
                #             figure=go.Figure(
                #             ),
                #             className="pretty-container twelve columns",
                #         ),
                #     ],
                #     className="pretty-container twelve columns",
                #     style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"}
                # ),
                html.Div(
                    [
                        html.H4("% of Edmonton Employment in Nodes and Corridors (2 Million City Target: 50%)",
                            id="Nodes and Corridors support 50% of all employment in Edmonton",
                            style={"font-weight":"bold", 'textAlign': 'center'},
                        ),
                        dcc.Graph(
                            id="Nodes and Corridors support 50% of all employment in Edmonton-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"} 
                ),
                html.Div(
                    [
                        html.H4("Additional Employment in Innovation Corridor (2 Million City Target: 50k)",
                            id="Innovation Corridor attracts 50,000 more employment",
                            style={"font-weight":"bold", 'textAlign': 'center'},
                        ),
                        dcc.Graph(
                            id="Innovation Corridor attracts 50,000 more employment-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"} 
                ),
                html.Div(
                    [
                        html.H4("% of Total Regional Employment in Edmonton (2 Million City Target: 70%)",
                            id="Hold 70% of total regional employment in Edmonton",
                            style={"font-weight":"bold", 'textAlign': 'center'},
                        ),
                        dcc.Graph(
                            id="Hold 70% of total regional employment in Edmonton-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"} 
                ),
                html.Div(
                    html.H4("BCM - Greener as We Grow",
                    className="pretty_container twelve columns",
                    style={"font-weight":"bold", 'textAlign': 'center', 'backgroundColor':'rgba(65, 154, 197, 0.5)', "margin": "3px", "margin-top": "5px"},
                    ),
                ),
                html.Div(
                    [
                        html.H4("Net Per Person GHG Emissions (2 Million City Target: ZERO)",
                            id="Net per person GHG emissions are zero",
                            style={"font-weight":"bold", 'textAlign': 'center'},
                        ),
                        dcc.Graph(
                            id="Net per person GHG emissions are zero-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="Net per person GHG emissions are zero2-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"} 
                ),
                html.Div(
                    html.H4("BCM - A Community of Communities",
                    className="pretty_container twelve columns",
                    style={"font-weight":"bold", 'textAlign': 'center', 'backgroundColor':'rgba(65, 154, 197, 0.5)', "margin": "3px", "margin-top": "5px"},
                    ),
                ),
                html.Div(
                    [
                        html.H4("Mode Share by Transit and Active Modes (2 Million City Target: 50%)",
                            id="50% Mode Share by Transit and Active Modes",
                            style={"font-weight":"bold", 'textAlign': 'center'},
                        ),
                        dcc.Graph(
                            id="50% Mode Share by Transit and Active Modes-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="50% Mode Share by Transit and Active Modes2-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="50% Mode Share by Transit and Active Modes3-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"} 
                ),
                html.Div(
                    [
                        html.H4("% of Daily Travel Within 15 Minutes District",
                            id="15 minute districts that allow people easily complete their daily needs",
                            style={"font-weight":"bold", 'textAlign': 'center'},
                        ),
                        dcc.Graph(
                            id="15 Minutes Districts-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="15 Minutes Districts2-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="15 Minutes Districts3-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="15 Minutes Districts4-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        dcc.Graph(
                            id="15 Minutes Districts5-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                        # dcc.Graph(
                        #     id="15 Minutes Districts6-graph",
                        #     figure=go.Figure(
                        #     ),
                        #     className="pretty-container twelve columns",
                        # ),
                        dcc.Graph(
                            id="15 Minutes Districts7-graph",
                            figure=go.Figure(
                            ),
                            className="pretty-container twelve columns",
                        ),
                    ],
                    className="pretty-container twelve columns",
                    style={"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"} 
                ),
            ],
            className="pretty_container eight columns",
            style={"display": "inline-block", "float": "right"}
        ),
    ]
    return child

# def main_2_tab():
#     child = [
#         html.Div(
#             dcc.Store(
#                 id="item_range_list_2",
#                 data=df.to_dict("records")
#             ),
#         ),
#         html.Div(
#             html.H4("EMAT Measures",
#                 id="emat_measures_title_box",
#                 style={"font-weight":"bold", 'textAlign': 'center'},
#             ),
#             className="pretty_container twelve columns",
#             style={'backgroundColor':'rgba(221, 161, 94, 0.5)'}
#         ),
#         html.Div(
#             [
#                 html.Div(
#                     [
#                         html.H6(
#                             "Select one of the EMAT measures:",
#                             style={"font-weight":"bold"}
#                         ),
#                         dcc.Dropdown(
#                             id="measures-dropdown",
#                             options=MEASURES,
#                             value=MEASURES[0],
#                             placeholder="EMAT Measures",
#                             multi=False,
#                             style={"margin-top": "1rem"},
#                         ),
#                         html.H6(
#                             "Select a range of the selected measure:",
#                             style={"font-weight":"bold", "margin-top": "3rem", "margin-bottom": "2rem"}
#                         ),
#                         dcc.RangeSlider(
#                             id="measures-slider",
#                             min=round_down(min(df["Ridership in City"]), 2),
#                             max=round(max(df["Ridership in City"]), 2),
#                             value=[
#                                 round_down(min(df["Ridership in City"]), 2),
#                                 round(max(df["Ridership in City"]), 2)
#                             ],
#                             tooltip={
#                                 "placement": "top",
#                                 "always_visible": True
#                             },
#                         ),
#                     ],
#                     className="pretty-container three columns",
#                     style={"margin-top": "2rem"}
#                 ),
#                 dcc.Graph(
#                     id="measures-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container nine columns",
#                 ),
#             ],
#             className="pretty_container twelve columns",
#             style={"border":"darkorange double"}
#         ),
#         html.Div(
#             html.H4("EMAT Inputs",
#                 id="emat_inputes_title_box",
#                 style={"font-weight":"bold", 'textAlign': 'center'},
#             ),
#             className="pretty_container twelve columns",
#             style={'backgroundColor':'rgba(69, 123, 157, 0.5)'}
#         ),
#         html.Div(
#             [
#                 dcc.Graph(
#                     id="Fare relative to base-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container four columns",
#                 ),
#                 dcc.Graph(
#                     id="Parking cost relative to base-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container four columns",
#                 ),
#                 dcc.Graph(
#                     id="Mobility as a service improvement-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container four columns",
#                 ),
#             ],
#             className="pretty_container twelve columns"
#         ),
#         html.Div(
#             [
#                 dcc.Graph(
#                     id="Transit network-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container four columns",
#                 ),
#                 dcc.Graph(
#                     id="Work at home-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container four columns",
#                 ),
#                 dcc.Graph(
#                     id="Utility change to transit alternatives-graph",
#                     figure=go.Figure(
#                     ),
#                     className="pretty-container four columns",
#                 ),
#             ],
#             className="pretty_container twelve columns"
#         )
#     ]
#     return child