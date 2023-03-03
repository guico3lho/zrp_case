import plotly.express as px
import pandas as pd
import numpy as np

# matplotlib x plotly
## plotly focus on browser
##matplotlib more profissional and more complete (arch linux) (seaborn)

# Plotly Hello World using scatter
x_data = np.random.random(100)
y_data = np.random.random(100)

fig = px.scatter(x=x_data, y=y_data)
fig.show()

# data from europe
europe_data2007 = px.data.gapminder().query("year==2007").query("continent=='Europe'")
fig = px.scatter(europe_data2007, x='lifeExp', y='gdpPercap', color='lifeExp', size='pop', hover_name='country')
fig.show()

# data from europe px line
europe_data = px.data.gapminder().query("continent=='Europe'")
fig = px.line(europe_data, x='year', y='lifeExp', color='country')
fig.show()

# auustria_data using px bar and colors
austria_data = px.data.gapminder().query("country=='Austria'")
fig = px.bar(austria_data, x='year', y='pop', color='gdpPercap', color_continuous_scale='ice')
fig.show()

# europe data px pie
fig = px.pie(europe_data2007, values='pop', names='country', title='Population of European continent')
fig.show()


