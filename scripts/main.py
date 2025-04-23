import argparse
import os
import pandas as pd
from bleu_scorer import read_hypotheses_file, read_references_file, calculate_bleu
from chrF_scorer import computeChrF

import subprocess




def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Evaluate Speech Translation")
    parser.add_argument("--ref", required=True, help="Path to reference text file")
    parser.add_argument("--phyp", required=True, help="Path to folder of hypothesis text files")
    args = parser.parse_args()
    return args 

def validate_file(filename):
    """Validate the filename format."""
    parts = filename.split(".")
    if len(parts) != 6:
        print(f"Invalid filename: {filename}")
        return False
    if parts[1] != "st":
        print(f"Invalid filename: {filename}. Must contain 'st'.")
        return False
    if parts[2] not in ["constrained", "unconstrained"]:
        print(f"Invalid filename: {filename}. Must be 'constrained' or 'unconstrained'.")
        return False
    if parts[3] not in ["primary", "contrastive1", "contrastive2"]:
        print(f"Invalid filename: {filename}. Must be 'primary' or 'contrastive1' or 'contrastive2'.")
        return False
    if parts[4] != "que-spa":
        print(f"Invalid filename: {filename}. Must be 'que-spa'.")
        return False
    return True

def main():
    """Main function."""
    args = parse_args()
    
    if not os.path.exists(args.phyp):
        print(f"{args.phyp} does not exist.")
        return

    files = os.listdir(args.phyp)
    print(f"Number of files to process: {len(files)}")
    
    team = []
    condition = []
    bleu_scores = []
    types = []
    chrf_scores = []
    
    for file in files:
        print(f"Processing file: {file}")
        
        if not validate_file(file):
            continue

        # BLEU
        hypotheses = os.path.join(args.phyp, file)
        #references = read_references_file(args.ref)
        references = args.ref
        # Define el comando como una lista de argumentos
        command ="sacrebleu "+references+" -i "+ hypotheses +" -m bleu -lc"

        # Ejecuta el comando y captura la salida
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # La salida estará en result.stdout
        bleu_score = result.stdout
        #bleu_score = calculate_bleu(hypotheses, references)
        #bleu_score = str(bleu_score)
        #print(bleu_score)
        #bleu_result = float(bleu_score[6:11])
        #print(bleu_result)
        #if bleu_result < 200: 
            # chrF
        with open(args.ref, "r") as ref_file:
            with open(os.path.join(args.phyp, file), "r") as hyp_file:
                sentence_level_scores = None
                totalF, averageTotalF, totalPrec, totalRec = computeChrF(ref_file, hyp_file, 2, 6, 2.0, sentence_level_scores)
        chrf_score = f"{totalF * 100:.2f} (nc = 6 nw = 2 beta = 2.0)"
        # store results
        parts = file.split(".")
        team.append(parts[0])
        condition.append(parts[2])
        types.append(parts[3])
        bleu_scores.append(bleu_score)
        chrf_scores.append(chrf_score)

    # write results to file
    data = {"Participant": team, "Condition": condition, "Type": types, "BLEU": bleu_scores, "chrF": chrf_scores}
    df = pd.DataFrame(data)
    output_file = os.path.join(args.phyp, "results.tsv")
    df.to_csv(output_file, sep="\t", index=False)
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
