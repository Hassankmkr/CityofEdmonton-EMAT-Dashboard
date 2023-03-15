import math
import pandas as pd
import plotly
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html

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

def human_format(number, decimals):
    units = ['', 'K', 'M', 'G', 'T', 'P']
    k = 1000.0
    magnitude = int(math.floor(math.log(number, k)))
    return decimals % (number / k**magnitude, units[magnitude])

def round_down(value, decimals):
    """Round down the number based on decimals

    Args:
        value (int): Number
        decimals (int): Number of decimals to consider

    Returns:
        Float: Rounded number
    """
    factor = 1 / (10 ** decimals)
    return (value // factor) * factor

def modal_range_slider(lst, ind, title):
    feature_div= html.Div(
        [
            html.Div(
                html.P(
                    "- " + title,
                    style={"font-size": "120%", "padding": "5px"}
                ),
                className="one-third column",
            ),
            html.Div(
                dcc.RangeSlider(
                    id=f"{lst[ind]}-slider",
                    min=math.floor(df[lst[ind]].min()),
                    max=math.ceil(df[lst[ind]].max()),
                    value=[
                        math.floor(df[lst[ind]].min()),
                        math.ceil(df[lst[ind]].max())
                    ],
                    tooltip={
                        "placement": "top",
                        "always_visible": True
                    },
                ),
                className="one-third column"
            ),
            html.Div(
                html.P(
                    id=f"{lst[ind]}-text",
                    style={"font-size": "120%"}
                ),
                className="one-third column",
            )
        ],
        className="twelve columns",
        style={"margin-bottom": "1rem"}   
    )  
    return feature_div

def maas_slider(lst, ind, title):
    feature_div= html.Div(
        [
            html.Div(
                html.P(
                    "- " + title,
                    style={"font-size": "120%", "padding": "5px"}
                ),
                className="one-third column",
            ),
            html.Div(
                dcc.RangeSlider(
                    id=f"{lst[ind]}-slider",
                    step=None,
                    min=math.floor(df[lst[ind]].min()),
                    max=math.ceil(df[lst[ind]].max()),
                    marks={
                        -10: 'Low',
                        0: 'Zero',
                        8: 'Moderate',
                        16: 'High',
                        25: 'Extreme'
                    },
                    value=[
                        math.floor(df[lst[ind]].min()),
                        math.ceil(df[lst[ind]].max())
                    ],
                ),
                className="one-third column"
            ),
            html.Div(
                html.P(
                    id=f"{lst[ind]}-text",
                    style={"font-size": "120%"}
                ),
                className="one-third column",
            )
        ],
        className="twelve columns",
        style={"margin-bottom": "1rem"}   
    )  
    return feature_div

def transitA_slider(lst, ind, title):
    feature_div= html.Div(
        [
            html.Div(
                html.P(
                    "- " + title,
                    style={"font-size": "120%", "padding": "5px"}
                ),
                className="one-third column",
            ),
            html.Div(
                dcc.RangeSlider(
                    id=f"{lst[ind]}-slider",
                    step=None,
                    min=math.floor(df[lst[ind]].min()),
                    max=math.ceil(df[lst[ind]].max()),
                    marks={
                        -10: 'Very Low',
                        -4: 'Low',
                        0: 'Zero',
                        4: 'High',
                        10: "Very High"
                    },
                    value=[
                        math.floor(df[lst[ind]].min()),
                        math.ceil(df[lst[ind]].max())
                    ],
                    # tooltip={
                    #     "placement": "top",
                    #     "always_visible": True
                    # },
                ),
                className="one-third column"
            ),
            html.Div(
                html.P(
                    id=f"{lst[ind]}-text",
                    style={"font-size": "120%"}
                ),
                className="one-third column",
            )
        ],
        className="twelve columns",
        style={"margin-bottom": "1rem"}   
    )  
    return feature_div

def modal_category_selection(title, lst, ind, multiOption, optionOptions, valueOptions):
    feature_div=html.Div(
        [
            html.Div(
                html.P(
                "- " + title,
                className="one-third column",
                style={"font-size": "120%", "padding": "5px"}
                ),
            ),
            html.Div(
                [
                    dcc.Dropdown(
                        id=lst[ind]+"-dropdown",
                        options=optionOptions,
                        value=valueOptions,
                        placeholder=title,
                        multi=multiOption,
                    ),
                ],
            className="one-half column",
            ) 
        ],
        className="twelve columns",
        style={"margin-bottom": "1rem"} 
    )
    return feature_div

# df_BCM = pd.DataFrame(
#     np.array(
#         [
#             [349272, 182239, 225, 1041, 352102, 196596, 18597, 3049],
#             [753483, 487714, 627, 1535, 784932, 425802, 8958, 6836]
#         ]
#     ),
#     columns=["CP Redeveloping", "CP Developing", "CP Future Growth", "CP Industrial" ,"Ref Redeveloping", "Ref Developing", "Ref Future Growth", "Ref Industrial"],
#     index=["50% Net New Units will be added through Infill City wide", "600k additional residents will be welcomed within redeveloping Area"] 
# )

# df_pop_policy = pd.DataFrame(
#     np.array(
#         [
#             [11069,0,8101,-7662,18547,2877],
#             [-392,0,-2289,6310,-2118,935],
#             [-8159,0,-7,22,5,27],
#             [-19,0,-9,-43,155,-3]
#         ]
#     ),
#     columns=["pol_A", "pol_B", "pol_C", "pol_D","pol_E", "pol_F"],
#     index=["Redeveloping", "Developing", "Future Growth", "Industrial"]
# )

# df_unit_policy = pd.DataFrame(
#     np.array(
#         [
#             [11079,0,3256,-2559,6972,1204],
#             [-3982,0,-1584,2074,-576,71],
#             [-15539,0,-55,-296,148,121],
#             [8,0,-19,-9,48,-9]
#         ]
#     ),
#     columns=["pol_A", "pol_B", "pol_C", "pol_D","pol_E", "pol_F"],
#     index=["Redeveloping", "Developing", "Future Growth", "Industrial"]
# )



# def build_modal_info_overlay(title, id, side, content):
#     """Create modal tabs to provide information to users on each dashboard sections

#     Args:
#         id (str): ID of the modal
#         side (str): Place of modal in dashboard
#         content (str): Description to show on modal

#     Returns:
#         html.Div: A window that present the description of each sections
#     """
#     div = html.Div(
#         [  # modal div
#             html.Div(
#                 [  # content div
#                     html.Div(
#                         [
#                             html.H4(
#                                 [
#                                     title,
#                                     html.Img(
#                                         id=f"close-{id}-modal",
#                                         src="assets/cross-sign-svgrepo-com.svg",
#                                         n_clicks=0,
#                                         className="info-icon",
#                                         style={"margin": 0},
#                                     ),
#                                 ],
#                                 className="container_title",
#                                 style={"color": "Black"},
#                             ),
#                             dcc.Markdown(content),
#                         ]
#                     )
#                 ],
#                 className=f"modal-content {side}",
    #         ),
    #         html.Div(className="modal"),
    #     ],
    #     id=f"{id}-modal",
    #     style={"display": "none"},
    # )

    # return div

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "sticky",
    "top": "0px",
    "float": "left",
    "display": "inline-block",
    "height":"100vh",
}
            
# padding for the page content
CONTENT_STYLE = {
    "display": "inline-block",
    "float": "right",
}
info_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H3(
                        "Introduction",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Big City Moves are an invitation to work together to build our future city in a new way. They define bold, transformative priorities and create a different set of opportunities for Edmonton. The Big City Moves point the way as we deliberately change our city to welcome one million more on our journey towards a population of two million. Achieving tangible change means setting ambitious targets. The city plan has identified five big city moves and set long term targets and measures for each of them. The next step is setting interim targets for the next 10-years.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'> Urban Systems Assessments</span> has developed an <span style='text-decoration:underline'>analytical and visualization dashboard</span> to understand the impact of different policies, levers, and uncertainties on Edmonton’s future growth and travel patterns. The main objective of this dashboard is to allow the planners to set interim City plan targets based on evidence from exploratory modeling and analysis. The analytics were conducted using the results extracted from both 2032 Edmonton RTM (Regional travel Model) and 2032 MRSET (Metro Regional Spatial Economic and Transportation model).</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Rather than providing single point estimates for a fixed set of assumptions, the exploratory analysis tool provides a range of possibilities for a given policies, levers, and uncertainties. Users can pick and choose the policy and lever combinations and see what combinations would yield a desired outcome.</h6>
                    '''),
                    html.Img(src="assets/Flowchart.png", style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_info_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="info_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

landuse_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H4(
                        ""
                    )
                )
            ),
            dbc.ModalBody(
                ""
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_landuse_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="landuse_modal",
        is_open=False,
    ),
)

AB_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H3(
                        "Delayed Land Release + Upzonning in Redeveloping Areas",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>
                            <ul style="padding-left:20px; list-style-type: disc; line-height:1">
                                <li> Delayed land release means postponing the availability of suburban lands in Edmonton for housing construction until a later date.</li>
                                <li> Lot splitting is the process of subdividing a single residential lot into multiple legal lots. To increase the population density of redeveloping areas, City may develop a new zoning bylaw that allows:</li>
                                    <ul style="padding-left:20px; line-height:1">
                                        <li> Construction of two detached skinny houses or two semi-detached houses with separate titles </li>
                                        <li> Construction of row houses on a parcel that is currently zoned for single detached housing  </li>
                                    </ul>
                            </ul>
                        </h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style="text-decoration:underline">Delayed Land Release</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>In some neighborhoods outside of Anthony Henday Drive, such as Horse Hill, Riverview, Windermere, Decoteau, and annexation lands in South Edmonton, the release of lands for development has been delayed by 10~35 years.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style="text-decoration:underline">Lot Splitting</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>
                            <ul style="padding-left:20px; list-style-type: disc; line-height:1">
                                <li> Criteria: Select all single-family detached dwelling parcels in Redeveloping areas that have</li>
                                    <ul style="padding-left:20px; line-height:1">
                                        <li> Total site area of 500 sqm or more </li>
                                        <li> And lot frontage width greater than 50 ft </li>
                                    </ul>
                                <li> What Allowed: Based on demand, single-family, attached and row housing options were permitted for reconstruction</li>
                            </ul>
                        </h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Where: The red hashed polygons on the map below (left) shows the areas with delayed land release. The red color parcels on the right map shows the parcel within the redeveloping areas where lot splitting is allowed. </h6>
                    '''),
                    html.Img(src="assets/a.png", style={'display': 'inline-bblock', 'width':'50%'}),
                    html.Img(src="assets/b.png", style={'display': 'inline-block', 'width':'50%'}),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_AB_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="AB_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

C_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H3(
                        "Diffential Residential Tax",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>The residential property taxes are varied by housing products (e.g., single detached, semi-detached, attached, apartments, etc.) and housing locations (e.g., redeveloping, developing and future growth areas)</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>
                            <ul style="padding-left:20px; list-style-type: disc; line-height:1">
                                <li> Incentives or tax subsidies were provided for all houses located in redeveloping neighborhoods. Marked as brown on the map below:</li>
                                    <ul style="padding-left:20px; line-height:1">
                                        <li> Single-family dwellings and attached dwellings receive 8% of equivalent annual rent (~ 40% of the annual property taxes) as subsidies </li>
                                        <li> Multifamily dwellings receive 12% of equivalent annual rent (~ to 110% of their annual property taxes) as subsidies </li>
                                    </ul>
                                <li> Single-family homes in developing areas and future growth areas (yellow and light yellow in color) were penalized with additional tax burden.</li>
                                    <ul style="padding-left:20px; line-height:1">
                                        <li> Single-family dwellings will be paying 8% of equivalent annual rent as additional taxes (~ 40% additional property tax cost) </li>
                                    </ul>
                            </ul>
                        </h6>
                    '''),
                    html.Img(src="assets/c.png", style={'display': 'block', 'width':'50%', 'margin-left': 'auto', 'margin-right': 'auto'}),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_C_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="C_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

D_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H3(
                        "Upzoning in Nodes and Corridors",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Single-family and attached houses are converted into high-density multi-family housing in nodes and corridors.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>
                            <ul style="padding-left:20px; list-style-type: disc; line-height:1">
                                <li> Permit the construction of high-density multifamily housing on low-density multifamily housing zones that have a floor area ratio (FAR) greater than 2.6, without altering the density (FAR) of the land. </li>    
                                <li> Single-family and attached zoning parcels in nodes and corridors were rezoned to high-density multifamily space with a minimum FAR of 0.5 and a maximum FAR of 4. </li>
                            </ul>
                        </h6>
                    '''),
                    html.Img(src="assets/d.png", style={'display': 'block', 'width':'50%', 'margin-left': 'auto', 'margin-right': 'auto'}),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_D_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="D_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

E2_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H3(
                        "Increase in Automobile Operating Costs (2x)",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>City attempts to increase auto operating costs by means of taxes, levies, registration charges etc.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>The cost items such as fuel consumption, routine maintenance, tires, and repairs  that depend on the amount of driving were considered as part of the BASE automobile operating costs. These costs are currently estimated at 17.5 cents per kilometer based on the AMA's Car Operating Cost report, which is used in the Edmonton Regional Travel model (RTM). However, in order to achieve a desired City plan target, the city may need to increase the overall auto operational cost by imposing taxes, levies, registration charges, etc. Two scenarios are examined to understand the impact of such actions, where the operating costs are increased to twice and five times the base costs.</h6>
                    '''),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_E2_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="E2_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

E5_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle(
                    html.H3(
                        "Increase in Automobile Operating Costs (5x)",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>City attempts to increase auto operating costs by means of taxes, levies, registration charges etc.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>The cost items such as fuel consumption, routine maintenance, tires, and repairs  that depend on the amount of driving were considered as part of the BASE automobile operating costs. These costs are currently estimated at 17.5 cents per kilometer based on the AMA's Car Operating Cost report, which is used in the Edmonton Regional Travel model (RTM). However, in order to achieve a desired City plan target, the city may need to increase the overall auto operational cost by imposing taxes, levies, registration charges, etc. Two scenarios are examined to understand the impact of such actions, where the operating costs are increased to twice and five times the base costs.</h6>
                    '''),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_E5_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="E5_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

levers_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle( 
                    html.H3(
                        "Mobility Policies, Actions and Levers",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    html.H4(
                        "Changes in Transit Fare",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Increase or decrease the cost of a transit ride.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Several levels (increase and decrease) of fares were considered to capture the impacts of fare on transit ridership and potential changes in travel patterns such as automobile use.</h6>
                    '''),
                    
                    html.H4(
                        "Changes in Parking Cost",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>To capture the potential impacts of increase or decrease in parking rates.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Parking Rates especially in downtown and university play a significant role in commuting mode share. The potential impact of parking rate on travel patterns has been evaluated through several RTM scenarios built with varying parking prices (very low to extremely high). This policy is implemented only for parking lots in downtown and University.</h6>
                    '''),
                    
                    html.H4(
                        "Emergence of Shared Mobility Services",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Changes in cost and availability of shared ride services such as taxis in Edmonton.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Mobility Services refers to a shift from individual vehicle ownership to transportation services provided by operators. With the advancements in technology, transportation services have become more convenient and accessible for people. The traditional taxi service has been revolutionized by the advent of app-based ride-hailing services such as Uber and Lyft, which have made it easier for people to access transportation services at the touch of a button. Even autonomous vehicles in the future may work as taxi-like services without a driver.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>The potential impact of Emergence of Shared Mobility Services on travel patterns has been evaluated through several RTM scenarios developed by varying the usage of mobility services. (very low to extremely high).</h6>
                    '''),
                    
                    html.H4(
                        "Investment in Transit and Active Mode Infrastructure",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the policy?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Evaluate the impacts of transit and active mode infrastructure investments on use of transportation systems.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the policy implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>
                        Two alternative transit and active mode networks were considered.
                            <ul style="padding-left:20px; list-style-type: disc; line-height:1">
                                <li> Limited Investment Scenario </li>    
                                <li> Aspirational Investment Scenario </li>
                            </ul>
                        </h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Investment in public transportation infrastructure can bring improvement in transit accessibility and increase transit mode share and reduce car usage and GHG emissions. </h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Two RTM scenarios, one with the current transit network and another with a comprehensive mass transit network, were created to assess the impact of transit investments on transit mode share and greenhouse gas reductions. These analytics tools help us make informed decisions about investment and understand how effective these investments are to achieve City plan goals.</h6>
                    '''),
                    html.Img(src="assets/Limited.jpg", style={'display': 'inline-bblock', 'width':'50%'}),
                    html.Img(src="assets/Aspirational.jpg", style={'display': 'inline-block', 'width':'50%'}),
                    
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_levers_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="levers_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)

uncertainties_modal = html.Div(
    dbc.Modal(
        [
            dbc.ModalHeader(
                dbc.ModalTitle( 
                    html.H3(
                        "Uncertainties",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    )
                )
            ),
            dbc.ModalBody(
                [
                    html.H4(
                        "Economic Diversification",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the uncertainty?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>This uncertainty is to understand the potential impacts of diversification of Alberta’s economy. Under this uncertainty, it was assumed that the technology sector growth will outpace the oil and gas sector while the overall size of the economy will remain the same.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the uncertainty implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>First, North American Industry Classification System (NAICS) codes representing technology- and innovation-focused businesses were selected. To achieve substantial growth in these businesses compared to others, the projected economic outputs associated with these selected businesses in Alberta by 2065 were doubled compared to base projections. Then, the growth between now and 2065 was interpolated to the interim horizons. To maintain the projected total economic output in Alberta, the economic activity of industries outside the innovation and technology sectors was correspondingly reduced annually.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>The chart below shows the chosen NAICS codes to represent the innovation and technology businesses and their corresponding economic output in 1M, 1.25M and 2M City population horizons. The second chart below illustrates the share of the innovation sector within the overall economic output, both prior to and following the shift towards economic diversification.</h6>
                    '''),
                    html.Img(src="assets/Innovation sectors.png", style={'display': 'inline-bblock', 'width':'50%'}),
                    html.Img(src="assets/AfterBefore.png", style={'display': 'inline-bblock', 'width':'50%'}),
                    
                    
                    html.H4(
                        "Emergence of Hybrid Work",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the uncertainty?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>To capture the uncertainty around emergence of “Hybrid Work” as the potential new normal for the office workers. </h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the uncertainty implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>According to Statistics Canada, approximately 40% of the Canadian workforce has the potential to work remotely. While workers in some industries such as retail and construction do not have much choice of remote work, other industries such as information and cultural industries, professional, scientific and technical services and managers of companies and enterprises have more flexibility in their workplace choice. To capture this variation, the remote work rate by industry sector has been varied from 5% to 40%.</h6>
                    '''),
                    
                    
                    html.H4(
                        "Changes in Citizens' Perception Towards Transit",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the uncertainty?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>To capture the potential impacts on transit system use with the change in people's perception and attitudes towards public transit systems. </h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the uncertainty implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>Perception and attitudes towards public transit systems are influenced by several factors such as system reliability, transit safety, system cleanliness, efficient and convenient ticketing system, convenience of fare medium, access to real time transit information. Using the 2015 Household Travel Survey (HTS) data, and 2019 LRT and bus boarding data, the Edmonton RTM has established factors to represent the user perceptions towards transit in Edmonton. To capture variation in user experiences, these factors were varied (relative to pre-pandemic user experience) in a negative and positive direction.</h6>
                    '''),
                    
                    
                    html.H4(
                        "Emergence of Micromobility",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the uncertainty?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>To capture the impacts (i.e., how do people choose to travel in and around urban centers?) of alternative mobility options using micro mobility modes such as e-scooters, and e-bikes.</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the uncertainty implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>The potential impact of micromobility has been evaluated through several RTM scenarios, ranging from nominal adoption to accelerated adoption. The potential adoption rate was altered based on the user experience, safety perception, cost of service, availability, and area of operation. With the varying degree of experience and perception, the several adoption rates from limited (representing current condition) to extremely high were considered. </h6>
                    '''),
                    
                    
                    html.H4(
                        "Market Adoption of Electric Vehicles",
                        style={"font-weight": "bold", "color": "rgba(47, 99, 173, 1)"}
                    ),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>What is the uncertainty?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>To capture the impacts of accelerated market adoption of the Electric Vehicles (EV).</h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6><span style='font-weight:bold'>How was the uncertainty implemented?</span></h6>
                    '''),
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                        <h6>According to the ambitious mandatory target set out by the Federal Government, by 2026, 20% of all passenger cars, SUVs, and trucks sold in Canada will need to run on electricity, and this number will increase to 60% by 2030 and 100% by 2035. To capture the uncertainty, two different vehicle fleet compositions (current composition and 26% of passenger cars being electric) were considered.  </h6>
                    '''),
                    
                    
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close", id="close_uncertainties_modal", className="ms-auto", n_clicks=0
                )
            ),
        ],
        id="uncertainties_modal",
        is_open=False,
        size="xl",
        scrollable=True,
    ),
)