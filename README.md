# SfB-FinalProject

This group of scripts is capable of analyzing data using multiple statitcal approaches. 


1. The scrips are able to calculate the necessary sample size to have statistical power using the power_analysis.py package. The necessary inputs are effect size, power level, level of significance (alpha), and the type of test you would like to perform (ANOVA, 1-sample t-test, 2-sample t-test, chi-squared test). The results are returned in the terminal. 


2. The scripts can calculate the F statistic and p value for a 1-way ANOVA, 2-way ANOVA, repeated-measures ANOVA, and MANOVA. This analyis is done using the anova.py script, and requires a path input (to the data), the name of the dependent variable, the name of the independent variable, and the type of ANOVA you want to perform. The results are returned in the terminal. 


3. The scripts can calculate the slope, intercept, r value and p value of a linear regression analysis, using the file linear_regression.py. The file requires the inputs x, y, x_lab, y_lab, output, group, path, save plots, point color and line color. the variable x, y, and group correspond to the column headers in the data input file (path). the x_lab and y_lab variables are what you want the axes to be labed as for the plots generated, which can be saved by inputting true or false for the save plots variable. The point color and line color variables dictate the point and line color in the plots, and the output variable selects the title for the output graphs, which are stored as png fles. If the group varibale is populated, individual graphs will be made for each group, and the output will have the group name appended to the title of the file. 


4. The alignment tool MAAFT and the tree building tool RAxML have been inplemented into the stats.py file, and are capable of generating a MAAFT alignment from a fasta file (dictated by the user) and a phylogenetic tree is built from this alignment (or any alignment selected by the user). The stats.py file is the preferred way to interface with the other files. Upon calling the file, a interactive script will prompt the user to populate the variables and list file locations before executing the scripts. If multiple tests are needed, the script will need to be executed multiple times. 

For ease of testing, there are default values that are coded into each package (eg. If anova.py is called with nothing else, a default ANOVA will execute using the data.csv file). Simply calling variables is enough to circumvent this testing feature. Simmilarly, each test in the stats.py file also has default vales included. The test will prompt "would you like to use the default value? y/n" and by selecting "y", these values will be used instead of user supplied values. 
