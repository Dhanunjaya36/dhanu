import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns
from corner import corner

def sanitize_filename(name):
    """Sanitize filename by removing special characters."""
    # Replace spaces and remove invalid characters
    invalid_chars = [' ', '(', ')', '/', '\\', ':', ';', '<', '>', '?', '*', '|']
    for char in invalid_chars:
        name = name.replace(char, '_')
    return name

def plot_relational_plot(df, col):
    """Create a scatter plot of the chosen column against index."""
    plt.figure(figsize=(8, 6))
    plt.scatter(df.index, df[col], alpha=0.7, color='blue')
    plt.xlabel("Index")
    plt.ylabel(col)
    plt.title(f"Relational Plot: {col}")
    
    # Sanitize filename
    safe_filename = sanitize_filename(f"{col}_relational_plot.png")
    plt.savefig(safe_filename)
    plt.close()

def plot_categorical_plot(df, col):
    """Create a categorical plot if data is categorical, else bin continuous data."""
    plt.figure(figsize=(8, 6))

    if df[col].dtype == 'object' or len(df[col].unique()) < 10:  # Categorical column
        counts = df[col].value_counts()
        counts.plot(kind='bar', color='green')
    else:  # Continuous column, use histogram
        plt.hist(df[col], bins=10, color='green', alpha=0.7, edgecolor='black')

    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.title(f"Categorical/Histogram Plot: {col}")
    
    # Sanitize filename
    safe_filename = sanitize_filename(f"{col}_categorical_plot.png")
    plt.savefig(safe_filename)
    plt.close()

def plot_statistical_plot(df, col):
    """Create a box plot to show statistical distribution."""
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[col], color='orange')
    plt.xlabel(col)
    plt.title(f"Statistical Plot (Box Plot): {col}")
    
    # Sanitize filename
    safe_filename = sanitize_filename(f"{col}_statistical_plot.png")
    plt.savefig(safe_filename)
    plt.close()

def statistical_analysis(df, col: str):
    """Compute mean, standard deviation, skewness, and excess kurtosis."""
    data = df[col].dropna()
    mean =  df["CO2 Emissions(g/km)"].mean()
    stddev = data.std()
    skew_val = ss.skew(data)
    excess_kurtosis = ss.kurtosis(data)
    return mean, stddev, skew_val, excess_kurtosis

def preprocessing(df):
    """Preprocess data: drop missing values and strip column names."""
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
    df = df.dropna()  # Drop rows with missing values

    # Select only numeric columns for correlation calculation
    numeric_df = df.select_dtypes(include=[np.number])

    # Displaying quick insights
    print("Data Overview:")
    print(df.describe(), "\n")
    print("First few rows:")
    print(df.head(), "\n")

    if not numeric_df.empty:  # Check if there are numeric columns before calculating correlation
        print("Correlation Matrix (numeric columns only):")
        print(numeric_df.corr(), "\n")
    else:
        print("No numeric columns available for correlation analysis.\n")

    return df

def writing(moments, col):
    """Print the computed statistical moments with interpretation."""
    print(f'\nFor the attribute "{col}":')
    print(f'  Mean = {moments[0]:.2f}')
    print(f'  Standard Deviation = {moments[1]:.2f}')
    print(f'  Skewness = {moments[2]:.2f}')
    print(f'  Excess Kurtosis = {moments[3]:.2f}')

    skew_interpretation = "right-skewed" if moments[2] > 0 else "left-skewed" if moments[2] < 0 else "symmetric"
    kurtosis_interpretation = "leptokurtic (peaked)" if moments[3] > 0 else "platykurtic (flat)" if moments[3] < 0 else "mesokurtic (normal)"

    print(f'  The data is {skew_interpretation} and {kurtosis_interpretation}.\n')

def main():
    # Set the correct file path for Windows
    folder_path = r'C:\Users\lenovo\Desktop\machine learning\Data science\Applied Data Science'
    file_name = "data.csv"  # Use data.csv file
    file_path = f"{folder_path}\\{file_name}"  # Use f-string to join the path

    # Check if file exists
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        return

    # Preprocess the data
    df = preprocessing(df)

    # Choose column for analysis
    col = 'CO2 Emissions(g/km)'
    if col not in df.columns:
        print(f"Error: The column '{col}' does not exist in the dataset.")
        print("Available columns:", list(df.columns))
        col = input("Enter the column name to analyze: ").strip()
        if col not in df.columns:
            print("Invalid column name. Exiting program.")
            return

    # Generate plots
    plot_relational_plot(df, col)
    plot_statistical_plot(df, col)
    plot_categorical_plot(df, col)

    # Perform statistical analysis
    moments = statistical_analysis(df, col)
    writing(moments, col)

    # Generate corner plot for all numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(numeric_cols) > 1:  # Only plot if multiple numeric columns exist
        numeric_data = df[numeric_cols].dropna().values
        figure = corner(numeric_data, labels=numeric_cols, show_titles=True, title_fmt=".2f")
        plt.show()

if __name__ == '__main__':
    main()
