import subprocess
from Bio.Align.Applications import MafftCommandline
from Bio import AlignIO
from io import StringIO

print("executing stats.py")

# Get user input
user_input = input("What test would you like to run? (ANOVA, power analysis, linaer regression, sequence alignment, RAxML tree generation) ")

# Check to see if the user input is valid
if user_input == "ANOVA":
        print("executing anova.py")
        answer = input("Would you like to use the default values? (y/n) ")
        if answer == "y":
                path = "data.csv"
                x_col = "Group"
                y_col = "Antibody"
                group = "Group"
                model = "1-way"
                subprocess.call(["python", "anova.py", "-d", path, "-x", x_col, "-y", y_col, "-g", group, "-m", model])
        elif answer == "n":
                path = input("What is the path to the data file? default is 'data.csv' ")
                x_col = input("What is the name of the column containing the independent variable? default is 'Group' ")
                y_col = input("What is the name of the column containing the dependent variable? default is 'Antibody' ")
                group = input("What is the name of the column containing the group variable? default is 'Group' ")
                model = input("What is the type of ANOVA to be performed? default is '1-way' ")
                subprocess.call(["python", "anova.py", "-d", path, "-x", x_col, "-y", y_col, "-g", group, "-m", model])
        else:
                print("Invalid input. Please try again.")
        
elif user_input == "power analysis":
        print("executing power_analysis.py")
        answer = input("Would you like to use the default values? (y/n) ")
        if answer == "y":
                effect_size = "0.5"
                power = "0.8"
                alpha = "0.05"
                test = "ANOVA"
                subprocess.call(["python", "power_analysis.py", "-e", effect_size, "-p", power, "-a", alpha, "-t", test])
        elif answer == "n":
                effect_size = input("What is the effect size? default is 0.5 ")
                power = input("What is the power? default is 0.8 ")
                alpha = input("What is the alpha? default is 0.05 ")
                test = input("What is the test? default is 'ANOVA' ")
                subprocess.call(["python", "power_analysis.py", "-e", effect_size, "-p", power, "-a", alpha, "-t", test])
        else:
                print("Invalid input. Please try again.")

elif user_input == "linear regression":
        print("executing linear_regression.py")
        answer = input("Would you like to use the default values? (y/n) ")
        if answer == "y": # Default values
                x = "petal_length_cm"
                y = "sepal_length_cm"
                x_lab = "Petal Length (cm)"
                y_lab = "Sepal Length (cm)"
                output = "linear_regression"
                group = "species"
                path = "iris.csv"
                save_plots = "True"
                point_color = "b"
                line_color = "r"
                subprocess.call(["python", "linear_regression.py", "-x", x, "-y", y, "-x_lab", x_lab, "-y_lab", y_lab, "-output", output, "-group", group, "-path", path, "-save_plots", save_plots, "-point_color", point_color, "-line_color", line_color])
        elif answer == "n": # User defined values
                x = input("What is the name of the column containing the independent variable? default is 'petal_length_cm' ")
                y = input("What is the name of the column containing the dependent variable? default is 'sepal_length_cm' ")
                x_lab = input("What is the label for the x-axis? default is 'Petal Length (cm)' ")
                y_lab = input("What is the label for the y-axis? default is 'Sepal Length (cm)' ")
                output = input("What is the name of the output file? default is 'linear_regression' ")
                group = input("What is the name of the column containing the group variable? default is 'species' ")
                path = input("What is the path to the data file? default is 'iris.csv' ")
                save_plots = input("Would you like to save the plots? default is 'True' ")
                point_color = input("What color would you like the points to be? default is 'b' ")
                line_color = input("What color would you like the line to be? default is 'r' ")
                subprocess.call(["python", "linear_regression.py", "-x", x, "-y", y, "-x_lab", x_lab, "-y_lab", y_lab, "-output", output, "-group", group, "-path", path, "-save_plots", save_plots, "-point_color", point_color, "-line_color", line_color])
        else:
                print("Invalid input. Please try again.")

elif user_input == "sequence alignment":
        print("executing sequence_alignment.py")
        answer = input("Would you like to use the default values? (y/n) ")
        if answer == "y":
                input_file = "test.fasta"
                output_file = "alignment.fasta"

                # Execute Mafft alignment
                mafft_cline = MafftCommandline(input=input_file)
                stdout, stderr = mafft_cline()
                alignment = AlignIO.read(StringIO(stdout), "fasta")

                # Write output to file
                AlignIO.write(alignment, output_file, "fasta")

        elif answer == "n":
                # Define input and output file paths
                input_file = input("What is the path to the fasta file? default is 'test.fasta' ")
                output_file = input("What is the name of the output file? default is 'alignment' ")

                # Execute Mafft alignment
                mafft_cline = MafftCommandline(input=input_file)
                stdout, stderr = mafft_cline()
                alignment = AlignIO.read(StringIO(stdout), "fasta")

                # Write output to file
                AlignIO.write(alignment, output_file, "fasta")
        else:
                print("Invalid input. Please try again.")

elif user_input == "RAxML tree generation":
        print("executing RAxML tree generation")
        answer = input("Would you like to use the default values? (y/n) ")
        if answer == "y":
                input_file = "alignment.fasta"
                output_file = "tree.txt"

                # Read Mafft alignment and write to phylip format
                alignment = AlignIO.read(input_file, "fasta")
                AlignIO.write(alignment, output_file, "phylip")

                # Call RAxML from command line
                cmd = ["raxmlHPC-PTHREADS", "-T", "2", "-m", "GTRGAMMA", "-s", input_file, "-n", "output", "-p", "12345"]
                subprocess.run(cmd)
        elif answer == "n":
                # Define input and output file paths
                input_file = input("What is the path to the fasta file? default is 'test.fasta' ")
                output_file = input("What is the name of the output file? default is 'tree' ")

                # Read Mafft alignment and write to phylip format
                alignment = AlignIO.read(input_file, "fasta")
                AlignIO.write(alignment, output_file, "phylip")

                # Call RAxML from command line
                cmd = ["raxmlHPC-PTHREADS", "-T", "2", "-m", "GTRGAMMA", "-s", input_file, "-n", "output", "-p", "12345"]
                subprocess.run(cmd) 
        else: 
                print("Invalid input. Please try again.")

        
else:
        print("Invalid input. Please try again.")

