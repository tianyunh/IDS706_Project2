import click
import pandas as pd

# import helper functions
from csvhelper import zero_count_columns, unnamed_columns, na_columns


@click.command()
@click.option('--csv', "filename", type=click.Path(exists=True), prompt="csv file to be inspected", help='The csv file to be inspected.', required=True)
@click.option('--option', type=click.Choice(['summary', 'check'], case_sensitive=False), prompt="option", help='Select options to inspect csv file.')
#@click.argument("filename", type=click.Path(exists=True))

def main(filename, option):
    """Command line tool for csv file overview and inspection"""
    df = pd.read_csv(filename)
    if option=='summary':
        click.echo(df.describe())
    
    if option=='check':
        # check columns that contain NAN
        for column in na_columns(df):
            click.echo(f"Warning: Column '{column}' has NANs in it")
        # check for zero count columns
        for column in zero_count_columns(df):
            click.echo(f"Warning: Column '{column}' has no items in it")
        # check unnamed columns
        unnamed = unnamed_columns(df)
        if unnamed:
            click.echo(f"Warning: found {unnamed} columns that are Unnamed")
            
        
        

