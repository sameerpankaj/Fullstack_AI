#Applying Data Manipulation and Visualization for EDA 


'''
What is EDA?
--Exploratory Data Analysis 
--Steps in EDA
  --Data Cleaning
  --Data Transformation
  --Aggregation and Filtering

Identifying Patterns, Trends, and Correlations
--Visual Tools for Insights:
  --Line Plots for trends over time
  --Bar Charts for categorical comparisons
  --Scatter plots for relationships
  --Heatmaps for correlation analysis
--Key Patterns to Look for:
  --Relationships between variables (correlations)
  --Distribution of variables (histograms, boxplots)
  --Outliers or anomalies

Summary Statistics , Visual Insights, and Hypothesis Generation
--Summary Statistics
--Hypothesis Generation




'''


'''
Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is the process of examining, summarizing, and visualizing a dataset to understand its main characteristics before building machine learning models or performing advanced analysis.

Think of EDA as "getting to know your data".

Why is EDA Important?

EDA helps you:

Understand the structure of the dataset
Detect missing values
Identify outliers
Discover patterns and trends
Find relationships between variables
Check data quality
Generate hypotheses for further analysis

Without EDA, you may build models on poor-quality data and get misleading results.

Typical EDA Workflow
1. Load the Data
import pandas as pd

df = pd.read_csv('data.csv')
2. Inspect the Data
print(df.head())      # First 5 rows
print(df.tail())      # Last 5 rows
print(df.shape)       # Rows and columns
print(df.columns)     # Column names
print(df.info())      # Data types and missing values
3. Summary Statistics
print(df.describe())

Example output:

Statistic	Meaning
count	Number of values
mean	Average
std	Standard deviation
min	Minimum
max	Maximum
4. Check Missing Values
print(df.isnull().sum())

Example:

Name      0
Age       2
Salary    5

This shows how many missing values exist in each column.

5. Analyze Distributions
Histogram
import matplotlib.pyplot as plt

df['Age'].hist()
plt.show()

Shows how values are distributed.

6. Detect Outliers
Box Plot
import seaborn as sns

sns.boxplot(x=df['Salary'])
plt.show()

Helps identify unusually high or low values.

7. Find Relationships
Correlation Matrix
correlation = df.corr(numeric_only=True)
print(correlation)
Heatmap
sns.heatmap(correlation, annot=True)
plt.show()

Shows how variables are related.

8. Group and Aggregate Data
df.groupby('Department')['Salary'].mean()

Example:

Department	Avg Salary
IT	70000
HR	55000
Sales	62000
Common EDA Visualizations
Histogram

Shows data distribution.

plt.hist(df['Age'])
Bar Chart

Compares categories.

df['Department'].value_counts().plot(kind='bar')
Scatter Plot

Shows relationships.

plt.scatter(df['Experience'], df['Salary'])
Box Plot

Shows outliers and spread.

sns.boxplot(x=df['Salary'])
Heatmap

Shows correlations.

sns.heatmap(df.corr(numeric_only=True))
Example EDA on Iris Dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
)

print(df.head())
print(df.info())
print(df.describe())

sns.pairplot(df, hue='species')
plt.show()

This helps you:

Understand feature distributions
Compare species
Visualize relationships between measurements
EDA Tools in Python
Library	Purpose
Pandas	Data inspection and manipulation
NumPy	Numerical computations
Matplotlib	Basic plotting
Seaborn	Statistical visualization
Plotly	Interactive charts
Simple Definition
Exploratory Data Analysis (EDA)
=
Understanding your data before analyzing
or building machine learning models.
The EDA Mindset

Before asking:

"Which model should I use?"

First ask:

"What does my data look like?"

That's exactly what Exploratory Data Analysis (EDA) is designed to answer.


'''