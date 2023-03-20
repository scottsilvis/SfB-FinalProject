import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import pandas as pd

def ANOVA():
    """Perform one-way or two-way ANOVA.

    Parameters
    ----------
  
    """
    # read csv file as a dataframe
    data = pd.read_csv('data.csv')
    print("\nopening data.csv\n")

    # Assign variables - include a print statement to check that the variables are being assigned
    animal = data['Animal'] #comes from csv file
    print("variable animal assigned")
    print(animal)
    timepoint = data['Timepoint'] #comes from csv file
    print("variable timepoint assigned")
    print(timepoint)
    antibody = data['Antibody'] #comes from csv file
    print("variable antibody assigned")
    print(antibody)
    group = data['Group'] #The variable exists in the csv file, but it is empty. This seems to work just fine. 
    print("variable group assigned")
    print(group)
    #treatment = data['Treatment'] #If the variable doesnt exist, it will throw an error. Need to fix this. 
    print("variable treatment assigned")
    
def main():
    import argparse

    # Define command line arguments
    parser = argparse.ArgumentParser(description='Perform power analysis for one-sample t-test or ANOVA test.')
    
    parser.add_argument('-a', '--animal', 
            help='animal name')
    
    parser.add_argument('-t', '--timepoint', 
            type=float, 
            help='day or time of sample collection')
    
    parser.add_argument('-ab', '--antibody', 
            type=float, 
            help='antibody titer')
    
    parser.add_argument('-g', '--group',
            type=float, 
            default=1.5,
            help='standard deviation of the population (default: 1.5)')
    
    parser.add_argument('-pp', '--path', 
            type=str, 
            default=None,
            help='path csv file containing relevent variables (default: power.csv)')

    # Parse the command line arguments
    args = parser.parse_args()

    # Perform power analysis
    ANOVA(args.animal,
                   args.timepoint,
                   args.antibody,
                   args.group,
                   args.path)
    
if __name__ == '__main__':
    main()