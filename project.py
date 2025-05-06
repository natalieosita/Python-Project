# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style and figure size for plots
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load dataset from URL
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
try:
    df = pd.read_csv(url)
    print("Data loaded successfully from URL.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Explore dataset
print("\nDataset Columns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values Summary:")
print(df.isnull().sum())

# Data cleaning
selected_countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(selected_countries)]

df['date'] = pd.to_datetime(df['date'])

# Fill missing values forward
df.fillna(method='ffill', inplace=True)

# Drop rows with missing critical fields
df.dropna(subset=['total_cases', 'total_deaths', 'new_cases'], inplace=True)

# Basic statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Calculate death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']
avg_death_rate = df.groupby('location')['death_rate'].mean()
print("\nAverage Death Rate per Country:")
print(avg_death_rate)

# Line chart: Total cases over time
plt.figure()
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.show()

# Line chart: Total deaths over time
plt.figure()
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart: Total cases on latest date
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]
bar_data = latest_data.groupby('location')['total_cases'].sum().sort_values(ascending=False)
bar_data.plot(kind='bar', title='Total Cases on Latest Date', ylabel='Total Cases', xlabel='Country')
plt.tight_layout()
plt.show()

# Histogram: New daily cases
plt.figure()
sns.histplot(df['new_cases'], bins=30, kde=True)
plt.title("Distribution of Daily New Cases")
plt.xlabel("New Cases")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter plot: Total cases vs total deaths
plt.figure()
sns.scatterplot(data=df, x='total_cases', y='total_deaths', hue='location')
plt.title("Total Cases vs Total Deaths")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.show()

# Line chart: Vaccination progress over time
plt.figure()
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title("Vaccination Progress Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.show()

# Key insights
print("\nKey Insights:")
print("- The United States has the highest total cases and deaths among the selected countries.")
print("- India experienced a large vaccination rollout starting mid-2021.")
print("- Kenya has significantly fewer reported cases and deaths.")
print("- The average death rate differs by country, potentially due to differences in healthcare infrastructure.")
