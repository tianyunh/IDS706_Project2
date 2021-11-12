# IDS706 Project2: Command-line Tool

This is Project 2 for IDS 706 - Create Data Engineering Command-line Tool.
## CSV Linter CLT
This is a command line tool designed to generate an overview and inspection of csv files.

### Instructions 
To use this tool, you will first need to run the `setup.py` file to install any required packages.
In the command line, first run command: `python setup.py develop`
After the setting up is finished, this command line tool is ready to use.
* Run command: `csv-linter`
* Type the name of the csv file you want to inspect as input 
* You will have two options:
- 1) **summary**: you can get the summary statistics and general info of the dataset
- 2) **check**: you can check if there are any issues with the dataset. Common issues covered include columns that contain NAN, zero count columns and unnamed columns.
* Type the option name (`summary` or `check`) to continue, the CLT will return the summary statistics and info of the dataset or warnings on potential issues after inspection.
