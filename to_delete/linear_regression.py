import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def linear_regression(x = "petal_length_cm", # x variable in the garph
                      y = "sepal_length_cm", # y variable in the graph
                      x_lab = "Petal Length (cm)", # x axis label
                      y_lab = "Sepal Length (cm)", # y axis label
                      output = "linear_regression",  # output file name
                      group = "species", # group to subdivide dataset
                      path = "iris.csv"): # Function to perform linear regression on the data
    
    """Perform linear regression and create a graph containing slope and trendline.

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
        The path to the data file #Should I include a second path to an excel file that contains x_lab and y_lab?

    Returns
    -------
    slopes : list
        A list of the slopes of the linear regression for each group.
    intercepts : list
        A list of the intercepts of the linear regression for each group.
    r_values : list
        A list of the correlation coefficients for each group.
    p_values : list
        A list of the p-values for each group.
    stderrs : list
        A list of the standard errors for each group.
    """

    try: # Try to read the data file
        dataframe = pd.read_csv(path) 
    except FileNotFoundError: # If the file is not found, print an error message
        print("Error: File not found") 
        return
    except pd.errors.EmptyDataError: # If the file is empty, print an error message
        print("Error: Empty dataframe")
        return
    except pd.errors.ParserError: # If the file cannot be parsed, print an error message
        print("Error: Could not parse the file")
        return
    except Exception as e: # If there is an unknown error, print an error message
        print("Error:", e)
        return
    
    print("\nreading data from ", path)
    
    if group not in dataframe.columns: # If the group is not in the dataframe, plot all data
        print("\nGroup not found in dataframe. Plotting all data.")
        x_data = dataframe[x] # Set x_data to the x variable
        y_data = dataframe[y] # Set y_data to the y variable
        regression = stats.linregress(x_data, y_data) # Perform linear regression
        slope = regression.slope # Set slope to the slope of the linear regression
        intercept = regression.intercept # Set intercept to the intercept of the linear regression

        plt.scatter(x_data, y_data) # Plot the data
        plt.plot(x_data, slope * x_data + intercept, label = 'Fitted line') # Plot the trendline
        plt.xlabel(x_lab) # Set the x axis label
        plt.ylabel(y_lab) # Set the y axis label
        print("\nx axis label: ", x_lab) 
        print("\ny axis label: ", y_lab) 
        plt.legend() # Show the legend
        save = output + ".png" # Set the output file name
        print("\nsaving plot to ", save) 
        plt.savefig(save) # Save the plot
        print("\nplot saved!")
    
    if group in dataframe.columns: # If the group is in the dataframe, plot each group
        for i in dataframe[group].unique(): # For each unique group
            print("\nplotting ", i) 
            x_data = dataframe[dataframe[group] == i][x] # Set x_data to the x variable for the group
            y_data = dataframe[dataframe[group] == i][y] # Set y_data to the y variable for the group
            
            if x_data.empty or y_data.empty: # If the data is empty, print an error message
                print("Error: Empty data")
                continue

            regression = stats.linregress(x_data, y_data) # Perform linear regression
            slope = regression.slope # Set slope to the slope of the linear regression
            intercept = regression.intercept # Set intercept to the intercept of the linear regression

            plt.scatter(x_data, y_data, label = i) # Plot the data
            plt.plot(x_data, slope * x_data + intercept, label = 'Fitted line') # Plot the trendline
            plt.xlabel(x_lab) # Set the x axis label
            plt.ylabel(y_lab) # Set the y axis label
            print("\nx axis label: ", x_lab)
            print("\ny axis label: ", y_lab)
            plt.legend() # Show the legend
            save = output + "_" + i + ".png" # Set the output file name
            print("\nsaving plot to ", save)
            plt.savefig(save) # Save the plot
            print("\nplot saved!")
            plt.clf() # Clear the plot

        print("\nAll plots generated!")

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

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    linear_regression(
            args.x,
            args.y, 
            args.x_lab,
            args.y_lab,
            args.output,
            args.group,
            args.path)

if __name__ == "__main__":
    main()