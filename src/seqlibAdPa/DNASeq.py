# And there it is, our DNASeq class!
class DNASeq:
 
    #===SECTION=1========================================================
    
    ALPH = {
        'A' : 'T',   'T' : 'A',   'G' : 'C',   'C' : 'G',
        'K' : 'M',   'M' : 'K',   'B' : 'V',   'D' : 'H',
        'H' : 'D',   'V' : 'B',   'N' : 'N',   '-' : '-'
    }
    
    #===SECTION=2========================================================
    
    def __init__(self, seqid, title, seq):
        
        self.seqid = seqid
        self.title = title
        self.seq = seq
        
    #===SECTION=3========================================================
    
    @classmethod
    def from_file(cls, filename):
        seqs, seqid = {}, None
        alphaset = cls.ALPH.keys()

        f = open(filename)

        for line in f:
            if line[0] == '>':
                 header = line[1:-1].split(' ', 1)
                 seqid = header[0]
                 title = header[1] if len(header)>1 else ''
                 if seqid in seqs:
                     raise Exception(f'Non-unique: {seqid}')
                 seqs[seqid] = cls(seqid, title, [])
            else:
                 seqs[seqid].seq.append(line[:-1])
                 set(line[:-1]).issubset(alphaset)
        for seq in seqs.values():
            seq.seq = ''.join(seq.seq)
        f.close()

        return seqs
  
    #===SECTION=4========================================================

    def __repr__(self):
        if len(self.seq) <= 10:
            return f"{self.seq}..."
        else:
            return f"{self.seq[0:10]}..."

    #===SECTION=5========================================================

    def __len__(self):
        return len(self.seq)

    #===SECTION=6========================================================

    def __str__(self):
        lines = '\n'.join(
            self.seq[i:i+60] for i in range(0, len(self.seq), 60)
        )

        title = f' {self.title}' if self.title != '' else ''

        fasta = f">{self.seqid}{title}\n{lines}"

        return fasta

    #===SECTION=7=======================================================

    def revcmpl(self):

        seq = self.seq[::-1]

        seq_revcmpl = ''.join( self.ALPH[let] for let in seq )

        seqid = f"{self.seqid}_revcmpl"

        rev = DNASeq(seqid, self.title, seq_revcmpl)
        return rev

    #===SECTION=8========================================================

    def __getitem__(self, key):
        
        if isinstance(key, slice):

            start, end, step = key.start, key.stop, key.step
            
            if step is not None:
                raise KeyError('Step is not allowed in GenBank notation')
            
            if start is None:
                raise KeyError('start index is required')
            
            if end is None:
                raise KeyError('end index is required')
                
            if not np.issubdtype(type(start), np.integer) or \
               not np.issubdtype(type(end), np.integer):

                raise TypeError('Start and end must be integers')
            
            if start <= 0 or end <= 0:
                raise KeyError('Minimal value for start and end is 1')
                
            strand = 1 if start <= end else -1
            
            if strand == -1:
                start, end = end, start
            else: 
                pass
            
            seqid = f"{self.seqid}_loc({start}_{end})"
            
            start -= 1
            
            sub_seq = DNASeq(seqid, self.title, self.seq[start:end])
            
            if strand == -1:
                sub_seq = sub_seq.revcmpl()
                
            return sub_seq
                
        else:

            if not np.issubdtype(type(key), np.integer):
                raise TypeError('Index must be an integer')
                
            if key <= 0:
                raise KeyError('Minimal value of index is 1')

            return self.seq[key-1]

    #===SECTION=9========================================================

    def __add__(self, other):

        seqid = f"{self.seqid}_{other.seqid}"
        title = f"{self.title}_{other.title}"
        seq = self.seq + other.seq

        return type(self)(seqid, title, seq)

    #===SECTION=10========================================================

    def copy(self):
        return type(self)(self.seqid, self.title, self.seq)

__all__ = [ 'DNASeq' ]

