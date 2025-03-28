#!/usr/bin/env python3

import argparse
from sacrebleu.metrics import BLEU


def parse_args():
    """
    Parsea los argumentos de línea de comandos.
    :return: Los argumentos parseados.
    """
    parser = argparse.ArgumentParser(description="Evaluation of Speech Translation")
    parser.add_argument("--ref", required=True, help="path of reference text file")
    parser.add_argument("--hyp", required=True, help="path of hypothesis text file")
    args = parser.parse_args()
    return args 


def read_hypotheses_file(path):
    """
    Lee el archivo de hipótesis y lo retorna como una lista de strings.
    :param path: La ruta del archivo de hipótesis.
    :return: Una lista de strings, cada uno siendo una hipótesis.
    """
    with open(path, 'r', encoding='utf-8') as f:
        hypotheses = [line.strip() for line in f]
    return hypotheses


def read_references_file(path):
    """
    Lee el archivo de referencias y lo retorna como una lista de listas de strings.
    :param path: La ruta del archivo de referencias.
    :return: Una lista de listas de strings, cada lista interna siendo las referencias para una hipótesis.
    """
    references = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            references.append([line.strip()])
    return references


def calculate_bleu(hypotheses, references):
    """
    Calcula el puntaje BLEU para una lista de hipótesis y sus referencias.
    :param hypotheses: La lista de hipótesis.
    :param references: La lista de referencias.
    :return: El puntaje BLEU.
    """
    bleu = BLEU()
    return bleu.corpus_score(hypotheses, references)


def write_output_file(result, path):
    """
    Escribe el puntaje BLEU en un archivo de texto.
    :param result: El puntaje BLEU a escribir.
    :param path: La ruta del archivo de salida.
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(result))


def main():
    """
    Función principal que lee los archivos de hipótesis y referencias, calcula el puntaje BLEU y lo imprime.
    """
    args = parse_args()
    hypotheses = read_hypotheses_file(args.hyp)
    references = read_references_file(args.ref)
    bleu_score = calculate_bleu(hypotheses, references)
    print(f"BLEU score: {bleu_score}")
    write_output_file(bleu_score, "output.txt")


if __name__ == "__main__":
    main()
