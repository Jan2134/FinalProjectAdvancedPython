"""
Main script to execute the code through the CLI
"""

import pandas as pd
import click

if __name__ == "__main__":
    from plotting import StressfactorAnalysis
    from plotting import plot_two_variables

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
@click.option("-plot", "--plotting", is_flag=True, help="Plotdata")
@click.option("-main", "--plot_main", is_flag=True, help="Plot the overview graph")
@click.option("-var1", "--variable1", help="Name of the first variable to plot")
@click.option("-var2", "--variable2", help="Name of the second variable to plot")
def main(input, plotting, plot_main, variable1, variable2):
    """
    Main execution function
    """
    global count
    df = load_dataset(input)

    if plotting:
        if plot_main:
            StressfactorAnalysis(df)
        if variable1 and variable2:
            plot_two_variables(df, variable1, variable2)

if __name__=="__main__":
    main()
