# Doing BLAST on your local computer

BLAST: Compare & identify sequences

## Basic sequence format - FASTA

A fasta file is **Text file** begins with a single-line description, followed by lines of sequence data.

Introducing `.fasta`/`.fa`

```fasta
>DNA_Sequence_ID_1
ATCGCCGGTGACGTCTGCGTC
>DNA_Sequence_ID_2
TGGGCTAGCTAGTTATCTCCGCGCGGAAT
AGCTCTATTGTGTGTATTATAT
>DNA_Sequence_ID_3
TCGATCTCTTCTTATATATGCGCGGATCTAGGCTATATTCGATCGTAGCTA
```

```fasta
>Prot_Sequence_ID
VAETLKKGSRVTGAARDKLAADLKKKYDAGASIRALAEETGRSYGFVHRMLSESGVTLRG
RGGATRGKKATSA*
```

:::{NOTE}
1. Sequence data is always connected, nither 'space' nor 'line break' creates gap.
2. One or more sequence can be in one file
3. ID can contain 'space', but not 'line break'
4. Protein may contain '*' representing stop codon, but not necessarily
:::

Variants of file extensions:

- `.fna` fasta for Nucleotide (DNA and RNA)
- `.frn` fasta for RNA (RNA coding)
- `.faa` fasta for protein (Amino acid)
- `.ffn` fasta for protein coding DNA

## How BLAST works

- Which program
  - blastn
    - Query: nucleic acid sequence(s)
    - Database: nucleic acid sequences
  - blastp
    - Query: amino acid sequence(s)
    - Database: amino acid sequences
  - blastx
    - Query: nucleic acid sequence(s)
    - Automatically translate **query** to amino acid sequences (all frames)
    - Database: amino acid sequences
  - tblastn
    - Query: amino acid sequence(s)
    - Database: nucleic acid sequences
    - Automatically translate **database** to amino acid sequences (all frames)
  - tblastx
    - Query: nucleic acid sequence(s)
    - Automatically translate **query** to amino acid sequences (all frames)
    - Database: nucleic acid sequences
    - Automatically translate **database** to amino acid sequences (all frames)
- Query
  - A fasta file/text (one or multiple sequences)
- Database
  - RefSeq? Non-redudant? WGS?
  - Local
    - One genome
    - One proteome
    - Manual combination of sequences
- Parameters
  - Number of max targets
  - Expect (*e-value*)
  - Word size (length of intial exact match)
  - Output/Download format
  - ...

## Setup command line BLAST tool set

:::{NOTE}
You do NOT have `blast` command!  
Commands avaliable: `blastn`, `blastp`, `blastx`, `tblastn`, `tblastx`, `makeblastdb` etc.
:::

### Setup Windows machine in bash environment (git for windows)

1. Install https://gitforwindows.org/ first, you get access to `tar` command.
2. Download portable blast from NCBI:
   - https://blast.ncbi.nlm.nih.gov/Blast.cgi -> Download BLAST
   - ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ -> ncbi-blast-2.13.0+-x64-win64.tar.gz
3. Open 'Git Bash', change directory to the download files, do `tar xzf ncbi-blast-2.13.0+-x64-win64.tar.gz`
   - Equivalent to `tar -x -z -f ncbi-blast-2.13.0+-x64-win64.tar.gz`
   - `-x` To unpack the package (`.tar`)
   - `-z` Tells the program that this is a compressed package and the compression format is "gzip" (`.gz`)
   - `-f [file]` Specify the file to operate.
4. Copy everything from `ncbi-blast-2.13.0+/bin` to `/usr/bin` directory.

```shell
$ cd /c/User/[name]/Downloads/
$ ls
ncbi-blast-2.13.0+-x64-win64.tar.gz
ncbi-blast-2.13.0+/
$ cp /c/User/[name]/Downloads/ncbi-blast-2.13.0+/bin/* /usr/bin/
$ blastn -h
USAGE
  blastn [-h] [-help] [-import_search_strategy filename]
    [-export_search_strategy filename] [-task task_name] [-db database_name]
    ...
```

### Setup BLAST on MacOS/Linux

#### Solution 1

Download the program and put it in your environment variables.

1. Download portable blast from NCBI:
   - https://blast.ncbi.nlm.nih.gov/Blast.cgi -> Download BLAST
   - ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ 
   - ncbi-blast-2.13.0+-x64-macosx.tar.gz 
   - ncbi-blast-2.13.0+-x64-linux.tar.gz
2. Open terminal, change directory to download folder, do `tar xzf ncbi-blast-2.13.0+-x64-win64.tar.gz`
   - Equivalent to `tar -x -z -f ncbi-blast-2.13.0+-x64-win64.tar.gz`
   - `-x` To unpack the package (`.tar`)
   - `-z` Tells the program that this is a compressed package and the compression format is "gzip" (`.gz`)
   - `-f [file]` Specify the file to operate.
3. Put the directory `ncbi-blast-2.13.0+` in a location you can remember, eg. `cp -r ncbi-blast-2.13.0+ ~/`
4. Put `~/ncbi-blast-2.13.0+/bin/` in your environment variables. `export PATH="~/ncbi-blast-2.13.0+/bin/:$PATH"`

#### Solution 2

Use a package manager.

##### Linux

Need **sudo** right. Ubuntu and other Debian based system:

```shell
sudo apt install ncbi-blast+
```

##### MacOS

Install [homebrew](https://brew.sh/) (need **sudo** right)

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install BLAST, you do not need sudo right anymore.

```shell
brew install blast
```

### Setup BLAST using conda/micromamba

Check how to install conda (micromamba) [here](micromamba.md).

```shell
conda activate
# this will activate
conda install blast -c bioconda
```

## Run your first BLAST job locally

### Make a database

Download sequences you want to target.

1. Search an organism on NCBI, download its assembly
   - Genome / CDS / Proteins / RNA ...
2. Search a term on NCBI, download all matching sequences
   - Protein and Nucleotide sequences
   - Note "Gene" is information, "Nucleotide" is the sequence you want
3. Search a term on UniProt, download all matching sequences
4. "Write" a text fasta file by yourself
   - Make it up
   - Combine some of your downloaded sequences

:::{NOTE}
"Protein" and "Translated CDS" are different. "Protein" has higher certainty etc.  
"Gene" is information, "Nucleotide" is the sequence you want.
:::

```shell
makeblastdb -in [Genbank_ACC]_[RefSeq_ACC]_protein.faa -dbtype prot -title [Genbank_ACC]_[RefSeq_ACC]_prot -out [Genbank_ACC]_[RefSeq_ACC]_prot
```

### Make a query file

Use any text editor except "Word".

```shell
$ echo ">protein_A
KLCOSANAASLDFKJVOIKJASF
>protein_B
OSIJOJVOIFOJYUIQAJVK" > proteins.faa
```

### Run a BLAST job

Basic syntex

```shell
$ blastp -query protins.faa -db [Genbank_ACC]_[RefSeq_ACC]_prot
[blast output]
```

Or specying output

```shell
blastp -query protins.faa -db [Genbank_ACC]_[RefSeq_ACC]_prot > proteins_blastResult.txt
blastp -query protins.faa -db [Genbank_ACC]_[RefSeq_ACC]_prot -out proteins_blastResult.txt
```

With arguments. Short help `blastp -h`, full help can be obtained by `blastp -help`.

- `-outfmt 6` Tabular output
- `-max_target_seqs 2` Report max **two** match per sequence (when `-outfmt` > 4)
  - If you set `-outfmt` &le; 4, set both `-num_descriptions` and `-num_alignments` to 2
- `-max_hsps 1` For each match only show **one** aligned part
- `-evalue 1e-12` Set expectation value threshold to < 1 &times; 10<sup>-12</sup>
- `-word_size 7` Set initial exact match to be a lenth of 7 (default 11) (for finding CRISPR off-targets)
- `-num_threads 4` Use 4 threads for parallel computing

```shell
blastp -db [Genbank_ACC]_[RefSeq_ACC]_prot -query protins.faa -outfmt 6 -max_target_seqs 2 -max_hsps 1 -evalue 1e-12 -word_size 7 > proteins_blastResult.txt
```