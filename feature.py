"""
Classes for features within sequences
"""

class Initiate_Site:
    def __init__(self,seq):
        self.pre = seq[:4]
        self.start = seq[4:7]
        self.first = seq[7:]
    def out(self):
        return [self.pre, self.start, self.first]

class Enter_CDS:
    def __init__(self,seq):
        self.Yratio = self._calYratio(seq[:-3])
        self.end2 = seq[-3:-1]
        self.first1 = seq[-1]
    def out(self):
        return [self.Yratio, self.end2, self.first1]
    def _calYratio(self,seq):
        total = len(seq)
        count = 0
        for ele in seq:
            if ele == 'C' or ele == 'T' or ele == 'Y':
                count += 1
        return count/total

class Out_CDS:
    def __init__(self,seq):
        self.pre2 = seq[:2]
        self.first2 = seq[2:4]
        self.next4 = seq[4:]
    def out(self):
        return [self.pre2, self.first2, self.next4]

# class Feature:
#     def __init__(self, seq_src, type, beg, end, strand,
#     src = '.', score = '.', phase = '.', id = None, pid = None):
#     self.seq_src =
#     self.type =
#     self.beg =
#     self.end =
#     self.strand =
#     self.src = src
#     self.score = score
#     self.phase = phase
#     self.id = id
#     self.pid = []
#     self.cid= []
