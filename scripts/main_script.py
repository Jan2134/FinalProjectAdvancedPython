"""
Main script to execute the code through the CLI
"""

import pandas as pd
import click

if __name__ == "__main__":
    from plotting import StressfactorAnalysis


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
def main(input, plotting, plot_main):
    """
    Main execution function
    """
    df = load_dataset(input)

    if plotting:
        if plot_main:
            StressfactorAnalysis(df)


if __name__=="__main__":
    main()
