CITY_MOVES = dict(
    GG="Greener as We Grow",
    CC="A Community of Communities",
    IC="Inclusive and Compationate",
    RC="A Rebuildable City",
    CaC="Catalyze and Converge"
)

CITY_TARGETS = dict(
    GG=[
        "Achive total community-wide carbon budget of 135 megatonnes",
        "Two million urban tree planted",
        "Net per person GHG emissions are zero"
    ],
    CC=[
        "50% Mode Share by Transit and Active Modes",
        "15 minutes districts"
    ],
    IC=[
        "less than 35% of average houshold expendiures are spent on housing and transportation",
        "Nobody is in core housing",
        "There is no cronic or episodic homelessness in Edmonton"
    ],
    RC=[
        "50% Net New Units will be added through Infill City wide",
        "600k additional residents will be welcomed within redeveloping Area"
    ],
    CaC=[
        "Nodes and Corridors support 50% of all employment in Edmonton",
        "Innovation Corridor attracts 50,000 more employment",
        "Hold 70% of total regional employment in Edmonton"
    ]
)

UNCERTAINTIES = [
    "Work at home",
    "Households in denser areas",
    "Households from region to city",
    "Employment (off, ind) from region to city",
    "Office employment moved to cbd",
    "Employment (off, pop) moved to nodes & corridors",
    "Utility change to transit alternatives",
    "Amount of GHG Produced (kgCO2e) (Base)",
    "Utility change to bike alternatives"
]

LEVERS = [
    "Fare relative to base",
    "Parking cost relative to base",
    "Transit network",
    "Mobility as a service improvement",
]

MEASURES = [
    "Ridership in City",
    "Annual CO2 emissions overall",
    "Transit revenue in City",
    "Work At Home overall",
    "Annual VKT per capita overall",
    "Active & Transit share in City",
    "Vehicles per capita overall",
    "Total trips made overall",
    "Population Red_NC",
    "Population Red_Rem",
    "Population Develop",
    "Population SP/SA",
    "Population Region",
    "Daily LRT boardings",
    "Daily Bus boardings",
    "Time in cars per capita Overall",
    "Time in transit per capita Overall",
    "Pct 15 min green Overall"
]

LU_POLICIES = [
    "ab - land & infill",
    "c - tax subsidy",
    "d - N&C zoning",
    "e - auto op cost",
    "f - change tech emp"
]

SLIDERS = [
    LEVERS[0],
    LEVERS[1],
    LEVERS[3],
    UNCERTAINTIES[0],
    UNCERTAINTIES[6],
    UNCERTAINTIES[8]
]

REFERENCE_VALUES = {
    "Work at home": 15,
    "Households in denser areas": 0,
    "Households from region to city": 0,
    "Employment (off, ind) from region to city": 0,
    "Office employment moved to cbd": 0,
    "Employment (off, pop) moved to nodes & corridors": 0,
    "Utility change to transit alternatives": 0,
    "Fare relative to base": 1,
    "Parking cost relative to base": 1,
    "Auto operating cost": 0.128,
    "Transit network": "BNR",
    "Mobility as a service improvement": 0,
    "Active & Transit share in City": 0.228, # From HH Travel Survey
    "Active share in City": 0.125, # From HH Travel Survey
    "Transit share in City": 0.103, # From HH Travel Survey
    "Total trips made overall": 6780709,
    "Daily LRT boardings": 108689,
    "Daily Bus boardings": 299051,
    "2021 GHG by transportation sector": 2757295,
    "2032 Annual GHG by RTM": 3562101,
    "Ridership in City": 371000,
    "Transit revenue in City": 190269141,
    "Time in cars per capita Overall": 35.23,
    "Vehicles per capita overall": 0.71,
    "Time in transit per capita Overall": 10.5,
    "Pct 15 min green Overall": 0.095,
    "50% Net New Units will be added through Infill City wide": 0.25, # Use Last five years trend:
    "Total Number of Units in the City": 452300, # 2022 RTM number : 452300
    "600k additional residents will be welcomed within redeveloping Area": 68430, # From RTM Difference 1.25M and 1M
    "Total Population in the City": 1024494, # Federal Census 2021: 1010899 (1M RTM: 1024494)
    "Total Employment in the City": 699733, # I311+100K
    "Total Employment in the Region": 206083, # Comes from 2021, emplyment form 1M RTM: 792368-586285=206083
    "Nodes and Corridors support 50% of all employment in Edmonton": 0.47, # 2016 federal census
    "Innovation Corridor attracts 50,000 more employment": 32048, # From RTM Difference 1.25M and 1M
    "Hold 70% of total regional employment in Edmonton": 0.74 # Comes from RTM 2022
    
    
}

POLICIES = dict(
    A="Delay Land Release",
    B="Infill Lot Splitting & Upzoning",
    C="Residential Tax Subsidy", # Residential Property Tax Subsidy
    D="Upzoning in N/C", # Upzoning in Nodes and Corridors
    E="Increase Auto Operating Costs",
    F="Economic Diversification"
)