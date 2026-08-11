# Python DNA Mutation Analyzer

A simple Python-based bioinformatics project that compares two DNA sequences, aligns them using the **Needleman-Wunsch global sequence alignment algorithm**, identifies mutations, and analyzes their potential effects on protein sequences.

This project was created to help me learn and explore an intersection of **computer science and biology** while practicing Python, dynamic programming, and basic bioinformatics concepts.

## Technologies

* **Python**
* Needleman-Wunsch Sequence Alignment
* Basic Molecular Biology / Genetics
* Amino Acid and Codon Analysis

## Features

* Validate DNA sequences
* Compare the lengths of two DNA sequences
* Perform global sequence alignment using the Needleman-Wunsch algorithm
* Detect:

  * Substitutions
  * Insertions
  * Deletions
* Transcribe DNA sequences into RNA
* Divide sequences into codons
* Translate codons into amino acids
* Classify point mutations as:

  * Silent
  * Missense
  * Nonsense

## How to Run

### Requirements

* Python 3.x
* Git (optional, if cloning the repository)

### 1. Clone the Repository

```bash
gh repo clone Thedirtt/PythonMutation
cd PythonMutation
```

### 2. Run the Program

Run the main Python file:

```bash
python Main.py
```

Depending on your system, you may need to use:

```bash
python3 Main.py
```

### 3. Enter DNA Sequences

The program will prompt you to enter two DNA sequences:

```text
Please Enter your first DNA Sequence: ATGCCATGCTAAGCT
Please Enter your Second DNA Sequence: ATGCCGTCTAAGCT
```

The program will then:

1. Validate both DNA sequences.
2. Compare their lengths.
3. Perform Needleman-Wunsch global sequence alignment.
4. Identify insertions, deletions, and point mutations.
5. Analyze point mutations and classify their potential effects as silent, missense, or nonsense mutations.

## How It Works

The program takes two DNA sequences from the user as input:

```text
Original DNA: ATGCCATGCTAAGCT
Mutated DNA:  ATGCCGTCTAAGCT
```

The sequences are first validated to make sure they contain only valid DNA nucleotides:

```text
A = Adenine
T = Thymine
C = Cytosine
G = Guanine
```

The program then uses the **Needleman-Wunsch algorithm** to globally align the two sequences. This allows the program to identify insertions and deletions that would not be detected by simply comparing the sequences otherwise.

example:

```text
Original: ATGCCATGCTA
Mutated:  ATGCC-GCTA
```

The `-` represents a gap introduced during sequence alignment.

### Needleman-Wunsch

Needleman-Wunsch is a dynamic programming algorithm used to find an optimal global alignment between two biological sequences.

The algorithm constructs a scoring matrix where each cell represents the best possible alignment score up to that point.

For this implementation, the scoring system is currently:

```text
Match:       +1
Mismatch:    -1
Gap:         -1
```

After constructing the matrix, the program performs a traceback from the bottom-right corner to determine the optimal alignment.

The implementation was written from scratch as part of this project.

## Mutation Analysis

After alignment, the program examines the sequences to identify differences.

### Substitution

A nucleotide is replaced by another nucleotide.

```text
Original: ATGCCA
Mutated:  ATGGCA
             ^
             C → G
```

### Insertion

A nucleotide or sequence of nucleotides is added.

```text
Original: ATGCA
Mutated:  ATGCCA
              ^
```

### Deletion

A nucleotide or sequence of nucleotides is removed.

```text
Original: ATGCCA
Mutated:  ATGCA
             ^
```

## Mutation Effects

For point mutations, the program converts the DNA sequence to RNA and divides it into groups of three nucleotides called **codons**.

Each codon corresponds to an amino acid or a stop signal.

The program compares the amino acids produced by the original and mutated sequences.

### Silent Mutation

A nucleotide changes, but the resulting amino acid remains the same.

```text
Codon 1: GAA → GAG
Amino acid: Glutamic Acid → Glutamic Acid
```

### Missense Mutation

A nucleotide change results in a different amino acid.

```text
Codon 1: GAA → GTA
Amino acid: Glutamic Acid → Valine
```

### Nonsense Mutation

A mutation changes a codon into a stop codon.

```text
Codon 1: TGG → TAG
Amino acid: Tryptophan → STOP
```

## Example

Example input:

```text
Please Enter your first DNA Sequence: ATGCCATGCTAAGCT
Please Enter your Second DNA Sequence: ATGCCGTCTAAGCT
```

The program validates both sequences and performs the alignment.

Example output:

```text
Sequence 1 is Valid DNA
Sequence 2 is Valid DNA

DNA is the Same Length

Results of the Needleman-Wunsch Algorithm:
ATGCCATGCTAAGCT
ATGCCGTCTAAGCT

Point mutation at pos 5
```

The program then analyzes the codons to determine the potential effect of the mutation.

## Project Structure

```text
DNA-Mutation-Analyzer/
│
├── main.py
├── codon_table.py
└── README.md
```

## Current Limitations

This project is currently a learning project and has several limitations.

* Insertions and deletions can cause a frameshift, which requires additional analysis.
* The current scoring system uses fixed match, mismatch, and gap scores.
* The program currently works with relatively small sequences entered directly by the user.
* It does not currently retrieve or analyze real-world genomic datasets.

## Possible Improvements

Possible improvements if this program was expanded on could include:

* [ ] Improve insertion/deletion and frameshift analysis
* [ ] Add support for FASTA files
* [ ] Improve mutation reporting
* [ ] Add automated tests
* [ ] Add sequence statistics such as GC content
* [ ] Allow customizable Needleman-Wunsch scoring parameters
* [ ] Compare results against established bioinformatics libraries
* [ ] Support larger biological datasets
* [ ] Add visualization of sequence alignments
* [ ] Add analysis of real genomic variants

## Why I Built This

I am a Computer Science/Biology student interested in the intersection of **computer science, biology, and computational evolution**.

I built this project to strengthen my Python skills while learning new algorithms can be applied to biology.

The long-term goal is to continue expanding the project as I learn more about **bioinformatics, genomics, and computational biology**.
