# Python-Project
# COVID-19 Global Data Tracker

This project is a Python-based data analysis tool that tracks and visualizes global COVID-19 trends using real-world data from [Our World in Data](https://ourworldindata.org/coronavirus-source-data). It focuses on total cases, deaths, and vaccinations over time for selected countries.

## 📌 Features

- Loads live COVID-19 data directly from an online CSV source
- Filters data for selected countries (Kenya, United States, India)
- Cleans and processes missing values
- Generates descriptive statistics and key metrics like death rate
- Visualizes data with:
  - Line charts (cases, deaths, vaccinations)
  - Bar chart (total cases on the latest date)
  - Histogram (distribution of daily new cases)
  - Scatter plot (total cases vs total deaths)

## 🗃️ Dataset

The script uses the [OWID COVID-19 dataset](https://covid.ourworldindata.org/data/owid-covid-data.csv) which includes global daily updates on:

- New and total cases
- New and total deaths
- Vaccination data
- Testing and demographic info (not all used in this script)

## 🛠️ Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn

Install required packages with:

```bash
pip install pandas matplotlib seaborn
```

## 🚀 How to Run

1. Download or clone this repository.
2. Save the Python script as `project.py`.
3. Run the script:

```bash
python project.py
```

The script will load the dataset from the URL and display several charts in sequence.

## 📊 Visualizations Included

* **Total Cases Over Time**: Line chart comparing countries
* **Total Deaths Over Time**: Line chart
* **Total Cases (Latest Date)**: Bar chart
* **Daily New Cases**: Histogram
* **Total Cases vs Deaths**: Scatter plot
* **Vaccination Progress**: Line chart

## 📈 Key Insights

* The United States has the highest total cases and deaths among the selected countries.
* India had a rapid vaccination increase starting mid-2021.
* Kenya has significantly lower reported figures.
* Death rates vary by country due to different healthcare capabilities and testing coverage.

## 🧾 Notes

* Missing values are forward-filled to preserve time series continuity.
* Visualizations are generated using `matplotlib` and `seaborn`.
* The script is written for standalone execution, no Jupyter Notebook required.


