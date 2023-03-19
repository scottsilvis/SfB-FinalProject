import pandas as pd
from Bio import SeqIO


def read_data(path_data = "data.csv",
              path_fasta = "test.fasta",
              path_power = "power.csv"):

    # Read in the data
    data = pd.read_csv(path_data)


    # Use SeqIO to read in the fasta file
    fasta_file = "test.fasta" #path_fasta
    sequences = {} #create an empty dictionary to store the sequences

    for seq_record in SeqIO.parse(fasta_file, "fasta"): #parse the fasta file
        sequence_id = seq_record.id #get the sequence id
        sequence = str(seq_record.seq) #get the sequence
        sequences[sequence_id] = sequence #add the sequence to the dictionary

    for sequence_id, sequence in sequences.items():
        print(f">{sequence_id}\n{sequence}\n")
    
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
    import subprocess

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--data',    
            type=str,
            default= None,
            help=('data file in .csv format. ' 
                  'default: data.csv'))
    parser.add_argument('-f', '--fasta', 
            type=str,
            default= None,
            help=('fasta file containing sequence data. '
                  'default: test.fasta'))
    parser.add_argument('-p', '--path_power', 
            help="Path to power_analysis.py script")
    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # Check to see if data file was provided by the caller. If not,
    # use the defaults.
    if not args.data:
        args.data = "data.csv"

    # Check to see if fasta file was provided by the caller. If not,
    # use the defaults.
    if not args.fasta:
        args.fasta = "test.fasta"

    #Return the input file, output file, and terms
    print('data file: ', args.data, '\nfasta file: ', args.fasta, '\n')

    # Call the search_text function   
    read_data(path_data = args.data, 
                path_fasta= args.fasta)
    
    if args.path_power:
        #power_analysis
        print("executing power_analysis.py")

if __name__ == '__main__':
    main()