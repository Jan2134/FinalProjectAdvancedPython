"""
Statistically show dataset
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def calculate_correlation_matrix(df, n=3):
    """
    Calculate the correlation matrix for all columns in the DataFrame and show a heatmap.
    Than show the most common correlations of each other.
    """
    # Convert non-numeric columns to numeric types
    df_numeric = df.apply(pd.to_numeric, errors="coerce")
    df_numeric = df_numeric.select_dtypes(include=["number"])

    correlation_matrix = df_numeric.corr()

    # Show a heatmap of the correlation matrix
    plt.figure(figsize=(12, 10))
    sns.heatmap(
        correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1
    )
    plt.title("Correlation Matrix")
    plt.savefig(os.path.join("outputs", "correlation_matrix_heatmap.png"))
    print("\n\nHeatmap in output folder\n\n")

    # Show three highest correlations for each column
    for column in correlation_matrix.columns:
        print(f"\nTop {n} correlations for column '{column}':")
        correlations = correlation_matrix[column].abs().sort_values(ascending=False)
        top_correlations = correlations.index[1: n + 1]  # Exclude self-correlation
        for other_column in top_correlations:
            correlation_value = correlation_matrix.loc[column, other_column]
            print(f"{other_column}: {correlation_value:.4f}")
