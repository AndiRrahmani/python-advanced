import plotly.express as px

import pandas as pd
import matplotlib.pyplt as pit

df = pd.read_csv("avgIQpercountry.csv")

df['Population - 2023']= df['Population - 2023'].str.replace(',','').astype(float)

print(df.info())


fig = px.scatter_geo(df,locaions='Country',locationmode='Country name',
                     over_name='Country', size="Average IQ", color="Continent",
                     projection='natural earth', title="Average ID by Country",
                     size_max=20,template='plotly_dark')

fig.show()