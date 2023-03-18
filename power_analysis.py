
import numpy as np
import statsmodels.stats.power as smp

def power_analysis(group1, 
                   group2, 
                   sd, 
                   nobs):
    """Perform power analysis for two-sample t-test

    Parameters
    ----------
    group1 : float
        mean of group 1
    group2 : float
        mean of group 2
    sd : float
        pooled standard deviation
    nobs : int
        number of observations per group

    Returns
    -------
    power : float
        power of the test
    """
    # Calculate the effect size
    effect_size = (group1 - group2) / sd

    # Perform power analysis using statsmodels
    power = smp.TTestIndPower().solve_power(effect_size=effect_size, nobs1=nobs, alpha=0.05, power=None)

    return power

def main():
    import argparse

    # Define command line arguments
    parser = argparse.ArgumentParser(description='Perform power analysis for two-sample t-test')
    
    parser.add_argument('group1', 
            type=float, 
            help='mean of group 1')
    
    parser.add_argument('group2', 
            type=float, 
            help='mean of group 2')
    
    parser.add_argument('sd', 
            type=float, 
            help='pooled standard deviation')
    
    parser.add_argument('nobs', 
            type=int, 
            help='number of observations per group')

    # Parse the command line arguments
    args = parser.parse_args()

    # Perform power analysis
    power_analysis(args.group1, 
                   args.group2, 
                   args.sd, 
                   args.nobs)
    
if __name__ == '__main__':
    main()