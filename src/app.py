# Import required libraries
import pathlib
import plotly
import dash
import time
import pandas as pd
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go

# Multi-dropdown options
from controls import UNCERTAINTIES, LEVERS, REFERENCE_VALUES, SLIDERS, LU_POLICIES
from tabs import main_tab 
from helpers import human_format

stime = time.time()
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

total_color = 'rgba(240, 88, 83, 0.6)'
selected_color = 'rgba(47, 99, 173, 0.6)'


# Header

def make_header() -> html.Header:
    """
    Returns a HTML Header element for the application Header.

    :return: HTML Header
    """
    return html.Header(
        children=[
            # Icon and title container
            html.Div(
                children=[
                    html.Img(src="assets/City_of_Edmonton_Logo.png", style={'height':'100px', 'width':'100px'}),
                    html.H1(className="dash-title", children=["Exploratory Modeling and Analysis of City of Edmonton Growth by 1.25 Million Horizon"]),
                ],
                className="dash-title-container",
                style={'margin-right': 'auto'}
            ),
            html.Div(
                html.Button(
                    "About",
                    id="open-info-modal",
                    n_clicks=0,
                    style={'color': 'primary',
                        'font-style': 'italic', 
                        "display": "inline-block", 
                        "margin": "3rem", 
                        "float": "right", 
                        "cursor": "pointer"
                    },        
                ),
            ),
   
            ## create navigator with buttons
            # html.Nav(
            #     children=[
            #         dcc.Tabs(
            #             id="navigation-tabs",
            #             value="Dashboard",
            #             children=[
            #                 dcc.Tab(
            #                     label="Info",
            #                     value="Info",
            #                     className="dash-tab",
            #                     selected_className="dash-tab-selected",
            #                 ),
            #                 dcc.Tab(
            #                     label="Dashboard",
            #                     value="Dashboard",
            #                     className="dash-tab",
            #                     selected_className="dash-tab-selected",
            #                 ),
            #             ],
            #         ),
            #     ]
            # ),
        ]
    )

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}], external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server
app.title = "City of Edmonton - EMAT"
app.config["suppress_callback_exceptions"] = True


# Create app layout

# for id in ["Land Use/Growth Policies"]:

#     @app.callback(
#         [Output(f"{id}-modal", "style"), Output(f"{id}-div", "style")],
#         [Input(f"show-{id}-modal", "n_clicks"), Input(f"close-{id}-modal", "n_clicks")],
#     )
#     def toggle_modal(n_show, n_close):
#         ctx = dash.callback_context
#         if ctx.triggered and ctx.triggered[0]["prop_id"].startswith("show-"):
#             return {"display": "block"}, {"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"}
#         else:
#             return {"display": "none"}, {"border-style":"double", "border-color": "rgb(189, 195, 199)", "margin-top": "5px"}

@app.callback(
    Output("info_modal", "is_open"),
    [Input("open-info-modal", "n_clicks"), Input("close_info_modal", "n_clicks")],
    [State("info_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# @app.callback(
#     Output("landuse_modal", "is_open"),
#     [Input("open-landuse-modal", "n_clicks"), Input("close_landuse_modal", "n_clicks")],
#     [State("landuse_modal", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open

@app.callback(
    Output("AB_modal", "is_open"),
    [Input("open-AB-modal", "n_clicks"), Input("close_AB_modal", "n_clicks")],
    [State("AB_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("C_modal", "is_open"),
    [Input("open-C-modal", "n_clicks"), Input("close_C_modal", "n_clicks")],
    [State("C_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("D_modal", "is_open"),
    [Input("open-D-modal", "n_clicks"), Input("close_D_modal", "n_clicks")],
    [State("D_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("E2_modal", "is_open"),
    [Input("open-E2-modal", "n_clicks"), Input("close_E2_modal", "n_clicks")],
    [State("E2_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("E5_modal", "is_open"),
    [Input("open-E5-modal", "n_clicks"), Input("close_E5_modal", "n_clicks")],
    [State("E5_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("levers_modal", "is_open"),
    [Input("open-levers-modal", "n_clicks"), Input("close_levers_modal", "n_clicks")],
    [State("levers_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("uncertainties_modal", "is_open"),
    [Input("open-uncertainties-modal", "n_clicks"), Input("close_uncertainties_modal", "n_clicks")],
    [State("uncertainties_modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

app.layout = html.Div(
    [
        # dcc.Location(id="url"),
        make_header(),
        html.Div(
            main_tab()
            # id="tab-area"
        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)

# @app.callbacks

# @app.callback(
#     Output("tab-area", "children"),
#     Input("navigation-tabs", "value")
# )
# def render_tab(tab):
#     if tab == "Dashboard":
#         return main_tab()
#     elif tab == "Info":
#         return about_tab()
#### About Tab
# a = "TMIP-EMAT is a methodological approach to exploratory modeling and analysis. It provides a window to rigorous analytical methods for handling uncertainty and making well informed decisions using travel forecasting models of all types. It is designed to integrate with and enhance an existing transportation model or tool to perform exploratory analysis of a range of possible scenarios. In the documentation of TMIP-EMAT, we refer to the existing model or tool as the “core model”."
# b = "TMIP-EMAT provides the following features to enhance the functionality of the underlying core model:"
# c = "To be clear, TMIP-EMAT is not a standalone model or tool by itself, it must be integrated with a separate core model. Moreover, the quality of any analysis undertaken with TMIP-EMAT depends on the quality and capabilities of the underlying core model. If the core model does not contain an explicit representation of the transportation network, then TMIP-EMAT will not allow an analyst to study policy questions that hinge on the microscopic details of traffic congestion."
# d = "TMIP-EMAT is presented as a flexible, methodological approach applicable to many different core models. It is not a fully-developed end-to-end software solution. Because of this, developing a new implementation of TMIP-EMAT to connect with a new core model will require at least one developer with some technical expertise. The documentation and code published with TMIP-EMAT is meant as guide and a start, but someone with detailed knowledge of the technical operation of the core model and at least basic Python skills will need to write a connector between the core model and the TMIP-EMAT tools."
# e = "The core model itself does not need to be in Python, it can be created and run in any computer language. It should take a collection of inputs and generate one or more outputs, or “performance metrics”, of interest. Inputs can include variable inputs (e.g., fuel cost) as well as model parameter inputs (e.g., the elasticity of vehicle travel with respect to fuel cost). Examples of a core model include, but are not necessarily limited to the following:"
# f = "TMIP-EMAT can be used to systematically explore uncertainties in input variables and model parameters, and the impact that those uncertainties have on performance metrics. It is useful for examining model forecasts as a range of model outcomes rather than a single outcome, and it provides a mechanism for defining uncertainties and visualizing outputs."
# g = "TMIP-EMAT can also be used to understand how uncertainties interact with policy decisions (e.g., extending a transit line), where uncertainties relate to model inputs and variables that are outside of the policy-maker’s control, and policy levers are model inputs that are within the policy-maker’s control."
# h = "If the existing tool or model is computationally expensive to run, TMIP-EMAT can generate meta-models of the core model that describe how a set of model inputs impact specific performance metrics. These meta-models are formulated as regression models of core model outputs that run very quickly (microseconds) and allow model input uncertainties to be explored systematically while limiting the number of computationally expensive core model runs."
# i = "The core model is interfaced with TMIP-EMAT using an API. The API enables TMIP-EMAT to programmatically define scenarios, launch, retrieve errors and status, and import metrics from the core model. The API should allow for configuration of all uncertainties and policy levers that are input to the system as well as configuration of the desired performance metrics. The core model should be well-validated to ensure model sensitivities are reasonable."
# j = "Uncertainty Definitions. Uncertainty definitions include the overall range, correlation, and distribution of the risk variables that were selected for the analysis. Uncertainties represent exogenous inputs to the core model that impact the forecasts of the core model, and may include input variables, model parameters, or model structures. The set of uncertainties input to TMIP-EMAT will typically be smaller than the full domain of inputs to the core model. Uncertainties should be selected based on the importance of the variable in the context of the scope of the analysis (considering policy levers and metrics of interest) and the relative impact the variable has on relevant performance metrics."
# k = "Policy Lever Definitions. Policy lever definitions include the specification of specific strategies/choices to test in the analysis, including the range in potential lever options. Levers (i.e., policy levers) represent inputs to the core model that impact the model’s forecasts, but are controllable by planners or decision makers. They can include individual variable inputs to the model (e.g., toll price) or can represent a portfolio of changes to the model (e.g., a transit line extension)."
# l = "Performance Metric Definitions. The set of metrics that will be analyzed must be defined. A performance metric is an output of the core model and represents a gage by which the impact of changes in uncertainties and levers can be measured. Often core models will have a large number of intermediate and final outputs that could be considered here. Metrics should be selected based on their relevance to the analysis and for decision makers."

# @app.callback(
#     Output("page-content", "children"),
#     [Input("url", "pathname")]
# )
# def render_page_content(pathname):
#     if pathname == "/":
#         return [
#                 html.H4('Introduction to EMAT',
#                         style={'textAlign':'left', 'font-weight':'bold'}),
#                 html.H6(a,
#                         style={'textAlign':'left'}),
#                 html.H6(b,
#                         style={'textAlign':'left'}),
#                 html.H6([html.Li("A structure to formalize and distill an exploratory scope, in a manner suitable for translating the abstraction of the “XLRM” robust decision making framework into a concrete, application-specific form,"),
#                          html.Li("A systematic process for designing experiments to be evaluated using the core model, and support for running those experiments in an automated fashion."),
#                          html.Li("A database structure to organize and store the results from a large number of experiments."),
#                          html.Li("A facility to automatically create a metamodel from experimental results, which uses machine learning techniques to rapidly approximate new outputs of the core model for without actually running it for every relevant combination of inputs."),
#                          html.Li("A suite a analytical and visualization tools to explore the relationships between modeled inputs and outputs, and develop robust policy strategies that might be effective across a range of possible future scenarios.")
#                          ],
#                         style={'textAlign':'left', 'margin-left': '40px'}),
#                 html.H6(c,
#                         style={'textAlign':'left'}),
#                 html.H6(d,
#                         style={'textAlign':'left'}),
#                 html.H4('The Core Model',
#                         style={'textAlign':'left', 'font-weight':'bold'}),
#                 html.H6(e,
#                         style={'textAlign':'left'}),
#                 html.H6([html.Li('Regional or statewide travel demand models'),
#                         html.Li("Activity-based travel models"),
#                         html.Li("Trip-based travel models"),
#                         html.Li("Sketch planning or spreadsheet model"),
#                         html.Li("Microsimulation models"),
#                         html.Li("Corridor-level travel model"),
#                         ],
#                         style={'textAlign':'left', 'margin-left': '40px'}),
#                 html.H6(f,
#                         style={'textAlign':'left'}),
#                 html.H6(g,
#                         style={'textAlign':'left'}),
#                 html.H6(h,
#                         style={'textAlign':'left'}),
#                 ]
#     elif pathname == "/page-1":
#         return [
#                 html.H4('Inputs',
#                         style={'textAlign':'left', 'font-weight':'bold'}),
#                 html.H6(
#                     html.Div([
#                         html.Span("1- Core model: ", style={'font-weight':'bold'}),
#                         i
#                     ]),
#                     style={'textAlign':'left', 'margin-left': '40px'}
#                 ),
#                 html.H4('Outputs',
#                         style={'textAlign':'left', 'font-weight':'bold'}),
                
#                 ]
#     elif pathname == "/page-2":
#         return [
#                 html.H1('Page 2',
#                         style={'textAlign':'center'}),
#                 ]

#### Main Tab
@app.callback(
    [
        Output("item_range_list", "data"),
        Output("BCM_range_list", "data")
    ],
    [
        Input("Policy AB", "on"),
        Input("Policy C", "on"),
        Input("Policy D", "on"),
        Input("Policy 2E", "on"),
        Input("Policy 5E", "on"),
        Input("Policy F", "on"),
        Input(SLIDERS[0]+"-slider", 'value'), 
        Input(SLIDERS[1]+"-slider", 'value'),
        Input(SLIDERS[2]+"-slider", 'value'),
        Input(SLIDERS[3]+"-slider", 'value'),
        Input(SLIDERS[4]+"-slider", 'value'),
        Input(SLIDERS[5]+"-slider", 'value'),
        Input(LEVERS[2]+"-dropdown", 'value')
    ]
)

def update_range_list_1(policy_AB, policy_C, policy_D, policy_2E, policy_5E, policy_F, value_range_0, value_range_1, value_range_2, value_range_3, value_range_4, value_range_5, dropdown_0):
    filter_data_df = df.copy()
    filter_BCM_df = BCM_df.copy()
    
    policy_AB = "{}".format(policy_AB)
    if policy_AB == "False":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[0]] == 0]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[0]] == 0]
    else:
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[0]] == 1]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[0]] == 1]
        
    policy_C = "{}".format(policy_C)
    if policy_C == "False":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[1]] == 0]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[1]] == 0]
    else:
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[1]] == 1]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[1]] == 1]
        
    policy_D = "{}".format(policy_D)
    if policy_D == "False":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[2]] == 0]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[2]] == 0]
    else:
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[2]] == 1]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[2]] == 1]
        
    policy_F = "{}".format(policy_F)
    if policy_F == "False":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[4]] == 0]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[4]] == 0]
    else:
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[4]] == 1]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[4]] == 1]
        
    policy_2E = "{}".format(policy_2E)
    policy_5E = "{}".format(policy_5E)
    if policy_2E == "False" and policy_5E == "False":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[3]] == 0]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[3]] == 0]
    elif policy_2E == "True" and policy_5E == "False":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[3]] == 1]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[3]] == 1]
    elif policy_2E == "False" and policy_5E == "True":
        filter_data_df = filter_data_df.loc[df[LU_POLICIES[3]] == 5]
        filter_BCM_df = filter_BCM_df.loc[BCM_df[LU_POLICIES[3]] == 5]
   
    filter_data_df = filter_data_df.loc[
        (df[SLIDERS[0]] >= value_range_0[0]) & (df[SLIDERS[0]] <= value_range_0[1]) &
        (df[SLIDERS[1]] >= value_range_1[0]) & (df[SLIDERS[1]] <= value_range_1[1]) &
        (df[SLIDERS[2]] >= value_range_2[0]) & (df[SLIDERS[2]] <= value_range_2[1]) &
        (df[SLIDERS[3]] >= value_range_3[0]) & (df[SLIDERS[3]] <= value_range_3[1]) &
        (df[SLIDERS[4]] >= value_range_4[0]) & (df[SLIDERS[4]] <= value_range_4[1]) &
        (df[SLIDERS[5]] >= value_range_5[0]) & (df[SLIDERS[5]] <= value_range_5[1])
    ]    
    
    if len(dropdown_0) > 0:
        filter_data_df = filter_data_df.loc[filter_data_df[LEVERS[2]].isin(dropdown_0)]
    return filter_data_df.to_dict("records"), filter_BCM_df.to_dict("records")


def graph_GHG(item, filtered_data, filtered_BCM_df):
    item11 = "Amount of GHG Produced (kgCO2e) (" + item + ")"
    updated_df = pd.DataFrame(filtered_data)
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    fig = make_subplots(
        rows=1,
        cols=4,
        specs=[
            [{"colspan": 3}, None, None, {"colspan": 1, "type": "indicator"}],
        ],
    )
    figure = fig.add_trace(
        go.Box(
            x=round(updated_df[item11] / 1000 * 333 / (updated_BCM_df["Total Population in the City"].values[0]), 1), # Ton / Year / Person
            name="Selected Policy, Lever and Uncertainty Combinations",
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=round(df[item11] / 1000 * 333 / (updated_BCM_df["Total Population in the City"].values[0]), 1),
            name="All Policy, Lever and Uncertainty Combinations",
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.update_xaxes(tickformat = ".1f", range = [1, 3], showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
    figure = fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            number = {"suffix": " t"},
            value=round((sum(updated_df[item11]) / len(updated_df[item11]) / 1000 * 333 / (updated_BCM_df["Total Population in the City"].values[0])), 1),
            gauge = {
                'axis': {
                    "range": [0, 3], 
                    "tickmode": "array", 
                    "tickvals": [0, 0.5, 1, 1.5, 2, 2.5, 3], 
                    "ticktext":['0t', '0.5t', '1t', '1.5t', '2t', '2.5t', '3t'],
                    "tickangle":0
                },
                'bar': {
                    'color': "rgb(47, 99, 173)"
                },
                'steps': [
                    {'range': [updated_df[item11].min() / 1000 * 333 / (updated_BCM_df["Total Population in the City"].values[0]), updated_df[item11].max() / 1000 * 333 / (updated_BCM_df["Total Population in the City"].values[0])], 'color': "rgba(47, 99, 173, 0.5)"},
                ],

            },
        ),
        row=1,
        col=4
    )
    
    figure = fig.update_layout(
        title="<span style='font-weight:bold; font-size:1.5vw'>Annual Transportation GHG Emissions per Person in City (Tonnes)</span>",
        template="ggplot2",
        font_family="Times New Roman",
        margin=dict(l=20, r=60, t=90, b=40),
        height=400,
        showlegend=True,
        legend_traceorder="reversed",
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation="h"
        )
    )
    
    return figure

app.callback(
    Output("Net per person GHG emissions are zero-graph", "figure"),
    [Input(UNCERTAINTIES[7] + "-dropdown", 'value'), Input("item_range_list", "data"), Input("BCM_range_list", "data")]
)(graph_GHG)

def graph_GHG2(item, filtered_data):
    item11 = "Amount of GHG Produced (kgCO2e) (" + item + ")"
    updated_df = pd.DataFrame(filtered_data)
    fig = make_subplots(
        rows=1,
        cols=4,
        specs=[
            [{"colspan": 3}, None, None, {"colspan": 1, "type": "indicator"}],
        ],
    )
    figure = fig.add_trace(
        go.Box(
            x=round(updated_df[item11] / 1000 * 333, -4), # Ton / Year / Person
            name="Selected Policy, Lever and Uncertainty Combinations",
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=round(df[item11] / 1000 * 333, -4),
            name="All Policy, Lever and Uncertainty Combinations",
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.update_xaxes(tickformat = ".3s", range = [1.5e6, 4e6], showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
    if (sum(updated_df[item11]) / len(updated_df[item11]) / 1000 * 333) < REFERENCE_VALUES["2021 GHG by transportation sector"]:
        thresholdColor = "rgba(42, 145, 52, 1)"
    else:
        thresholdColor = "rgba(240, 88, 83, 1)"
        
    # if (sum(updated_df[item11]) / len(updated_df[item11]) / 1000 * 333) < REFERENCE_VALUES["2032 Annual GHG by RTM"]:
    #     thresholdColor2 = "rgba(42, 145, 52, 1)"
    # else:
    #     thresholdColor2 = "rgba(240, 88, 83, 1)"
        
    figure = fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            value=round((sum(updated_df[item11]) / len(updated_df[item11]) / 1000 * 333), -4),
            # delta={
            #     'reference': REFERENCE_VALUES["2021 GHG by transportation sector"], 
            #     "suffix": " t", 
            #     "increasing": {"color": "rgba(240, 88, 83, 1)"}, 
            #     "decreasing": {"color": "rgba(42, 145, 52, 1)"}
            # },
            number = {"suffix": " t"},
            gauge = {
                'axis': {
                    "range": [0, 4e6],
                    "tickmode": "array", 
                    "tickvals": [
                        0,
                        0.5e6,
                        1e6,
                        1.5e6,
                        2e6,
                        2.5e6,
                        REFERENCE_VALUES["2021 GHG by transportation sector"],
                        3e6,
                        3.5e6,
                        # REFERENCE_VALUES["2032 Annual GHG by RTM"],
                        4e6,
                        ], 
                    "ticktext":[
                        '0',
                        '0.5M',
                        '1M',
                        '1.5M',
                        '2M',
                        '2.5M',
                        "<span style='color:{}'>     2.76M t <br>     (GPC Reporting)</span>".format(thresholdColor),
                        '3.0M',
                        '3.5M',
                        # "<span style='color:{}'><br><br>3.56M t (2032 RTM)</span>".format(thresholdColor2),
                        '4M'
                    ],
                    "tickangle":0
                },
                'bar': {'color': "rgb(47, 99, 173)"},
                # 'steps': [
                #     {'range': [updated_df[item].min()/ 1000 * 333, updated_df[item].max()/ 1000 * 333], 'color': "rgba(47, 99, 173, 0.5)"},
                # ],
                'threshold': {
                    'line': {
                        'color': thresholdColor, 
                        'width': 2
                    }, 
                    'thickness': 1, 
                    'value': REFERENCE_VALUES["2021 GHG by transportation sector"]
                },
                'steps': [
                    {'range': [updated_df[item11].min() / 1000 * 333, updated_df[item11].max() / 1000 * 333], 'color': "rgba(47, 99, 173, 0.5)"},
                ],
            },
        ),
        row=1,
        col=4
    )
    
    figure = fig.update_layout(
        title="<span style='font-weight:bold; font-size:1.5vw'>Annual Transportation GHG Emissions in City (Mega Tonnes)</span>",
        template="ggplot2",
        font_family="Times New Roman",
        margin=dict(l=20, r=90, t=90, b=40),
        height=400,
        showlegend=True,
        legend_traceorder="reversed",
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation="h"
        )
    )
    
    return figure

app.callback(
    Output("Net per person GHG emissions are zero2-graph", "figure"),
    [Input(UNCERTAINTIES[7] + "-dropdown", 'value'), Input("item_range_list", "data")]
)(graph_GHG2)

def graph_ATShare(filtered_data):
    updated_df = pd.DataFrame(filtered_data)
    item = "Active & Transit share in City"
    fig = make_subplots(
        rows=1,
        cols=4,
        specs=[
            [{"colspan": 3}, None, None, {"colspan": 1, "type": "indicator"}],
        ],
        horizontal_spacing = 0.05,
    )
    
    figure = fig.add_trace(
        go.Box(
            x=updated_df[item],
            hoverinfo=['x'],
            name="Selected Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item],
            hoverinfo=['x'],
            name="All Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.update_xaxes(tickformat=".1%", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
    if (sum(updated_df[item]) / len(updated_df[item])) < REFERENCE_VALUES[item]:
        thresholdColor = "rgba(240, 88, 83, 1)"
    else:
        thresholdColor = "rgba(42, 145, 52, 1)"
        
    figure = fig.add_trace(
        go.Indicator(
            mode="number+gauge+delta",
            value=(sum(updated_df[item]) / len(updated_df[item])),
            delta={'reference': REFERENCE_VALUES[item], "valueformat": ".1%"},
            number = {"valueformat": ".1%"},
            gauge = {
                'axis': {"range": [0, 0.40], 
                         "tickmode": "array", 
                         "tickvals": [0,.05,.10,.15,.20,.228,.25,.30,0.35,0.40], 
                         "ticktext":['0%','5%','10%','15%','20%',"<span style='color:{}'>22.8% (2015 T&A Share)<br> </span>".format(thresholdColor),'25%','30%','35%','40%'],
                         "tickangle":0
                },
                'bar': {'color': "rgb(47, 99, 173)"},
                'threshold': {'line': {'color': thresholdColor, 'width': 2}, 'thickness': 1, 'value': REFERENCE_VALUES[item]},
                'steps': [
                    {'range': [updated_df[item].min(), updated_df[item].max()], 'color': "rgba(47, 99, 173, 0.5)"},
                ],
            },
        ),
        row=1,
        col=4
    )
    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Roman",
        margin=dict(l=40, r=60, t=40, b=40),
        height=400,
        barmode='overlay',
        showlegend=True,
        legend_traceorder="reversed",
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation='h'
        )
    )

    return figure

app.callback(
    Output("50% Mode Share by Transit and Active Modes-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_ATShare)

def graph_ATShare2(filtered_data):
    updated_df = pd.DataFrame(filtered_data)
    fig = go.Figure()
    figure = fig.add_trace(
        go.Bar(
            y=["Selected<br>Combinations", "Actual Boardings<br>from 2015"],
            x=[
                sum(updated_df["Daily Bus boardings"]) / len(updated_df["Daily Bus boardings"]),
                REFERENCE_VALUES["Daily Bus boardings"],
            ],
            marker=dict(
                color = "rgba(47, 99, 173, 0.6)",
                line = dict(
                    color = "rgba(47, 99, 173, 1)", width=3
                )
            ),
            orientation='h',
            name="Bus"
        )
    )
    figure = fig.add_trace(
        go.Bar(
            y=["Selected<br>Combinations", "Actual Boardings<br>from 2015"],
            x=[
                sum(updated_df["Daily LRT boardings"]) / len(updated_df["Daily LRT boardings"]),
                REFERENCE_VALUES["Daily LRT boardings"]
            ],
            marker=dict(
                color = "rgba(62, 162, 218, 0.6)",
                line = dict(
                    color = "rgba(62, 162, 218, 1)", width=3
                )
            ),
            orientation='h',
            name="LRT",
        )
    ) 
    figure = fig.add_annotation(
        x=sum(updated_df["Daily LRT boardings"]) / len(updated_df["Daily LRT boardings"]) + sum(updated_df["Daily Bus boardings"]) / len(updated_df["Daily Bus boardings"]) + 30000,
        y="Selected<br>Combinations",
        xref="x",
        yref="y",
        text=human_format(sum(updated_df["Daily LRT boardings"]) / len(updated_df["Daily LRT boardings"]) + sum(updated_df["Daily Bus boardings"]) / len(updated_df["Daily Bus boardings"]), '%.0f%s'),
        showarrow=False,
        align="center",
    )
    
    figure = fig.add_annotation(
        x=REFERENCE_VALUES["Daily LRT boardings"] + REFERENCE_VALUES["Daily Bus boardings"] + 30000,
        y="Actual Boardings<br>from 2015",
        xref="x",
        yref="y",
        text=human_format(REFERENCE_VALUES["Daily LRT boardings"] + REFERENCE_VALUES["Daily Bus boardings"], '%.0f%s'),
        showarrow=False,
        align="right",
    )
    
    figure = fig.add_annotation(
        x=sum(updated_df["Daily Bus boardings"]) / len(updated_df["Daily Bus boardings"]) / 2,
        y="Selected<br>Combinations",
        xref="x",
        yref="y",
        text=human_format(sum(updated_df["Daily Bus boardings"]) / len(updated_df["Daily Bus boardings"]), '%.0f%s'),
        showarrow=False,
        align="center",
    )
    
    figure = fig.add_annotation(
        x=(sum(updated_df["Daily LRT boardings"]) / len(updated_df["Daily LRT boardings"])) / 2 + sum(updated_df["Daily Bus boardings"]) / len(updated_df["Daily Bus boardings"]),
        y="Selected<br>Combinations",
        xref="x",
        yref="y",
        text=human_format((sum(updated_df["Daily LRT boardings"]) / len(updated_df["Daily LRT boardings"])), '%.0f%s'),
        showarrow=False,
        align="center",
    )
    
    figure = fig.add_annotation(
        x=REFERENCE_VALUES["Daily Bus boardings"] / 2,
        y="Actual Boardings<br>from 2015",
        xref="x",
        yref="y",
        text=human_format(REFERENCE_VALUES["Daily Bus boardings"], '%.0f%s'),
        showarrow=False,
        align="right",
    )
    
    figure = fig.add_annotation(
        x=REFERENCE_VALUES["Daily LRT boardings"] / 2 + REFERENCE_VALUES["Daily Bus boardings"],
        y="Actual Boardings<br>from 2015",
        xref="x",
        yref="y",
        text=human_format(REFERENCE_VALUES["Daily LRT boardings"], '%.0f%s'),
        showarrow=False,
        align="right",
    )
    
    figure = fig.update_xaxes(range=[0, (df["Daily LRT boardings"] + df["Daily Bus boardings"]).max()], tickformat = ".3s", title_text = "# of Passengers", showline=True, linewidth=2, linecolor='black', mirror=True)
    figure = fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)  
    
    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Roman",
        title="<span style='font-weight:bold; font-size:1.5vw'>Daily Transit Boardings</span>",
        margin=dict(l=20, r=20, t=90, b=20),
        height=400,
        barmode='stack',
        showlegend=True,
        bargap=0.5,
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation='h',
            traceorder ='normal'
        )
    )
    
    return figure

app.callback(
    Output("50% Mode Share by Transit and Active Modes2-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_ATShare2)

def graph_ATShare3(filtered_data):
    # updated_df = pd.DataFrame(filtered_data)
    # item11 = "Transit share in City"
    # item14 = "Active share in City"
    # fig = make_subplots(
    #     rows=1,
    #     cols=2,
    #     specs=[
    #         [{"rowspan": 1, "colspan": 1}, {"rowspan": 1, "colspan": 1}],
    #     ],
    #     horizontal_spacing = 0.05,
    # )
    # fig11 = ff.create_distplot(
    #     hist_data=[
    #         df[item11],
    #         updated_df[item11]
    #     ],
    #     group_labels=["Total", "Selected"],
    #     bin_size=((updated_df[item11].max() - updated_df[item11].min()) / math.ceil(math.sqrt(updated_df.shape[0])))*0.7,
    #     show_rug=False,
    #     histnorm="probability",
    #     curve_type="normal",
    # )
    # figure = fig.add_trace(go.Histogram(fig11['data'][0],
    #                        marker_color=total_color,
    #                        showlegend=False
    #                       ), row=1, col=1)

    # figure = fig.add_trace(go.Histogram(fig11['data'][1],
    #                        marker_color=selected_color,
    #                        showlegend=False
    #                       ), row=1, col=1)

    # figure = fig.add_trace(go.Scatter(fig11['data'][2],
    #                      line=dict(color='rgba(240, 88, 83, 1)', width=3),
    #                      showlegend=False
    #                     ), row=1, col=1)

    # figure = fig.add_trace(go.Scatter(fig11['data'][3],
    #                      line=dict(color='rgba(47, 99, 173, 1)', width=3),
    #                      showlegend=False
    #                     ), row=1, col=1)
    
    # figure = fig.add_vline(
    #     x = REFERENCE_VALUES[item11], 
    #     annotation_text="2015 HH Travel Survey: <span style='font-weight:bold'>{0:.2%}</span>".format(REFERENCE_VALUES[item11]),  
    #     annotation_position="top right", 
    #     line_dash="dot", 
    #     line_color="black", 
    #     line_width=5, 
    #     row=1, 
    #     col=1
    # ),
    
    # figure = fig.add_annotation(
    #     showarrow = False,
    #     text = "<span style='font-weight:bold; font-size:1.5vw'>Transit Mode Share in City</span>",
    #     x = 0.225,
    #     xanchor = 'center',
    #     xref = 'paper',
    #     y = 1.15,
    #     yanchor = 'bottom',
    #     yref = 'paper',
    # ),
    
    # figure = fig.update_xaxes(tickformat=".1%", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    # figure = fig.update_yaxes(title_text="Probability", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
    # fig14 = ff.create_distplot(
    #     hist_data=[
    #         df[item14],
    #         updated_df[item14]
    #     ],
    #     group_labels=["Total", "Selected"],
    #     bin_size=((updated_df[item14].max() - updated_df[item14].min()) / math.ceil(math.sqrt(updated_df.shape[0])))*0.7,
    #     show_rug=False,
    #     histnorm="probability",
    #     curve_type="normal",
    # )
    # figure = fig.add_trace(go.Histogram(fig14['data'][0],
    #                        marker_color=total_color,
    #                        name="All Policy, Lever and Uncertainty Combinations",
    #                        showlegend=True,
    #                       ), row=1, col=2)

    # figure = fig.add_trace(go.Histogram(fig14['data'][1],
    #                        marker_color=selected_color,
    #                        name="Selected Policy, Lever and Uncertainty Combinations",
    #                        showlegend=True,
    #                       ), row=1, col=2)

    # figure = fig.add_trace(go.Scatter(fig14['data'][2],
    #                      line=dict(color='rgba(240, 88, 83, 1)', width=3),
    #                      showlegend=False
    #                     ), row=1, col=2)

    # figure = fig.add_trace(go.Scatter(fig14['data'][3],
    #                      line=dict(color='rgba(47, 99, 173, 1)', width=3),
    #                      showlegend=False
    #                     ), row=1, col=2)
    
    # figure = fig.add_vline(
    #     x = REFERENCE_VALUES[item14], 
    #     annotation_text="2015 HH Travel Survey: <span style='font-weight:bold'>{0:.2%}</span>".format(REFERENCE_VALUES[item14]), 
    #     annotation_position="top right", 
    #     line_dash="dot", 
    #     line_color="black", 
    #     line_width=5, 
    #     row=1, 
    #     col=2
    # )
    
    # figure = fig.add_annotation(
    #     showarrow = False,
    #     text = "<span style='font-weight:bold; font-size:1.5vw'>Active Mode Share in City</span>",
    #     x = 0.775,
    #     xanchor = 'center',
    #     xref = 'paper',
    #     y = 1.15,
    #     yanchor = 'bottom',
    #     yref = 'paper',
    # ),
    
    # figure = fig.update_xaxes(tickformat=".1%", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)
    # figure = fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)    

    # figure = fig.update_layout(
    #     template="seaborn",
    #     font_family="Times New Roman",
    #     margin=dict(l=20, r=20, t=90, b=40),
    #     height=400,
    #     barmode='overlay',
    #     showlegend=True,
    #     bargap=0.1,
    #     legend=dict(
    #         bgcolor="rgba(234,234,242,0.8)",
    #         bordercolor="Black",
    #         borderwidth=2,
    #         orientation='h'
    #     )
    # )
    updated_df = pd.DataFrame(filtered_data)

    item11 = "Transit share in City"
    item14 = "Active share in City"
    
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[
            [{"rowspan": 1, "colspan": 1}, {"rowspan": 1, "colspan": 1}],
        ],
        horizontal_spacing = 0.05,
    )

    figure = fig.add_trace(
        go.Box(
            x=updated_df[item11],
            hoverinfo=['x'],
            name="Selected Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item11],
            hoverinfo=['x'],
            name="All Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.add_annotation(
        showarrow = False,
        text = "<span style='font-weight:bold; font-size:1.25vw'>Transit mode Share in City</span>",
        x = 0.225,
        xanchor = 'center',
        xref = 'paper',
        y = 1.15,
        yanchor = 'bottom',
        yref = 'paper',
    ),
    figure = fig.add_annotation(
        x=sum(updated_df[item11]) / len(updated_df[item11]),
        xref="x1",
        y = 0.4,
        yanchor = 'bottom',
        yref = 'paper',
        text= "Selected average:<span style='font-weight:bold'> {0:.1%} </span>transit share".format((sum(updated_df[item11]) / len(updated_df[item11]))),
        showarrow=False,
    )
    
    figure = fig.update_xaxes(tickformat=".1%", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
    figure = fig.add_trace(
        go.Box(
            x=updated_df[item14],
            showlegend=False,
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=2
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item14],
            showlegend=False,
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=2
    ) 
    figure = fig.add_annotation(
        showarrow = False,
        text = "<span style='font-weight:bold; font-size:1.25vw'>Active Mode Share in City</span>",
        x = 0.775,
        xanchor = 'center',
        xref = 'paper',
        y = 1.15,
        yanchor = 'bottom',
        yref = 'paper',
    ),
    figure = fig.add_annotation(
        x=sum(updated_df[item14]) / len(updated_df[item14]),
        xref="x2",
        y = 0.4,
        yanchor = 'bottom',
        yref = 'paper',
        text= "Selected average:<span style='font-weight:bold'> {0:.1%} </span>active share".format(sum(updated_df[item14]) / len(updated_df[item14])),
        showarrow=False,
    )
    figure = fig.add_vline(
        x = REFERENCE_VALUES[item11], 
        annotation_text="2015 Transit Share: <span style='font-weight:bold'>{0:.2%}</span>".format(REFERENCE_VALUES[item11]),  
        annotation_position="top right", 
        line_dash="dash", 
        line_color="black", 
        line_width=1, 
        row=1, 
        col=1
    ),
    figure = fig.add_vline(
        x = REFERENCE_VALUES[item14], 
        annotation_text="2015 Active Share: <span style='font-weight:bold'>{0:.2%}</span>".format(REFERENCE_VALUES[item14]), 
        annotation_position="top right", 
        line_dash="dash", 
        line_color="black", 
        line_width=1, 
        row=1, 
        col=2
    )

    
    figure = fig.update_xaxes(tickformat=".1%", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)    

    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Romanl",
        margin=dict(l=20, r=20, t=90, b=40),
        height=400,
        barmode='overlay',
        showlegend=True,
        legend_traceorder="reversed",
        bargap=0.1,
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation='h'
        )
    )

    return figure

app.callback(
    Output("50% Mode Share by Transit and Active Modes3-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_ATShare3)


def graph_15Mins(filtered_data):
    updated_df = pd.DataFrame(filtered_data)
    fig = go.Figure()
    figure = fig.add_trace(
        go.Bar(
            y=["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"],
            x=[
                sum(updated_df["a"]) / len(updated_df["a"]),
                sum(updated_df["b"]) / len(updated_df["b"]),
                sum(updated_df["c"]) / len(updated_df["c"]),
                sum(updated_df["d"]) / len(updated_df["d"]),
                sum(updated_df["e"]) / len(updated_df["e"]),
                sum(updated_df["f"]) / len(updated_df["f"]),
                sum(updated_df["g"]) / len(updated_df["g"]),
                sum(updated_df["h"]) / len(updated_df["h"]),
                sum(updated_df["i"]) / len(updated_df["i"]),
                sum(updated_df["j"]) / len(updated_df["j"]),
                sum(updated_df["k"]) / len(updated_df["k"]),
                sum(updated_df["l"]) / len(updated_df["l"]),
                sum(updated_df["m"]) / len(updated_df["m"]),
                sum(updated_df["n"]) / len(updated_df["n"]),
                sum(updated_df["o"]) / len(updated_df["o"]),
                sum(updated_df["p"]) / len(updated_df["p"]),
            ],
            marker=dict(
                color=["rgba(62, 162, 218, 0.6)", 
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",],
                line = dict(
                    color=["rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", ], 
                    width=3
                )
            ),
             
            orientation='h',
            showlegend=False,
        )
    )  
    
    for name, col in zip(["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]):
        figure = fig.add_annotation(
            y=name,
            x=sum(updated_df[col]) / len(updated_df[col]) + 0.02,
            xref="x",
            yref="y",
            text="{0:.0%}".format(sum(updated_df[col]) / len(updated_df[col])),
            showarrow=False,
            align="center",
        )
        
    figure = fig.add_trace(
        go.Scatter(
            x=[0.6397,  0.5913, 0.6633, 0.4630, 0.6258, 0.6938, 0.6633, 0.6890, 0.5803, 0.6952, 0.5986, 0.6244, 0.6571, 0.6804, 0.6090, 0.6447],
            y=["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"],
            mode="markers",
            name="2015 Actual<br>Share",
            marker=dict(
                size=20, 
                symbol="line-ns",
                line_width=2,
                line_color="rgba(42, 145, 52, 1)",
            )
        )
    )
     
    figure = fig.update_xaxes(tickformat=".0%", showline=True, linewidth=2, linecolor='black', mirror=True, range= [0.3, 1])
    figure = fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)  
    
    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Roman",
        title="<span style='font-weight:bold; font-size:1.5vw'>(2 Million Target: 15 Minute Districts that Allow People Easily Complete Their Daily Needs)</span>",
        margin=dict(l=20, r=20, t=90, b=20),
        height=700,
        showlegend=True,
        bargap=0.2,
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2
        )
    )
    
    return figure
    
app.callback(
    Output("15 Minutes Districts-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_15Mins)

def graph_15Mins2(filtered_data):
    updated_df = pd.DataFrame(filtered_data)
    fig = go.Figure()
    figure = fig.add_trace(
        go.Bar(
            y=["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"],
            x=[
                sum(updated_df["118 Avenue-AT"]) / len(updated_df["118 Avenue-AT"]) + 0.0630,
                sum(updated_df["Central-AT"]) / len(updated_df["Central-AT"]) + 0.0044,
                sum(updated_df["Ellerslie-AT"]) / len(updated_df["Ellerslie-AT"]) + 0.0062,
                sum(updated_df["Horse Hills-AT"]) / len(updated_df["Horse Hills-AT"]) + 0.048,
                sum(updated_df["Jasper Place-AT"]) / len(updated_df["Jasper Place-AT"]) +0.0688,
                sum(updated_df["Mill Woods and Meadows-AT"]) / len(updated_df["Mill Woods and Meadows-AT"]) + 0.0001,
                sum(updated_df["Northeast-AT"]) / len(updated_df["Northeast-AT"]) + 0.0237,
                sum(updated_df["Northwest-AT"]) / len(updated_df["Northwest-AT"]) -0.0054 ,
                sum(updated_df["Rabbit Hill-AT"]) / len(updated_df["Rabbit Hill-AT"]) ,
                sum(updated_df["Region-AT"]) / len(updated_df["Region-AT"]) - 0.002 ,
                sum(updated_df["Scona-AT"]) / len(updated_df["Scona-AT"]) + 0.0798,
                sum(updated_df["Southeast-AT"]) / len(updated_df["Southeast-AT"]) + 0.0741,
                sum(updated_df["Southwest-AT"]) / len(updated_df["Southwest-AT"]) + 0.0023,
                sum(updated_df["West Edmonton-AT"]) / len(updated_df["West Edmonton-AT"]) + 0.037,
                sum(updated_df["West Henday-AT"]) / len(updated_df["West Henday-AT"]) + 0.0002,
                sum(updated_df["Whitemud-AT"]) / len(updated_df["Whitemud-AT"]) + 0.0069,
            ],

            marker=dict(
                color=["rgba(62, 162, 218, 0.6)", 
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",],
                line = dict(
                    color=["rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", ], 
                    width=3
                )
            ),
            orientation='h',
            showlegend=False,
        )
    )  
    
    for error , col in zip([0.0630, 0.0044, 0.0062, 0.048, 0.0688, 0.0001, 0.0237, -0.0054, 0, -0.002, 0.0798, 0.0741, 0.0023, 0.037, 0.0002, 0.0069], ["118 Avenue-AT", "Central-AT", "Ellerslie-AT", "Horse Hills-AT", "Jasper Place-AT", "Mill Woods and Meadows-AT", "Northeast-AT", "Northwest-AT", "Rabbit Hill-AT", "Region-AT", "Scona-AT", "Southeast-AT", "Southwest-AT", "West Edmonton-AT", "West Henday-AT", "Whitemud-AT"]):
        figure = fig.add_annotation(
            y=col[0:-3],
            x=sum(updated_df[col]) / len(updated_df[col]) + error + 0.01,
            xref="x",
            yref="y",
            text="{0:.0%}".format(sum(updated_df[col]) / len(updated_df[col]) + error),
            showarrow=False,
            align="center",
        )
        
    figure = fig.add_trace(
        go.Scatter(
            x=[0.272, 0.386, 0.148, 0.114, 0.207, 0.163, 0.195, 0.169, 0.0, 0.131, 0.401, 0.210, 0.158, 0.195, 0.138, 0.188], #HH Travel Survey
            #x=[0.187385, 0.459663, 0.054175, 0.01682, 0.082348, 0.073302, 0.065061, 0.068663, 0.078767, 0.151535, 0.39571, 0.083857, 0.055769, 0.165962, 0.170382, 0.146047], #RTM Model 2015
            y=["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"],
            mode="markers",
            name="2015 Actual<br>Share",
            marker=dict(
                size=20, 
                symbol="line-ns",
                line_width=2,
                line_color="rgba(42, 145, 52, 1)",
            )
        )
    )
     
    figure = fig.update_xaxes(tickformat=".0%", showline=True, linewidth=2, linecolor='black', mirror=True)
    figure = fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)  
    
    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Roman",
        title="<span style='font-weight:bold; font-size:1.5vw'>Transit & Active Mode Share by Planning District</span>",
        margin=dict(l=20, r=20, t=90, b=20),
        height=700,
        showlegend=True,
        bargap=0.2,
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
        )
    )
    
    return figure

app.callback(
    Output("15 Minutes Districts2-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_15Mins2)

def graph_15Mins3(filtered_data):
    updated_df = pd.DataFrame(filtered_data)
    fig = go.Figure()
    figure = fig.add_trace(
        go.Bar(
            y=["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"],
            x=[
                sum(updated_df["1CarOwn"]) / len(updated_df["1CarOwn"]),
                sum(updated_df["2CarOwn"]) / len(updated_df["2CarOwn"]),
                sum(updated_df["3CarOwn"]) / len(updated_df["3CarOwn"]),
                sum(updated_df["4CarOwn"]) / len(updated_df["4CarOwn"]),
                sum(updated_df["5CarOwn"]) / len(updated_df["5CarOwn"]),
                sum(updated_df["6CarOwn"]) / len(updated_df["6CarOwn"]),
                sum(updated_df["7CarOwn"]) / len(updated_df["7CarOwn"]),
                sum(updated_df["8CarOwn"]) / len(updated_df["8CarOwn"]),
                sum(updated_df["9CarOwn"]) / len(updated_df["9CarOwn"]),
                sum(updated_df["10CarOwn"]) / len(updated_df["10CarOwn"]),
                sum(updated_df["11CarOwn"]) / len(updated_df["11CarOwn"]),
                sum(updated_df["12CarOwn"]) / len(updated_df["12CarOwn"]),
                sum(updated_df["13CarOwn"]) / len(updated_df["13CarOwn"]),
                sum(updated_df["14CarOwn"]) / len(updated_df["14CarOwn"]),
                sum(updated_df["15CarOwn"]) / len(updated_df["15CarOwn"]),
                sum(updated_df["16CarOwn"]) / len(updated_df["16CarOwn"]),
            ],
            marker=dict(
                color=["rgba(62, 162, 218, 0.6)", 
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",
                       "rgba(62, 162, 218, 0.6)",
                       "rgba(47, 99, 173, 0.6)",],
                line = dict(
                    color=["rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", 
                       "rgba(62, 162, 218, 1)", 
                       "rgba(47, 99, 173, 1)", ], 
                    width=3
                )
            ),
             
            orientation='h',
            showlegend=False,
        )
    )  
    
    for name, col in zip(["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"], ["1CarOwn", "2CarOwn", "3CarOwn", "4CarOwn", "5CarOwn", "6CarOwn", "7CarOwn", "8CarOwn", "9CarOwn", "10CarOwn", "11CarOwn", "12CarOwn", "13CarOwn", "14CarOwn", "15CarOwn", "16CarOwn"]):
        figure = fig.add_annotation(
            y=name,
            x=sum(updated_df[col]) / len(updated_df[col]) + 0.04,
            xref="x",
            yref="y",
            text="{0:.1f}".format(sum(updated_df[col]) / len(updated_df[col])),
            showarrow=False,
            align="center",
        )
        
    figure = fig.add_trace(
        go.Scatter(
            # x=[1.476412,	1.078545,	2.033148,	2.285449,	1.612799,	1.925626,	1.802128,	1.820528,	3.298701,	2.201558,	1.304644,	1.620088,	1.946711,	1.786863,	2.011941,	1.828256], # 2015 Base RTM Model
            x = [1.379789,	0.984428,	1.90913,	2.070396,	1.503618,	1.854349,	1.705832,	1.735316,	2.270073,	2.155961,	1.228884,	1.48844,	1.806817,	1.652235,	1.947918,	1.683774], # 2032 Base RTM Model
            y=["118 Avenue", "Central", "Ellerslie", "Horse Hills", "Jasper Place", "Mill Woods and Meadows", "Northeast", "Northwest", "Rabbit Hill", "Region", "Scona", "Southeast", "Southwest", "West Edmonton", "West Henday", "Whitemud"],
            mode="markers",
            name="2015 Actual<br>Share",
            marker=dict(
                size=20, 
                symbol="line-ns",
                line_width=2,
                line_color="rgba(42, 145, 52, 1)",
            )
        )
    )
     
    figure = fig.update_xaxes(tickformat=".1f", showline=True, linewidth=2, linecolor='black', mirror=True)
    figure = fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)  
    
    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Roman",
        title="<span style='font-weight:bold; font-size:1.5vw'>Average Number of Cars Owned by Household in each Planning District</span>",
        margin=dict(l=20, r=20, t=90, b=20),
        height=700,
        showlegend=True,
        bargap=0.2,
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2
        )
    )
    
    return figure
    
app.callback(
    Output("15 Minutes Districts3-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_15Mins3)


def graph_15Mins4(filtered_data, filtered_BCM_df):
    updated_df = pd.DataFrame(filtered_data)
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    item = "Total vehicle distance (km) (Base)"
    fig = make_subplots(
        rows=1,
        cols=4,
        specs=[
            [{"rowspan": 1, "colspan": 3}, None, None, {"colspan": 1, "type": "indicator"}],
        ],
        # subplot_titles=(
        #     "Annual Vehicle Kilometer (Kms) in City<br><span style='font-size:0.8em;color:gray'>Kms Driven per Vehicle per Year</span>",
        #     "Average Vehicle Kilometer (Kms) in City<br><span style='font-size:0.8em;color:gray'>Kms Driven per Vehicle per Year</span>",
        # ),
        horizontal_spacing = 0.05,
    )
    
    figure = fig.add_trace(
        go.Box(
            x=updated_df[item] * 333 / (updated_BCM_df["Total Population in the City"].values[0]) * 2.43 / 1.63, # VKT per Car = VKT per person * Average HH size / Average car ownership per HH
            hoverinfo=['x'],
            name="Selected Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item] * 333 / (updated_BCM_df["Total Population in the City"].values[0]) * 2.43 / 1.63,
            hoverinfo=['x'],
            name="All Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.update_xaxes(tickformat=".3s",showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
        
    figure = fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            number = {"suffix": " km"},
            value=round((sum(updated_df[item]) / len(updated_df[item])) * 333 / (updated_BCM_df["Total Population in the City"].values[0])*  2.43 / 1.63, -2),
            gauge = {
                'axis': {
                    "range": [0, df[item].max() * 333 / (updated_BCM_df["Total Population in the City"].values[0]) * 2.43 / 1.63], 
                    "tickmode": "array", 
                    "tickangle":0,
                    "tickvals": [0, 2000, 4000, 6000, 8000, 10000, 12000, df[item].max() * 333 / (updated_BCM_df["Total Population in the City"].values[0]) * 2.43 / 1.63], 
                    "ticktext":['0', '2k', '4k', '6k', '8k', '10k', '12k', '13.4k'],
                },
                'bar': {'color': "rgb(47, 99, 173)"},
                'steps': [
                    {'range': [updated_df[item].min()* 333 / (updated_BCM_df["Total Population in the City"].values[0])*  2.43 / 1.63, updated_df[item].max()* 333 / (updated_BCM_df["Total Population in the City"].values[0])*  2.43 / 1.63], 'color': "rgba(47, 99, 173, 0.5)"},
                ],
            },
        ),
        row=1,
        col=4
    )
    figure = fig.update_layout(
        title= "<span style='font-weight:bold; font-size:1.5vw'>Average Annual Kilometer per Vehicle in City (Kms)</span>",
        template="ggplot2",
        font_family="Times New Roman",
        margin=dict(l=40, r=60, t=90, b=40),
        height=400,
        barmode='overlay',
        showlegend=True,
        legend_traceorder="reversed",
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation='h'
        )
    )

    return figure

app.callback(
    Output("15 Minutes Districts4-graph", "figure"),
    [Input("item_range_list", "data"), Input("BCM_range_list", "data")]
)(graph_15Mins4)

def graph_15Mins5(filtered_data):
    updated_df = pd.DataFrame(filtered_data)
    item = "Total vehicle distance (km) (Base)"
    fig = make_subplots(
        rows=1,
        cols=4,
        specs=[
            [{"rowspan": 1, "colspan": 3}, None, None, {"colspan": 1, "type": "indicator"}],
        ],
        horizontal_spacing = 0.05,
    )
    
    figure = fig.add_trace(
        go.Box(
            x=updated_df[item] * 333,
            hoverinfo=['x'],
            name="Selected Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item] * 333,
            hoverinfo=['x'],
            name="All Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
        
    figure = fig.add_trace(
        go.Indicator(
            mode="number+gauge",
            number = {"suffix": " km"},
            value=round((sum(updated_df[item]) / len(updated_df[item])) * 333, -7),
            gauge = {
                'axis': {
                    "range": [0, df[item].max() * 333], 
                    "tickmode": "array", 
                    "tickangle":0,
                    "tickvals": [0, 2e9, 4e9, 6e9, 8e9, 10e9, df[item].max() * 333], 
                    "ticktext":['0', '2B', '4B', '6B', '8B', '10B', '11.4B'],
                },
                'bar': {'color': "rgb(47, 99, 173)"},
                'steps': [
                    {'range': [updated_df[item].min() * 333 , updated_df[item].max() * 333], 'color': "rgba(47, 99, 173, 0.5)"},
                ],
            },
        ),
        row=1,
        col=4
    )
    figure = fig.update_layout(
        title= "<span style='font-weight:bold; font-size:1.5vw'>Average Annual Kilometer in City (Kms)</span>",
        template="ggplot2",
        font_family="Times New Roman",
        margin=dict(l=40, r=60, t=90, b=40),
        height=400,
        barmode='overlay',
        showlegend=True,
        legend_traceorder="reversed",
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation='h'
        )
    )
    return figure

app.callback(
    Output("15 Minutes Districts5-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_15Mins5)

# def graph_15Mins6(filtered_data):
#     updated_df = pd.DataFrame(filtered_data)

#     item11 = "Time in cars per capita Overall"
#     item14 = "Time in transit per capita Overall"
    
#     fig = make_subplots(
#         rows=1,
#         cols=2,
#         specs=[
#             [{"rowspan": 1, "colspan": 1}, {"rowspan": 1, "colspan": 1}],
#         ],
#         horizontal_spacing = 0.05,
#     )

#     figure = fig.add_trace(
#         go.Box(
#             x=updated_df[item11],
#             hoverinfo=['x'],
#             name="Selected Policy, Lever and Uncertainty Combinations",
#             boxpoints='suspectedoutliers', # only suspected outliers
#             boxmean=True,
#             marker=dict(
#                 color='rgb(229, 149, 0)',
#                 outliercolor='rgba(229, 149, 0)',
#                 line=dict(
#                     outliercolor='rgba(229, 149, 0)',
#                     outlierwidth=2)),
#             line_color='rgb(47, 99, 173)'
#         ),
#         row=1,
#         col=1
#     )
#     figure = fig.add_trace(
#         go.Box(
#             x=df[item11],
#             hoverinfo=['x'],
#             name="All Policy, Lever and Uncertainty Combinations",
#             boxpoints='suspectedoutliers', # only suspected outliers
#             boxmean=True,
#             marker=dict(
#                 color='rgb(229, 149, 0)',
#                 outliercolor='rgba(229, 149, 0)',
#                 line=dict(
#                     outliercolor='rgba(229, 149, 0)',
#                     outlierwidth=2)),
#             line_color='rgb(240, 88, 83)'
#         ),
#         row=1,
#         col=1
#     ) 
#     figure = fig.add_annotation(
#         showarrow = False,
#         text = "<span style='font-weight:bold; font-size:1.25vw'>Daily Time Spent in Cars per Person (Minutes)</span>",
#         x = 0.235,
#         xanchor = 'center',
#         xref = 'paper',
#         y = 1.15,
#         yanchor = 'bottom',
#         yref = 'paper',
#     ),
#     figure = fig.add_annotation(
#         x=sum(updated_df[item11]) / len(updated_df[item11]),
#         xref="x1",
#         y = 0.4,
#         yanchor = 'bottom',
#         yref = 'paper',
#         text= "Selected average:<span style='font-weight:bold'> {0:.1f} </span>minutes".format((sum(updated_df[item11]) / len(updated_df[item11]))),
#         showarrow=False,
#     )
    
#     figure = fig.update_xaxes(tickformat=".1f", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
#     figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
#     figure = fig.add_trace(
#         go.Box(
#             x=updated_df[item14],
#             showlegend=False,
#             hoverinfo=['x'],
#             boxpoints='suspectedoutliers', # only suspected outliers
#             boxmean=True,
#             marker=dict(
#                 color='rgb(229, 149, 0)',
#                 outliercolor='rgba(229, 149, 0)',
#                 line=dict(
#                     outliercolor='rgba(229, 149, 0)',
#                     outlierwidth=2)),
#             line_color='rgb(47, 99, 173)'
#         ),
#         row=1,
#         col=2
#     )
#     figure = fig.add_trace(
#         go.Box(
#             x=df[item14],
#             showlegend=False,
#             hoverinfo=['x'],
#             boxpoints='suspectedoutliers', # only suspected outliers
#             boxmean=True,
#             marker=dict(
#                 color='rgb(229, 149, 0)',
#                 outliercolor='rgba(229, 149, 0)',
#                 line=dict(
#                     outliercolor='rgba(229, 149, 0)',
#                     outlierwidth=2)),
#             line_color='rgb(240, 88, 83)'
#         ),
#         row=1,
#         col=2
#     ) 
#     figure = fig.add_annotation(
#         showarrow = False,
#         text = "<span style='font-weight:bold; font-size:1.25vw'>Daily Time Spent in Transit per Person (Minutes)</span>",
#         x = 0.755,
#         xanchor = 'center',
#         xref = 'paper',
#         y = 1.15,
#         yanchor = 'bottom',
#         yref = 'paper',
#     ),
#     figure = fig.add_annotation(
#         x=sum(updated_df[item14]) / len(updated_df[item14]),
#         xref="x2",
#         y = 0.4,
#         yanchor = 'bottom',
#         yref = 'paper',
#         text= "Selected average:<span style='font-weight:bold'> {0:.1f} </span>minutes".format((sum(updated_df[item14]) / len(updated_df[item14]))),
#         showarrow=False,
#     )
    


    
#     figure = fig.update_xaxes(tickformat=".1f", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)
#     figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)    

#     figure = fig.update_layout(
#         template="ggplot2",
#         font_family="Times New Romanl",
#         margin=dict(l=20, r=20, t=90, b=40),
#         height=400,
#         barmode='overlay',
#         showlegend=True,
#         legend_traceorder="reversed",
#         bargap=0.1,
#         legend=dict(
#             bgcolor="rgba(237,237,237,0.8)",
#             bordercolor="Black",
#             borderwidth=2,
#             orientation='h'
#         )
#     )

#     return figure

# app.callback(
#     Output("15 Minutes Districts6-graph", "figure"),
#     [Input("item_range_list", "data")]
# )(graph_15Mins6)

def graph_15Mins7(filtered_data):
    updated_df = pd.DataFrame(filtered_data)

    item11 = "Citywide-Carownership"
    item14 = "Citywide-Trips"
    
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[
            [{"rowspan": 1, "colspan": 1}, {"rowspan": 1, "colspan": 1}],
        ],
        horizontal_spacing = 0.05,
    )

    figure = fig.add_trace(
        go.Box(
            x=updated_df[item11],
            hoverinfo=['x'],
            name="Selected Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=1
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item11],
            hoverinfo=['x'],
            name="All Policy, Lever and Uncertainty Combinations",
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=1
    ) 
    figure = fig.add_annotation(
        showarrow = False,
        text = "<span style='font-weight:bold; font-size:1.25vw'>Average Car Ownership by Housholds in City</span>",
        x = 0.225,
        xanchor = 'center',
        xref = 'paper',
        y = 1.15,
        yanchor = 'bottom',
        yref = 'paper',
    ),
    figure = fig.add_annotation(
        x=sum(updated_df[item11]) / len(updated_df[item11]),
        xref="x1",
        y = 0.4,
        yanchor = 'bottom',
        yref = 'paper',
        text= "Selected average:<span style='font-weight:bold'> {0:.1f} </span>cars".format((sum(updated_df[item11]) / len(updated_df[item11]))),
        showarrow=False,
    )
    
    figure = fig.update_xaxes(tickformat=".1f", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=1)
    
    figure = fig.add_trace(
        go.Box(
            x=updated_df[item14],
            showlegend=False,
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(47, 99, 173)'
        ),
        row=1,
        col=2
    )
    figure = fig.add_trace(
        go.Box(
            x=df[item14],
            showlegend=False,
            hoverinfo=['x'],
            boxpoints='suspectedoutliers', # only suspected outliers
            boxmean=True,
            marker=dict(
                color='rgb(229, 149, 0)',
                outliercolor='rgba(229, 149, 0)',
                line=dict(
                    outliercolor='rgba(229, 149, 0)',
                    outlierwidth=2)),
            line_color='rgb(240, 88, 83)'
        ),
        row=1,
        col=2
    ) 
    figure = fig.add_annotation(
        showarrow = False,
        text = "<span style='font-weight:bold; font-size:1.25vw'>Total Number of Trips in City</span>",
        x = 0.775,
        xanchor = 'center',
        xref = 'paper',
        y = 1.15,
        yanchor = 'bottom',
        yref = 'paper',
    ),
    figure = fig.add_annotation(
        x=sum(updated_df[item14]) / len(updated_df[item14]),
        xref="x2",
        y = 0.4,
        yanchor = 'bottom',
        yref = 'paper',
        text= "Selected average:<span style='font-weight:bold'> {} </span>trips".format(human_format(sum(updated_df[item14]) / len(updated_df[item14]), '%.2f%s')),
        showarrow=False,
    )

    
    figure = fig.update_xaxes(tickformat=".3s", showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)
    figure = fig.update_yaxes(showticklabels=False, showline=True, linewidth=2, linecolor='black', mirror=True, row=1, col=2)    

    figure = fig.update_layout(
        template="ggplot2",
        font_family="Times New Romanl",
        margin=dict(l=20, r=20, t=90, b=40),
        height=400,
        barmode='overlay',
        showlegend=True,
        legend_traceorder="reversed",
        bargap=0.1,
        legend=dict(
            bgcolor="rgba(237,237,237,0.8)",
            bordercolor="Black",
            borderwidth=2,
            orientation='h'
        )
    )

    return figure

app.callback(
    Output("15 Minutes Districts7-graph", "figure"),
    [Input("item_range_list", "data")]
)(graph_15Mins7)


# def graph_RebuildableCity(filtered_BCM_df):
    
#     updated_BCM_df = pd.DataFrame(filtered_BCM_df)
#     item11 = "Total Number of Units in the City"
#     item13 = "Total Population in the City"
#     fig = make_subplots(
#         rows=1,
#         cols=4,
#         specs=[
#             [{"colspan": 2, "type": "indicator"}, None, {"colspan": 2, "type": "indicator"}, None],
#         ],
#     ) 
#     figure = fig.add_trace(
#         go.Indicator(
#             mode="number+delta",
#             title = {"text": "<span style='font-weight:bold; font-size:1.5vw'>Total Anticipated Dwelling Units in the City</span>"},
#             value=round(updated_BCM_df[item11].values[0], -3),
#             # delta={'reference': REFERENCE_VALUES[item11]},
#         ),
#         row=1,
#         col=1
#     )
    
#     figure = fig.add_trace(
#         go.Indicator(
#             mode="number+delta",
#             title = {"text": "<span style='font-weight:bold; font-size:1.5vw'>Total Anticipated Population in the City<br><span style='font-size:1.2vw;color:rgba(42, 145, 52, 1)'>Growth from 2021 Federal Census</span>"},
#             value=round(updated_BCM_df[item13].values[0], -3),
#             delta={'reference': REFERENCE_VALUES[item13]},
#         ),
#         row=1,
#         col=3
#     )
    
#     figure = fig.update_layout(
#         template="ggplot2",
#         font_family="Times New Roman",
#         margin=dict(l=20, r=20, t=80, b=40),
#         height=200,
#         barmode='overlay',
#         bargap=0.9,
#         showlegend=False
#     )
    
#     return figure

# app.callback(
#     Output("A Rebuildable City-graph", "figure"),
#     [Input("BCM_range_list", "data")]
# )(graph_RebuildableCity)


def graph_Unit(filtered_BCM_df):
    
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    item11 = "50% Net New Units will be added through Infill City wide"

    if updated_BCM_df[item11].values[0] < REFERENCE_VALUES[item11]:
        thresholdColor = "rgba(240, 88, 83, 1)"
    else:
        thresholdColor = "rgba(42, 145, 52, 1)"
        
    fig = go.Figure(go.Indicator(
        mode="number+gauge+delta",
        value=updated_BCM_df[item11].values[0],
        delta={'reference': REFERENCE_VALUES[item11], "valueformat": ".0%"},
        number = {"valueformat": ".0%"},
        gauge = {
            'shape': "bullet",
            'axis': {
                "range": [0, 0.385],
                "tickmode": "array",
                "tickvals": [0,.05,.10,.15,.20,.25,.30,0.35,0.385],
                "ticktext":['0%','5%','10%','15%','20%',
                            "25%<br>% of New Units added Through Infill<br>Average between 2016 and 2020",
                            '30%','35%',
                            "38.5%<br>Highest Result<br>by 2032",
                ],
                "tickangle":0,
            },
            'bar': {'color': "rgb(47, 99, 173)" , 'thickness': 0.6},
            'threshold': {'line': {'color': thresholdColor, 'width': 5}, 'thickness': 1, 'value': REFERENCE_VALUES[item11]},
            # 'steps': [
            #     {'range': (0, updated_BCM_df[item11].values[0]), 'color': "rgba(47, 99, 173, 0.3)"},
            # ],
        },
    ))
    
    fig.update_layout(
        template="ggplot2",
        # title="<span color:black'>Net New Units Percentage In Redeveloping Areas by 2032<br><span style='font-size:0.8em;color:gray'>Compare with the Net Infill Counts of the Last 5 years</span>",
        font_family="Times New Roman",
        margin=dict(l=30, r=30, t=30, b=60),
        height=200,
        barmode='overlay',
        bargap=0.9,
        showlegend=False
    )
    
    return fig

app.callback(
    Output("50% Net New Units will be added through Infill City wide-graph", "figure"),
    [Input("BCM_range_list", "data")]
)(graph_Unit)

def graph_Population(filtered_BCM_df):
    
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    item11 = "600k additional residents will be welcomed within redeveloping Area"
    if updated_BCM_df[item11].values[0] < REFERENCE_VALUES[item11]:
        thresholdColor = "rgba(240, 88, 83, 1)"
    else:
        thresholdColor = "rgba(42, 145, 52, 1)"
        
    fig = go.Figure(go.Indicator(
        mode="number+gauge",
        value=round(updated_BCM_df[item11].values[0], -3),
        #delta={'reference': REFERENCE_VALUES[item11]},
        gauge = {
            'shape': "bullet",
            'axis': {
                "range": [0, 111520],
                "tickmode": "array",
                "tickvals": [0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,111520],
                "ticktext":['0','10K','20K','30K','40K','50K','60K',
                            "70K",
                            '80K','90K','100K',
                            "111.5K<br>Highest Result<br>by 2032",
                ],
            },
            'bar': {'color': "rgb(47, 99, 173)" , 'thickness': 0.6},
            # 'threshold': {'line': {'color': thresholdColor, 'width': 5}, 'thickness': 1, 'value': REFERENCE_VALUES[item11]},
            # 'steps': [
            #     {'range': [0, (sum(updated_BCM_df[item11]) / len(updated_BCM_df[item11]))], 'color': "rgba(47, 99, 173, 0.3)"},
            # ],
        },
    ))
    
    fig.update_layout(
        template="ggplot2",
        # title="Population Growth in Redeveloping Areas by 2032<br><span style='font-size:0.8em;color:gray'></span>",
        font_family="Times New Roman",
        margin=dict(l=30, r=30, t=30, b=60),
        height=200,
        barmode='overlay',
        bargap=0.9,
        showlegend=False
    )
    
    return fig

app.callback(
    Output("600k additional residents will be welcomed within redeveloping Area-graph", "figure"),
    [Input("BCM_range_list", "data")]
)(graph_Population)


def graph_NodesCorridors(filtered_BCM_df):
    
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    item11 = "Nodes and Corridors support 50% of all employment in Edmonton"
    
    if updated_BCM_df[item11].values[0] < REFERENCE_VALUES[item11]:
        thresholdColor = "rgba(240, 88, 83, 1)"
    else:
        thresholdColor = "rgba(42, 145, 52, 1)"
        
    fig = go.Figure(go.Indicator(
        mode="number+gauge",
        value=updated_BCM_df[item11].values[0],
        #delta={'reference': REFERENCE_VALUES[item11], "valueformat": ".0%"},
        number = {"valueformat": ".0%"},
        gauge = {
            'shape': "bullet",
            'axis': {
                "range": [0.4, 0.4983],
                "tickmode": "array",
                "tickvals": [0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.4983],
                "ticktext":['40%','41%','42%','43%','44%','45%','46%',
                            # "47%<br>Federal Census<br>2016",
                            '47%',
                            '48%','49%',
                            "49.8%<br>Highest Result<br>by 2032",
                ],
                "tickangle":0,
            },
            'bar': {'color': "rgb(47, 99, 173)" , 'thickness': 0.6},
            # 'threshold': {'line': {'color': thresholdColor, 'width': 5}, 'thickness': 1, 'value': REFERENCE_VALUES[item11]},
            # 'steps': [
            #     {'range': [0.4, (sum(updated_BCM_df[item11]) / len(updated_BCM_df[item11]))], 'color': "rgba(47, 99, 173, 0.3)"},
            # ],
        },
    ))
    
    fig.update_layout(
        template="ggplot2",
        #title="Percentage of Employment in Nodes and Corridors by 2032<br><span style='font-size:0.8em;color:gray'>Compare to the 2016 Federal Census</span>",
        font_family="Times New Roman",
        margin=dict(l=30, r=30, t=30, b=60),
        height=200,
        barmode='overlay',
        bargap=0.9,
        showlegend=False
    )
    
    return fig

app.callback(
    Output("Nodes and Corridors support 50% of all employment in Edmonton-graph", "figure"),
    [Input("BCM_range_list", "data")]
)(graph_NodesCorridors)

def graph_InnovationCorridors(filtered_BCM_df):
    
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    item11 = "Innovation Corridor attracts 50,000 more employment"
    
    if updated_BCM_df[item11].values[0] < REFERENCE_VALUES[item11]:
        thresholdColor = "rgba(240, 88, 83, 1)"
    else:
        thresholdColor = "rgba(42, 145, 52, 1)"
        
    fig = go.Figure(go.Indicator(
        mode="number+gauge",
        value=round(updated_BCM_df[item11].values[0], -3),
        #delta={'reference': REFERENCE_VALUES[item11]},
        gauge = {
            'shape': "bullet",
            'axis': {
                "range": [0, 51380],
                "tickmode": "array",
                "tickvals": [0,5000,10000,15000,20000,25000,30000,35000,40000,45000,51380],
                "ticktext":['0','5K','10K','15K','20K','25K','30K',
                            '35K','40K','45K',
                            "51.3K<br>Highest Result<br>by 2032",
                ],
                "tickangle":0,
            },
            'bar': {'color': "rgb(47, 99, 173)" , 'thickness': 0.6},
            # 'threshold': {'line': {'color': thresholdColor, 'width': 5}, 'thickness': 1, 'value': REFERENCE_VALUES[item11]},
            # 'steps': [
            #     {'range': [0, (sum(updated_BCM_df[item11]) / len(updated_BCM_df[item11]))], 'color': "rgba(47, 99, 173, 0.3)"},
            # ],
        },
    ))
    
    fig.update_layout(
        template="ggplot2",
        # title="Employment Growth in Innovation Corridor by 2032<br><span style='font-size:0.8em;color:gray'></span>",
        font_family="Times New Roman",
        margin=dict(l=30, r=30, t=30, b=60),
        height=200,
        barmode='overlay',
        bargap=0.9,
        showlegend=False
    )
    
    return fig

app.callback(
    Output("Innovation Corridor attracts 50,000 more employment-graph", "figure"),
    [Input("BCM_range_list", "data")]
)(graph_InnovationCorridors)

def graph_Region(filtered_BCM_df):
    
    updated_BCM_df = pd.DataFrame(filtered_BCM_df)
    item11 = "Hold 70% of total regional employment in Edmonton"
    if updated_BCM_df[item11].values[0] < REFERENCE_VALUES[item11]:
        thresholdColor = "rgba(240, 88, 83, 1)"
    else:
        thresholdColor = "rgba(42, 145, 52, 1)"
        
    fig = go.Figure(go.Indicator(
        mode="number+gauge",
        value=updated_BCM_df[item11].values[0],
        # delta={'reference': REFERENCE_VALUES[item11], "valueformat": ".0%"},
        number = {"valueformat": ".0%"},
        gauge = {
            'shape': "bullet",
            'axis': {
                "range": [0.50, 0.7563],
                "tickmode": "array",
                "tickvals": [0.50,0.55,0.60,0.65,0.70,0.7563],
                "ticktext":['50%','55%',
                            "60%",
                            "65%","70%",
                            "75.6%<br>Highest Result<br>by 2032",
                ],
            },
            'bar': {'color': "rgb(47, 99, 173)" , 'thickness': 0.6},
            # 'threshold': {'line': {'color': thresholdColor, 'width': 5}, 'thickness': 1, 'value': REFERENCE_VALUES[item11]},
            # 'steps': [
            #     {'range': [0.72, (sum(updated_BCM_df[item11]) / len(updated_BCM_df[item11]))], 'color': "rgba(47, 99, 173, 0.3)"},
            # ],
        },
    ))
    
    fig.update_layout(
        template="ggplot2",
        # title="Percentage of Regional Employment in the City by 2032<br><span style='font-size:0.8em;color:gray'></span>",
        font_family="Times New Roman",
        margin=dict(l=30, r=30, t=30, b=60),
        height=200,
        barmode='overlay',
        bargap=0.9,
        showlegend=False
    )
    
    return fig

app.callback(
    Output("Hold 70% of total regional employment in Edmonton-graph", "figure"),
    [Input("BCM_range_list", "data")]
)(graph_Region)

##### Tab 2 #####

# @app.callback(
#     [Output("measures-slider", "min"), Output("measures-slider", "max"), Output("measures-slider", "value")],
#     Input("measures-dropdown", "value")
# )

# def update_measures_slider(item):
#     return round_down(min(df[item]), 2), round(max(df[item]), 2), [round_down(min(df[item]), 2), round(max(df[item]), 2)]
  
  
# @app.callback(
#     Output("item_range_list_2", "data"),
#     [Input("measures-dropdown", "value"), Input("measures-slider", "value")] 
# )

# def update_range_list_2(item, value_range):
#     filter_data_df = df.copy()
#     filter_data_df = filter_data_df.loc[(df[item] >= value_range[0]) & (df[item] <= value_range[1])] 
#     return filter_data_df.to_dict("records")

                        
# @app.callback(
#     Output("measures-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data")]
# )

# def update_measures_graph(item, filtered_data):
#     updated_df = pd.DataFrame(filtered_data)
#     fig = make_subplots(
#         rows=1,
#         cols=2,
#         column_widths=[0.8, 0.2],
#         specs=[
#             [
#                 {"type": "xy"},
#                 {"type": "indicator"}
#             ]
#         ]
#     )
#     figure = fig.add_trace(
#         go.Histogram(
#             x=df[item],
#             histnorm='probability',
#             bingroup=1,
#             marker_color="rgb(141, 153, 174)",
#             opacity=0.6,
#             name="Total",
#             showlegend=False,
#         ),
#         row=1,
#         col=1
#     )
#     figure = fig.add_trace(
#         go.Histogram(
#             x=updated_df[item],
#             histnorm='probability',
#             bingroup=1,
#             marker_color="rgb(43, 45, 66)",
#             opacity=0.6,
#             name="Selected",
#             showlegend=False,
#         ),
#         row=1,
#         col=1
#     )
#     figure = fig.add_trace(
#         go.Indicator(
#             mode="number+delta",
#             value=(sum(updated_df[item]) / len(updated_df[item]))
#         ),
#         row=1,
#         col=2
#     )
#     figure = fig.update_layout(
#         title_text=item,
#         title_x=0.5,
#         barmode='overlay',
#         bargap=0.1,
#         template={
#             'data': {
#                 'indicator': [
#                     {
#                         'title': {'text': "Mean"},
#                         'mode': "number+delta",
#                         'delta': {'reference': df[item].mean()}
#                     }
#                 ]
#             }
#         },
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.02,
#             xanchor="left",
#             x=0
#         ),
#         shapes=[
#             dict(
#                 type="line",
#                 yref='paper',
#                 y0=0,
#                 y1=1,
#                 xref='x',
#                 x0=REFERENCE_VALUES[item],
#                 x1=REFERENCE_VALUES[item],
#                 name="Default",
#                 line=dict(
#                     color="Blue",
#                     width=3,
#                     dash="dash"
#                 )
#             ),
#             dict(
#                 type='rect',
#                 xref='paper',
#                 yref='paper',
#                 x0=-0.03,
#                 y0=-0.13,
#                 x1=1.03,
#                 y1=1.13,
#                 line=dict(
#                     color="Black",
#                     width=1,
#                     dash="dash"
#                 ) 
#             )
#         ],
#         margin=dict(
#             l=50,
#             r=50,
#             t=50,
#             b=50
#         ),
#     )
#     return figure

# def update_input_graph(measure, filtered_data, input):
#     x_item=input.split("-")[0]
#     y_item=measure
#     updated_df = pd.DataFrame(filtered_data)
#     fig=go.Figure()
#     figure=fig.add_trace(
#         go.Scatter(
#             x=df[x_item],
#             y=df[y_item],
#             marker=dict(
#                 color='rgba(0, 110, 144, 0.3)',
#                 size=4
#             ),
#             mode="markers",
#             name="Total"
#         )
#     )
#     figure=fig.add_trace(
#         go.Scatter(
#             x=updated_df[x_item],
#             y=updated_df[y_item],
#             marker=dict(
#                 color='rgba(241, 143, 1, 0.3)',
#                 size=4
#             ),
#             mode="markers",
#             name="Selected"
#         )
#     )
#     figure=fig.update_layout(
#         title=y_item + " vs " + x_item,
#         title_x=0.5,
#         xaxis_title=x_item,
#         yaxis_title=y_item
#     )
#     return figure

# app.callback(
#     Output("Fare relative to base-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data"), Input("Fare relative to base-graph", "id")]   
# )(update_input_graph)

# app.callback(
#     Output("Parking cost relative to base-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data"), Input("Parking cost relative to base-graph", "id")]   
# )(update_input_graph)

# app.callback(
#     Output("Mobility as a service improvement-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data"), Input("Mobility as a service improvement-graph", "id")]   
# )(update_input_graph)

# app.callback(
#     Output("Transit network-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data"), Input("Transit network-graph", "id")]   
# )(update_input_graph)

# app.callback(
#     Output("Work at home-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data"), Input("Work at home-graph", "id")]   
# )(update_input_graph)

# app.callback(
#     Output("Utility change to transit alternatives-graph", "figure"),
#     [Input("measures-dropdown", "value"), Input("item_range_list_2", "data"), Input("Utility change to transit alternatives-graph", "id")]   
# )(update_input_graph)
    
    

# Main
if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)


