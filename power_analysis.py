import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import pandas as pd

def power_analysis(effect_size=0.5,
                   power=0.8,
                   alpha=0.05,
                   sd=1.5,
                   k=0,
                   n=0,
                   path_to_power =None):
    """Perform power analysis for one-sample t-test or ANOVA test.

    Parameters
    ----------
    effect_size : float
        The size of the effect. For one-sample t-test, d is Cohen's d. For ANOVA, f is the effect size.
    power : float
        The desired power level. Default is 0.8.
    alpha : float
        The significance level. Default is 0.05.
    sd : float
        The standard deviation of the population. Default is 1.5. Only used for one-sample t-test.
    k : int
        The number of groups in the study. Only used for ANOVA.
    n : int
        The total sample size. Only used for ANOVA.
    path_to_power : str
        The path to the power.csv script. Default is power.csv.
        This option bypasses the other arguments.
    """
    if path_to_power is not None:
        # read csv file as a dataframe
        df = pd.read_csv(path_to_power)
        print("\nopening " + path_to_power + "\n")

        # extract the variables from the dataframe
        effect_size = df['effect_size'][0]
        print("the effect size is " + str(effect_size) + "\n")
        power = df['power'][0]
        print("the power is " + str(power) + "\n")
        alpha = df['alpha'][0]
        print("the alpha is " + str(alpha) + "\n")
        sd = df['sd'][0]
        print("the sd is " + str(sd) + "\n")
        k = df['k'][0]
        n = df['n'][0]
    elif path_to_power is None:
        print("\nPath not supplied. Using input values\n")
        print("the effect size is " + str(effect_size) + "\n")
        print("the power is " + str(power) + "\n")
        print("the alpha is " + str(alpha) + "\n")

    if k != 0: # I want to check if k is empty in the csv, but it just returns nan. Temp solution is to check if k is 0.
        print("the number of groups in the study is " + str(k) + "\n")
    if n != 0:
        print("the required sample size is " + str(n) + "\n")

    # Load the pwr package
    pwr = importr('pwr')

    # Convert the variables to R vectors
    r_effect_size = robjects.FloatVector([effect_size])
    r_power = robjects.FloatVector([power])
    r_alpha = robjects.FloatVector([alpha])
    r_k = robjects.IntVector([k])
    r_n = robjects.IntVector([n])

    print("All variables have been converted to R vectors. \n")
    # Calculate the minimum sample size for an ANOVA test
    if k == 0 and n != 0:
        sample_size = pwr.pwr_anova_test(n=r_n, f=r_effect_size, sig_level=r_alpha, power=r_power)
    elif k != 0 and n == 0:
        sample_size = pwr.pwr_anova_test(k=r_k, f=r_effect_size, sig_level=r_alpha, power=r_power)
    # Calculate the minimum sample size for a one-sample t-test
    else:
        sample_size = pwr.pwr_t_test(d=r_effect_size, power=r_power, sig_level=r_alpha, type = "one.sample")

    # Print the results
    print("The required sample size is " + str(sample_size[0]) + "\n")

    # Plot the power curve - This is not working yet. I need to figure out how to plot the power curve.
    #import matplotlib.pyplot as plt
    #print("Plotting the power curve...\n")
    #df.head()
    #print("Done!\n")
    
def main():
    import argparse

    # Define command line arguments
    parser = argparse.ArgumentParser(description='Perform power analysis for one-sample t-test or ANOVA test.')
    
    parser.add_argument('-e', '--effect_size', 
            type=float, 
            default=0.5,
            help='effect size (default: 0.5)')
    
    parser.add_argument('-p', '--power', 
            type=float, 
            default=0.8,
            help='desired power level (default: 0.8)')
    
    parser.add_argument('-a', '--alpha', 
            type=float, 
            default=0.05,
            help='significance level (default: 0.05)')
    
    parser.add_argument('-sd', '--sd',
            type=float, 
            default=1.5,
            help='standard deviation of the population (default: 1.5)')
    
    parser.add_argument('-k', '--k',
            type=int, 
            default=0,
            help='The number of groups in the study. Only used for ANOVA.')
    
    parser.add_argument('-n', '--n',
            type=int, 
            default=0, #If n is None then error is thrown. Temp solution is to set n to 0.
            help='The total sample size. Only used for ANOVA.')
    
    parser.add_argument('-pp', '--path', 
            type=str, 
            default=None,
            help='path csv file containing relevent variables (default: power.csv)')

    # Parse the command line arguments
    args = parser.parse_args()

    # Perform power analysis
    power_analysis(args.effect_size,
                   args.power,
                   args.alpha,
                   args.sd,
                   args.k,
                   args.n,
                   args.path)
    
if __name__ == '__main__':
    main()