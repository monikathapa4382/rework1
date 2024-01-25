import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:\\Users\\Monika\\Downloads\\Monika\\World Population Live Dataset.csv"
population_data = pd.read_csv(file_path)

def plot_population_growth(data, countries):
    """Plot population growth for selected countries."""
    years = ['1970', '1980', '1990', '2000', '2010', '2015', '2020', '2022']
    population_growth = data[data['Name'].isin(countries)][['Name'] + years]

    plt.figure(figsize=(12, 8))
    sns.set(style="whitegrid")
    for index, row in population_growth.iterrows():
        sns.lineplot(x=years, y=row[1:], label=row['Name'], linewidth=2.5)

    plt.title('Population Growth Over Selected Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Population in Millions', fontsize=14)
    plt.legend(title='Country', title_fontsize='13', fontsize='12')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

def plot_advanced_pie_chart(data, countries):
    """Plot an advanced pie chart for world population percentage."""
    population_percentage = data[data['Name'].isin(countries)][['Name', 'World Population Percentage']]
    population_percentage['World Population Percentage'] = population_percentage['World Population Percentage'].str.rstrip('%').astype('float')
    explode = [0.1 if i == population_percentage['World Population Percentage'].idxmax() else 0 for i in population_percentage.index]

    plt.figure(figsize=(10, 10))
    colors = sns.color_palette('pastel')[0:len(countries)]
    plt.pie(population_percentage['World Population Percentage'], labels=population_percentage['Name'], autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
    plt.title('World Population Percentage of Top Countries', fontsize=16)
    plt.show()

def plot_population_density_bar_chart(data, countries):
    """Plot bar chart for population density."""
    population_density = data[data['Name'].isin(countries)][['Name', 'Density (per km²)']]

    plt.figure(figsize=(12, 8))
    sns.barplot(x='Name', y='Density (per km²)', data=population_density, palette='viridis')
    plt.title('Population Density of Top Countries', fontsize=16)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Density (per km²)', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y')
    plt.show()



# Top countries for demonstration
top_countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan']

# Calling the functions to plot the charts
plot_population_growth(population_data, top_countries)
plot_advanced_pie_chart(population_data, top_countries)
plot_population_density_bar_chart(population_data, top_countries)

