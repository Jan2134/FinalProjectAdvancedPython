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
@click.option("-p", "--plotting", is_flag=True, help="Plotdata")
def main(input, plotting):
    """
    Main execution function
    """
    df = load_dataset(input)
    print(df.shape)

    if plotting:
        StressfactorAnalysis(df)


if __name__=="__main__":
    main()
