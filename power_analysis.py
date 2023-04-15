import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.power import TTestPower, FTestAnovaPower

"""
I get an error when run t-test. From what I can tell online, this is due to an error with numby and statsmodels. It still completes, so there isnt anything to worry about. 
I need to create a chi-square dataset to test the chi-square function.
I need to create a two-sample t-test dataset to test the two-sample t-test function.
I would like to have the function plot a power curve like what is in g-power.
"""

def power_analysis(effect_size=0.5,
                   power=0.8,
                   alpha=0.05,
                   test='ANOVA',
                   path_to_power=None):
    """Perform power analysis for one-sample t-test or ANOVA test.

    Parameters
    ----------
    effect_size : float
        The size of the effect. For one-sample t-test, d is Cohen's d. For ANOVA, f is the effect size.
    power : float
        The desired power level. Default is 0.8.
    alpha : float
        The significance level. Default is 0.05.
    test : str
        The type of test to perform. Valid options are 'ANOVA', 't-test', 'chi-squared', or 'two-sample-t'.
    path_to_power : str
        The path to a CSV file containing relevant variables. Default is None.
    """
    # Error handling
    if not 0 <= alpha <= 1: # Check that alpha is between 0 and 1
        raise ValueError("alpha must be between 0 and 1")
    if not 0 <= power <= 1: # Check that power is between 0 and 1
        raise ValueError("power must be between 0 and 1")
    if test not in ['ANOVA', 't-test', 'chi-squared', 'two-sample-t']: # Check that the test type is valid
        raise ValueError("invalid test type")

    if path_to_power is not None: # If a path is supplied, read the CSV file
        # read csv file as a dataframe
        df = pd.read_csv(path_to_power)
        print("\nopening " + path_to_power + "\n")

        # extract the variables from the dataframe
        effect_size = df['effect_size'][0] # extract the effect size
        print("the effect size is " + str(effect_size) + "\n")
        power = df['power'][0] # extract the power
        print("the power is " + str(power) + "\n")
        alpha = df['alpha'][0] # extract the alpha
        print("the alpha is " + str(alpha) + "\n")
    else:
        print("\nPath not supplied. Using input values\n")
        print("the effect size is " + str(effect_size) + "\n")
        print("the power is " + str(power) + "\n")
        print("the alpha is " + str(alpha) + "\n")

    # Calculate the minimum sample size for the chosen test type
    if test == 'ANOVA':
        ftest = FTestAnovaPower()
        sample_size = ftest.solve_power(effect_size=effect_size, alpha=alpha, power=power)
        print("Minimum sample size required for ANOVA test with effect size {}, power {}, and alpha {}: {}".format(effect_size, power, alpha, int(np.ceil(sample_size))))
    elif test == 't-test':
        ttest = TTestPower()
        sample_size = ttest.solve_power(effect_size=effect_size, alpha=alpha, power=power)
        print("Minimum sample size required for one-sample t-test with effect size {}, power {}, and alpha {}: {}".format(effect_size, power, alpha, int(np.ceil(sample_size))))
    elif test == 'two-sample-t':
        ttest = TTestPower()
        sample_size = ttest.solve_power(effect_size=effect_size, alpha=alpha, power=power, ratio=1.0, alternative='two-sided')
        print("Minimum sample size required for two-sample t-test with effect size {}, power {}, and alpha {}: {}".format(effect_size, power, alpha, int(np.ceil(sample_size))))
    elif test == 'chi-squared':
        from scipy.stats import chi2_contingency

        # Calculate the minimum expected cell count for the chi-squared test
        # Expected cell count should be greater than or equal to 5 for accurate results
        min_expected_count = 5

        # Get degrees of freedom for the test
        df = df['df'][0] if path_to_power is not None else None

        # Calculate the minimum sample size required for the chi-squared test
        sample_size = None
        while sample_size is None or sample_size % 1 != 0:
            # Increase sample size until expected cell count is greater than or equal to the minimum expected cell count
            if sample_size is None:
                sample_size = 1
            else:
                sample_size += 1
            
            # Generate random data based on the expected proportions
            proportions = np.random.dirichlet([1] * len(df))
            data = np.array([np.random.multinomial(sample_size, p) for p in proportions])
            
            # Check that the expected cell count is greater than or equal to the minimum expected cell count
            obs_count = data.sum()
            exp_count = data.mean() * data.size
            if exp_count < min_expected_count:
                continue
            
            # Perform chi-squared test and check for statistical significance
            _, p, _, _ = chi2_contingency(data)
            if p <= alpha:
                break
        
        print("Minimum sample size required for chi-squared test with effect size {}, power {}, alpha {}, and degrees of freedom {}: {}".format(effect_size, power, alpha, df, sample_size))

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
            help='type of test to perform (default: ANOVA)')
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