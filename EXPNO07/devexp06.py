import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "State": ["California", "Texas", "New York", "Florida", "Illinois"],
    "Code": ["CA", "TX", "NY", "FL", "IL"],
    "Population": [39538223, 29145505, 20201249, 21538187, 12812508]
})

fig = px.choropleth(
    df,
    locations="Code",            
    locationmode="USA-states",   
    color="Population",          
    hover_name="State",          
    scope="usa",                
    color_continuous_scale="Viridis",
    title="US States Population (Interactive Map)"
)


fig.show()
