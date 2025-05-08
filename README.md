# The library overview
The `seqlibAdPa` library provides a class DNASeq with methods for handling DNA nucleotide sequences in python.

# Library installation using _pip_
Installation of the `seqlibAdPa` library with pip is quite straightforward:
```Bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple seqlibAdPa
```

# A quick example of the library usage
Learn how to use the `seqlibAdPa` library with examples provided below.

```Python
# Import the Seq class from the seqlibFiLa library
from seqlibAdPa import DNASeq

print('A letter complementary to "C":', DNASeq.ALPH['C'], '\n')

seq = DNASeq('new_seq', 'an exemplary sequence',
             'ATCGTAGGATCGGATTAGAGCGATTAGCTAG')

print(f'{seq.seqid} ({seq.title}): {seq.seq[:5]}...')


seqs = DNASeq.from_file('input/Staphylococcus_MLST_genes.fasta')

# Select one of the sequences by its sequence id (seqid):
seq = seqs['yqiL']

# Look up the length of the contained sequence:
len(seq)
```

# The `Seq` class in details
The `Seq` class (...)

## Initialisation
```Python
seq = DNASeq('new_seq', 'an exemplary sequence',
             'ATCGTAGGATCGGATTAGAGCGATTAGCTAG')
```

## Methods
- `__init__(self, seqid, title, seq)` &ndash; (...). Returns instance of the class with atributes as seqid, title and sequence (...).
- `fasta(self)` &ndash; (...). Returns (...).
- `from_file(cls, filename)` &ndash; (...). Allows you to load sequences from FASTA formated file (...).
- `__repr__(self)` &ndash; (...). Returns a string representation of an object as follows: first 10 nucleotides for longer sequences, and a whole sequence for sequences with the length 10 or shorter. (...).
- `__len__(self)` &ndash; (...). Returns length of the sequence in the object (...).
- `__str__(self)` &ndash; (...). Returns a string whenever obkect is being converted to one. (...).
- `revcmpl(self)` &ndash; (...). Returns new object od DNASeq type with reverse-complementary sequence to the object it is called from. Seqid of this objects is elongated by "_revcmpl", title is the same as in the original object. (...).
- `__getitem__(self, key)` &ndash; (...). Allows indexing and slicing the sequence. Rules follow FASTA format indexing and slicing (...).
- `__add__(self, other):` &ndash; (...). Returns new object of type(self) with one sequence elongated by the sequence form the other object. Seqid is the seqid from first object followed by "_" sign, and then the seqid from the second object. Title is just concatenated titles from both object, separated by "_" sign (...).
- `copy(self)` &ndash; (...). Returns an exact copy of  an object. (...).
