import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def linear_regression(x="petal_length_cm", 
                      y="sepal_length_cm", 
                      x_lab="Petal Length (cm)", 
                      y_lab="Sepal Length (cm)",
                      output="linear_regression", 
                      group="species", 
                      path="iris.csv", 
                      save_plots=True,
                      point_color='b', 
                      line_color='r'):
    """
    Perform linear regression and create a graph containing slope and trendline.

    Parameters
    ----------
    x : str
        The x-axis data. Default is "petal_length_cm".
    y : str
        The y-axis data. Default is "sepal_length_cm".
    x_lab : str
        The x-axis label. Default is "Petal Length (cm)".
    y_lab : str
        The y-axis label. Default is "Sepal Length (cm)".
    output : str
        The output file. Default is "linear_regression".
    group : str
        Variable to subdivide the data. Default is "species".
    path : str
        The path to the data file.
    save_plots : bool
        Whether to save the plots or not. Default is True.
    point_color : str
        The color of the scatter points. Default is 'b'.
    line_color : str
        The color of the trendline. Default is 'r'.

    Returns
    -------
    results : dict
        A dictionary containing the slope, intercept, r-value, p-value, and standard error for each group.
    """

    if not all(isinstance(arg, str) for arg in [x, y, x_lab, y_lab, output, group, path]): # Check if all arguments are strings
        raise ValueError("Input arguments must be strings")

    if not os.path.isfile(path): # Check if the file exists
        raise FileNotFoundError("File not found")

    dataframe = pd.read_csv(path) # Read the data file

    print(f"\nReading data from {path}")

    if group not in dataframe.columns: # Check if the group variable is in the dataframe
        print("\nGroup not found in dataframe. Plotting all data.")
        x_data = dataframe[x] # Set x_data to the x variable
        y_data = dataframe[y] # Set y_data to the y variable

        regression = stats.linregress(x_data, y_data) # Perform linear regression

        slope = regression.slope # Set slope to the slope of the linear regression
        intercept = regression.intercept # Set intercept to the intercept of the linear regression
        r_value = regression.rvalue # Set r_value to the correlation coefficient
        p_value = regression.pvalue # Set p_value to the p-value
        stderr = regression.stderr # Set stderr to the standard error

        plt.scatter(x_data, y_data, c=point_color) # Plot the data
        plt.plot(x_data, slope * x_data + intercept, c=line_color, label='Fitted line') # Plot the trendline
        plt.xlabel(x_lab) # Set the x-axis label
        plt.ylabel(y_lab) # Set the y-axis label
        plt.legend() # Show the legend

        if save_plots: # Save the plot if save_plots is True
            plt.savefig(f"{output}.png") 

        plt.show() # Show the plot

        return {"slope": slope, "intercept": intercept, "r_value": r_value, "p_value": p_value, "stderr": stderr}

    else: # If the group variable is in the dataframe
        print(f"\nGrouping data by {group}")
        groups = dataframe.groupby(group) # Group the data by the group variable

        results = {} # Create an empty dictionary to store the results

        for name, group_data in groups: # Loop through each group
            x_data = group_data[x] # Set x_data to the x variable
            y_data = group_data[y] # Set y_data to the y variable

            regression = stats.linregress(x_data, y_data) # Perform linear regression

            slope = regression.slope # Set slope to the slope of the linear regression
            intercept = regression.intercept # Set intercept to the intercept of the linear regression
            r_value = regression.rvalue # Set r_value to the correlation coefficient
            p_value = regression.pvalue # Set p_value to the p-value
            stderr = regression.stderr # Set stderr to the standard error

            plt.scatter(x_data, y_data, c=point_color, label=name) # Plot the data
            plt.plot(x_data, slope * x_data + intercept, c=line_color) # Plot the trendline
            plt.xlabel(x_lab) # Set the x-axis label
            plt.ylabel(y_lab) # Set the y-axis label
            plt.legend() # Show the legend

            if save_plots: # Save the plot if save_plots is True
                plt.savefig(f"{output}_{name}.png") 

            plt.show() # Show the plot

def main(): # Function to call the linear regression function
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser()

    # Tell the parser what command-line arguments this script can receive
    parser.add_argument("-x", 
                        help="The x-axis data", 
                        default="petal_length_cm",
                        required=False)
    parser.add_argument("-y", 
                        help="The y-axis data", 
                        default="sepal_length_cm",
                        required=False)
    parser.add_argument("-x_lab",
                        help="The x-axis label",
                        default="Petal Length (cm)",
                        required=False)
    parser.add_argument("-y_lab",
                        help="The y-axis label",
                        default="Sepal Length (cm)",
                        required=False)
    parser.add_argument("-output",
                        help="The output file",
                        default="linear_regression",
                        required=False)
    parser.add_argument("-group",
                        help="The group to plot",
                        #default="species",
                        required=False)
    parser.add_argument("-path",
                        help="The path to the data file",
                        default="iris.csv",
                        required=False)
    parser.add_argument("-save_plots",
                        help="Whether to save the plots or not",
                        default=True,
                        required=False)
    parser.add_argument("-point_color",
                        help="The color of the scatter points",
                        default="b",
                        required=False)
    parser.add_argument("-line_color",
                        help="The color of the trendline",
                        default="r",
                        required=False)

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    linear_regression(
            args.x,
            args.y, 
            x_lab=args.x_lab,
            y_lab=args.y_lab,
            output=args.output,
            group=args.group,
            path=args.path,
            save_plots=args.save_plots,
            point_color=args.point_color,
            line_color=args.line_color)

if __name__ == "__main__":
    main()