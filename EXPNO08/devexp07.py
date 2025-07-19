import pandas as pd
import plotly.express as px
import json
world_df = pd.DataFrame({
    'Country': ['India', 'China', 'United States', 'Brazil', 'Russia'],
    'ISO_Code': ['IND', 'CHN', 'USA', 'BRA', 'RUS'],
    'Population': [1393409038, 1444216107, 331893745, 213993437, 145912025]
})

world_fig = px.choropleth(
    world_df,
    locations="ISO_Code",
    color="Population",
    hover_name="Country",
    color_continuous_scale="Viridis",
    title="🌍 World Population Visualization"
)
world_fig.update_geos(showcountries=True)
world_fig.show()
with open("india_states.geojson", "r") as file:
    india_states_geo = json.load(file)

state_df = pd.DataFrame({
    'State': ['Tamil Nadu', 'Kerala', 'Maharashtra', 'Gujarat', 'Uttar Pradesh'],
    'Literacy': [80.1, 94.0, 82.3, 78.0, 70.2]
})

state_fig = px.choropleth(
    state_df,
    geojson=india_states_geo,
    featureidkey="properties.ST_NM",  
    locations="State",
    color="Literacy",
    color_continuous_scale="Blues",
    title="📚 Literacy Rate by Indian State"
)
state_fig.update_geos(fitbounds="locations", visible=False)
state_fig.show()

with open("india_districts.geojson", "r") as file:
    india_districts_geo = json.load(file)

district_df = pd.DataFrame({
    'District': ['Chennai', 'Mumbai', 'Lucknow', 'Ahmedabad'],
    'Rainfall': [950, 1100, 850, 720]
})

district_fig = px.choropleth(
    district_df,
    geojson=india_districts_geo,
    featureidkey="properties.district", 
    locations="District",
    color="Rainfall",
    color_continuous_scale="Greens",
    title="🌧️ Average Rainfall by Indian District"
)
district_fig.update_geos(fitbounds="locations", visible=False)
district_fig.show()
