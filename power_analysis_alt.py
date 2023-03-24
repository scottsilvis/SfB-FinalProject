import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.power import TTestPower, FTestAnovaPower

def power_analysis(effect_size=0.5,
                   power=0.8,
                   alpha=0.05,
                   test = 'ANOVA',
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
    elif path_to_power is None:
        print("\nPath not supplied. Using input values\n")
        print("the effect size is " + str(effect_size) + "\n")
        print("the power is " + str(power) + "\n")
        print("the alpha is " + str(alpha) + "\n")


    # Calculate the minimum sample size for an ANOVA test
    if test == 'ANOVA':
        power_analysis = FTestAnovaPower()
        sample_size = power_analysis.solve_power(effect_size=effect_size, 
                                                 power=power, 
                                                 alpha=alpha,
                                                 alternative = 'one-sided')
    elif test == 't-test':
        power_analysis = TTestPower()
        sample_size = power_analysis.solve_power(effect_size=effect_size, 
                                                 power=power, 
                                                 alpha=alpha, 
                                                 alternative = 'one-sided')
    else:
        print("Please enter a valid test type. Valid options are 'ANOVA' or 't-test'")

    # Print the results
    print("The required sample size is " + str(sample_size))

    # Plot the power curve - This is not working yet. I need to figure out how to plot the power curve.
    power_analysis.plot_power(dep_var='nobs',
                          nobs=np.arange(sample_size/2, sample_size*2),
                          effect_size=np.array([effect_size-0.1, effect_size, effect_size+0.1]),
                          alpha=alpha,
                          title='Sample Size vs. Statistical Power')
    plt.savefig("power_analysis.png")
    print("\nplot saved!")
    
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
    parser.add_argument('-t', '--test',
            type=str,
            default='ANOVA',
            help='type of test t-test or ANOVA (default: ANOVA)')
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
                   args.test,
                   args.path)
    
if __name__ == '__main__':
    main()