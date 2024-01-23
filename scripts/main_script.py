"""
Main script to execute the code through the CLI
"""

import pandas as pd
import click

if __name__ == "__main__":
    from plotting import StressfactorAnalysis
    from plotting import plot_two_variables
    from stats import calculate_correlation_matrix
    from filtering import Filtering
    from regression import perform_regression
    from clean_data import handle_null_values


def load_dataset(filename):
    """
    Function to load dataset
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    raise TypeError(f"The extension is {extension}, not csv. Try again.")


@click.command(short_help="Parser to import dataset")
@click.option("-id", "--input", required=True, help="File to import")
@click.option("-clean", "--cleaning", is_flag=True, help="Clean dataset")
@click.option("-plot", "--plotting", is_flag=True, help="Plotdata")
@click.option("-main", "--plot_main", is_flag=True, help="Plot the overview graph")
@click.option("-var1", "--variable1", help="Name of the first variable to plot")
@click.option("-var2", "--variable2", help="Name of the second variable to plot")
@click.option(
    "-corr",
    "--correlation",
    is_flag=True,
    help="Show correlation heatmap & common factors",
)
@click.option("-f", "--filtering", help="Filter dataset")
@click.option("-big", "--bigger_than", help="Filter colums for bigger than x")
@click.option("-small", "--smaller_than", help="Filter colums for smaller than x")
@click.option(
    "-reg", "--regression", is_flag=True, help="Perform linear regression analysis"
)
def main(
    input,
    cleaning,
    plotting,
    plot_main,
    variable1,
    variable2,
    correlation,
    filtering,
    bigger_than,
    smaller_than,
    regression,
):
    """
    Main execution function
    """
    df = load_dataset(input)

    if cleaning:
        df = handle_null_values(df)

    if correlation:
        calculate_correlation_matrix(df)
    if filtering:
        filter_instance = Filtering()
        if bigger_than:
            filtered_df = filter_instance.bigger_than(df, filtering, float(bigger_than))
            print(filtered_df)
        elif smaller_than:
            filtered_df = filter_instance.smaller_than(
                df, filtering, float(smaller_than)
            )
            print(filtered_df)
        else:
            filtered_df = df

        if plotting and variable1 and variable2:
            plot_two_variables(filtered_df, variable1, variable2)
    if plotting:
        if plot_main:
            StressfactorAnalysis(df)
        if variable1 and variable2:
            plot_two_variables(df, variable1, variable2)
    if regression:
        perform_regression(df)


if __name__ == "__main__":
    main()
