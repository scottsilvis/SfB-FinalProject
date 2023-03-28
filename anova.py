import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def ANOVA(data, x, y, model='1-way', plot_type='boxplot', figsize=(8,6)):
    """
    Perform ANOVA analysis on a given dataset and create a plot of the result.

    Parameters:
    data: pandas.DataFrame - The dataset to be analyzed.
    x: str - The name of the column containing the independent variable.
    y: str - The name of the column containing the dependent variable.
    model: str - The type of ANOVA to be performed. Default is '1-way'. Other options include '2-way', 
                  'repeated-measures', and 'MANOVA'.
    x_lab: str - The label for the x-axis. Default is the name of the x column.
    y_lab: str - The label for the y-axis. Default is the name of the y column.
    output: str - The name of the output file. Default is 'anova'.
    plot_type: str - The type of plot to be created. Default is 'boxplot'. Other options include 'violinplot', 
                     'swarmplot', and 'pointplot'.
    figsize: tuple - The size of the plot to be created. Default is (8,6).

    Returns:
    anova_result: pandas.DataFrame - The result of the ANOVA analysis.
    """

    # Perform 1-way ANOVA
    if model == '1-way':
        groups = [group[y] for name, group in data.groupby(x)]
        anova_result = stats.f_oneway(*groups)

    # Perform 2-way ANOVA
    elif model == '2-way':
        formula = f"{y} ~ {x} + {x} * C({y})"
        model = ols(formula, data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        anova_result = anova_table['F'][0:len(data[x].unique())]

    # Perform repeated-measures ANOVA
    elif model == 'repeated-measures':
        formula = f"{y} ~ C({x}) + C({x}, Treatment(reference='1'))*Time"
        model = ols(formula, data).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        anova_result = anova_table['F'][0:len(data[x].unique())]

    # Perform MANOVA
    elif model == 'MANOVA':
        y_var = [var for var in data.columns if var != x]
        manova_result = sm.multivariate.manova.MANOVA(data[y_var], data[x]).mv_test()
        anova_result = manova_result.results['x0']['stat'].iloc[0:len(data[x].unique())]

    else:
        raise ValueError(f"Invalid ANOVA model type: {model}")
    
    # Create plot
    fig, ax = plt.subplots(figsize=figsize)
    if plot_type == 'boxplot':
        boxprops = dict(linewidth=2, color='black')
        medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
        whiskerprops = dict(linewidth=2, color='black')
        capprops = dict(linewidth=2, color='black')
        bp = ax.boxplot(groups, boxprops=boxprops, medianprops=medianprops, whiskerprops=whiskerprops, capprops=capprops, patch_artist=True)

        # Set colors for the boxplot
        colors = ['lightblue', 'lightgreen', 'pink', 'tan']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)

        # Set labels for x-axis and y-axis
        ax.set_xticklabels(group_names)
        ax.set_ylabel(y_label)

        # Set title for the plot
        ax.set_title(title)

    elif plot_type == 'violinplot':
        parts = ax.violinplot(groups, showmeans=False, showmedians=True, showextrema=True)
        for pc in parts['bodies']:
            pc.set_facecolor('lightblue')
            pc.set_edgecolor('black')
            pc.set_alpha(1)

        # Set labels for x-axis and y-axis
        ax.set_xticklabels(group_names)
        ax.set_ylabel(y_label)

        # Set title for the plot
        ax.set_title(title)

    else:
        raise ValueError("Invalid plot type. Choose either 'boxplot' or 'violinplot'.")

    plt.show()

def main(): # Function to call the linear regression function
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser()
    
    # Tell the parser what command-line arguments this script can receive
    parser.add_argument('data', 
                        help='The name of the data file.')
    parser.add_argument('x',
                        help='The name of the column containing the independent variable.')
    parser.add_argument('y',
                        help='The name of the column containing the dependent variable.')
    parser.add_argument('-m', '--model',
                        help='The type of ANOVA to be performed. Default is 1-way ANOVA.',
                        choices=['1-way', '2-way', 'repeated-measures', 'MANOVA'],
                        default='1-way')
    parser.add_argument('-p', '--plot_type',
                        help='The type of plot to be created. Default is boxplot.',
                        choices=['boxplot', 'violinplot', 'swarmplot', 'pointplot'],
                        default='boxplot')
    parser.add_argument('-f', '--figsize',
                        help='The size of the plot to be created. Default is (8,6).',
                        nargs=2,
                        type=int,
                        default=(8,6))
    parser.add_argument('-o', '--output',
                        help='The name of the output file. Default is anova.',
                        default='anova')
    
    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    ANOVA(args.data, 
          args.x, 
          args.y, 
          args.model, 
          args.plot_type, 
          args.figsize, 
          args.output)
    
if __name__ == "__main__":
    main()

