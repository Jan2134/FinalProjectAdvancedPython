"""
Script to clean null values
"""


def handle_null_values(df):
    """
    Analyze and handle null values in a DataFrame.
    """
    print("Null values analysis:")
    print(df.isnull().sum())

    df_cleaned = df.dropna()

    print("\nDataFrame after removing null values:")
    print(df_cleaned.info())

    return df_cleaned
