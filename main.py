import pandas as pd               # Import libraries
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data from a CSV file into a pandas DataFrame
df = pd.read_csv(r'C:/Users/haidar/OneDrive/Desktop/Intern/Data Analysis Tool/DataFiveYear.csv')

# Line plot: Life expectancy over time by continent
# Plotly's line chart is used to show how life expectancy changes over the years, grouped by continent
fig = px.line(df, x='year', y='lifeExp', color='continent', 
              title='Life Expectancy Over Time by Continent')
fig.show()  # Show the plot

# Scatter plot: GDP per capita vs life expectancy, with population size as bubble size
# This plot compares the relationship between GDP per capita and life expectancy for each country,
# with the size of the bubbles representing the population and color representing the continent
fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent',
                 hover_name='country', log_x=True, title='GDP per Capita vs Life Expectancy')
fig.show()  # Show the plot

# Histogram: Distribution of GDP per capita
# This plot shows the distribution of GDP per capita across all countries in the dataset
plt.figure(figsize=(10, 6))
plt.hist(df['gdpPercap'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of GDP per Capita')
plt.xlabel('GDP per Capita')
plt.ylabel('Frequency')
plt.show()  # Show the plot

# Bar plot: Average life expectancy by continent
# This plot calculates and visualizes the average life expectancy for each continent
avg_lifeExp_by_continent = df.groupby('continent')['lifeExp'].mean().reset_index()
fig = px.bar(avg_lifeExp_by_continent, x='continent', y='lifeExp', 
             title='Average Life Expectancy by Continent')
fig.show()  # Show the plot

# Animated scatter plot: GDP per capita vs life expectancy over time
# This plot creates an animated visualization showing how GDP per capita and life expectancy evolve over time
# Each frame represents a year, and the countries are shown as bubbles
fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', size='pop',
                 animation_frame='year', animation_group='country',
                 hover_name='country', log_x=True, range_y=[20, 90],
                 title='GDP per Capita vs. Life Expectancy Over Time')
fig.show()  # Show the plot

# Box plot: Life expectancy distribution by continent
# This box plot shows the spread and distribution of life expectancy within each continent
fig = px.box(df, x='continent', y='lifeExp', 
             title='Life Expectancy Distribution by Continent')
fig.show()  # Show the plot
