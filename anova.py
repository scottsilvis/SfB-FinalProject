import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

def ANOVA(data = 'data.csv', 
        x_col = 'Group', 
        y_col = 'Antibody',
        group = 'Group', 
        model='1-way'):
    """
    Perform ANOVA analysis on a given dataset and create a plot of the result.

    Parameters:
    data: pandas.DataFrame - The dataset to be analyzed.
    x: str - The name of the column containing the independent variable.
    y: str - The name of the column containing the dependent variable.
    model: str - The type of ANOVA to be performed. Default is '1-way'. Other options include '2-way', 
                  'repeated-measures', and 'MANOVA'.

    Returns:
    anova_result: pandas.DataFrame - The result of the ANOVA analysis.
    """

     # Perform 1-way ANOVA
    if model == '1-way':
        print("\nPerforming 1-way ANOVA...")
        x = data[x_col]
        y = data[y_col]
        groups = [group[y_col] for name, group in data.groupby(x_col)]
        anova_result = stats.f_oneway(*groups)

    # Perform 2-way ANOVA
    elif model == '2-way':
        print("\nPerforming 2-way ANOVA...")
        formula = f"{y_col} ~ {x_col} + {x_col} * C({group})"
        model = smf.ols(formula, data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        anova_result = anova_table['F'][0:len(data[x_col].unique())]

    # Perform repeated-measures ANOVA
    elif model == 'repeated-measures':
        print("\nPerforming repeated-measures ANOVA...")
        formula = f"{y_col} ~ C({x_col}) + C({x_col}, Treatment(reference='1'))*Time"
        model = smf.ols(formula, data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        anova_result = anova_table['F'][0:len(data[x_col].unique())]

    # Perform MANOVA
    elif model == 'MANOVA':
        print("\nPerforming MANOVA...")
        y_var = [var for var in data.columns if var != x_col]
        manova_result = sm.multivariate.manova.MANOVA(data[y_var], data[x_col]).mv_test()
        anova_result = manova_result.results['x0']['stat'].iloc[0:len(data[x_col].unique())]

    else:
        raise ValueError(f"\nInvalid ANOVA model type: {model}")
        
    return anova_result
    

def main(): # Function to call the anova function
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser(description='Perform 1-way ANOVA on data.')
    
    # Tell the parser what command-line arguments this script can receive
    parser.add_argument('-d', '--data', 
                        help='The name of the data file.',
                        default='data.csv',
                        required=False)
    parser.add_argument('-x', '--x_col',
                        help='The name of the column containing the independent variable.',
                        default = 'Group',
                        required= False)
    parser.add_argument('-y', '--y_col',
                        help='The name of the column containing the dependent variable.',
                        default = 'Antibody',
                        required= False)
    parser.add_argument('-g', '--group',
                        help='The name of the column containing the group variable.',
                        default = 'Group',
                        required= False)
    parser.add_argument('-m', '--model',
                        help='The type of ANOVA to be performed. Default is 1-way ANOVA.',
                        choices=['1-way', '2-way', 'repeated-measures', 'MANOVA'],
                        default='1-way',
                        required=False)
    
    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # Load data from file
    data = pd.read_csv(args.data)

    # Perform ANOVA
    anova_result = ANOVA(data, args.x_col, args.y_col, args.group, args.model)

    # Print the result of the ANOVA analysis
    print("\nsuccess!\n")
    print(anova_result, "\n")
    
if __name__ == "__main__":
    main()

