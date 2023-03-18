# SfB-FinalProject

# Project Proposal

For my class project, I would like to create a script to handle much of the data analysis that I perform on routine projects. These projects primarily consist of vaccine effacy studies which may or may not have genetic sequence data associated with it. 

I would like to have the ability to run power analyses, with the scripts handling the majority of the work and only the bare minimum input from me being required. 

Antibody data will generally be present. I would like to be able to give a dataframe or excel document and have the function automatically caculate the geometic mean from the data I provide. From there I would need functionalty to run the basic tests we typically perform (ANOVA, Repeated Measures ANOVA, Mann Whitney U, etc). Again I would like our typical option selection to be already input so I only need to give the bare minimun. 

When genetic sequence data is present I would like to have the ability to run a MAAFT alignment (if RNA or DNA) or Clustal alignment (if protein), and create an RAxML tree following procedures for each sequence type. 

Occasionally we will analyze the sequence data or antibody data with PCA. Having that functionality available, but in a more versitile form would be nice (more options available to modify). 

Lastly, having a simplified way of producing the common tables and figures would be great. 

## Outline

script 1: Input data here

The file should be simple to read and understand.

Read_csv in r
Read_Excel in r
Maybe using pandas library in Python
Once data is in, I will need to assign appropriate variables to the data based on the column headings in the data set.

Assign Home Location for outputs

Maybe a section that allows me to choose which tests I would like to run? If that is included, a section that allows me to choose if sequence data is present, where it can be found, and what tests to run using the sequence data. 

Assign Variables

    Animal
    Timepoint
    Antibody (We will often measure antibody with multiple viruses, a good way to distinguish these but still have them be discernable by future functions)
    Sequence (y/n?)
    Group
    ...

PowerAnlysis(Variable1, Variable2)- Can easily be done in R

Power Analysis output

if antibody present convert to geometric mean (can use the geometric mean function available in the scipy library in Python, or the geom.mean() function in the dplyr library in R).

ANOVA lme4, to perform ANOVA, repeated measures ANOVA, and Mann Whitney U tests.
ANOVA graph

RM-ANOVA
RM-ANOVA graph
 
plus more (can use functions like aov(), lm(), or wilcox.test() depending on the type of statistical test you need to perform.)

Scipt 2-n:

This is where the majority of the code should be hidden. I think a script for each test would be best. I imagine this would simplify things signficanly. The Scipt 1 would only need to call the second function with the approproate variables. 

Options for Nucleotide and Protein Alignments (Python): Biopython(Not sure Yet), Mafft(Only DNA/RNA?), and Clustal Omega (Only Protein?). I would prefer MAAFT for DNA/RNA and Clustal for Protein if there is any cross over. 

PCA - prcomp() function in R or the PCA() function in Python's scikit-learn library.

Tables and Figures - ggplot2 and knitr? 

### Background information

I have previously used R for the majority of my data analysis and table/figure generation. I may stick with R, or use a combination of R and python where necessary (if possible, I am not sure how compatable the two are). I typically use RStudio for this, but maybe that isnt necessary. I know that some things like the alignment tools are typically written in python, so I think there will need some interaction between the two. 

### The code

